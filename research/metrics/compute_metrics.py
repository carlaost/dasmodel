#!/usr/bin/env python3
"""
Good-science metrics workflow over the ARA library.

Loads every compiled ARA under research/ara-library/<slug>/, its discovery record
(research/data/lib/<slug>/sources.yaml), and the library index (research/data/papers.json),
computes the metrics proposed in metrics-directions.md, prints the outcomes, and writes a
`/metrics` layer:
  - per ARA:      research/ara-library/<slug>/metrics/{metrics.json, metrics.md}
  - library roll: research/metrics/{library_metrics.json, library_metrics.md}

Honesty policy (mirrors the doc's det/sem/ext tags):
  - [det] metrics are computed exactly from the artifact.
  - [sem] metrics (need an LLM judge) and [ext] metrics (need a sandbox run or an external DB)
    are NOT fabricated. Where a deterministic *structural proxy* exists it is computed and
    flagged `proxy: true`; otherwise the metric is emitted with status "pending_model" /
    "pending_exec" / "pending_external" plus the inputs a later pass would need.

Pure stdlib + PyYAML. Re-runnable; overwrites the /metrics layer each run.
"""
from __future__ import annotations
import json, re, statistics, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # research/
ARA_LIB = ROOT / "ara-library"
DATA_LIB = ROOT / "data" / "lib"
PAPERS_JSON = ROOT / "data" / "papers.json"
OUT_DIR = ROOT / "metrics"

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

# Load-bearing quantities only: a number NOT embedded in an alphanumeric token, so nomenclature
# like p-tau217 / C231D181 / Table S2 is excluded while 0.859, 95%, 0.04 are kept.
NUM_RE = re.compile(r"(?<![A-Za-z0-9_])\d+(?:\.\d+)?%?(?![A-Za-z0-9_])")
ENV_FIELDS = ["Language", "Framework", "Hardware", "Data source", "dependenc", "Protocol", "seed"]
RW_TYPES = ["imports", "extends", "refutes", "bounds", "baseline"]


# ----------------------------- parsers -----------------------------
def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""


def _field(block: str, name: str) -> str:
    """Value of a `- **Name**: ...` line (single line)."""
    m = re.search(rf"-\s*\*\*{re.escape(name)}\*\*:\s*(.*)", block)
    return m.group(1).strip() if m else ""


def parse_claims(md: str) -> list[dict]:
    claims = []
    blocks = re.split(r"(?m)^##\s+(C\d+):", md)
    # blocks = [preamble, id1, body1, id2, body2, ...]
    for i in range(1, len(blocks), 2):
        cid, body = blocks[i], blocks[i + 1]
        statement = _field(body, "Statement")
        # Sources block: from '- **Sources**:' to the next top-level field or end
        src_m = re.search(r"-\s*\*\*Sources\*\*:\s*(.*?)(?=\n-\s*\*\*Tags\*\*|\Z)", body, re.S)
        src_block = src_m.group(1) if src_m else ""
        quotes = re.findall(r"«([^»]*)»", src_block)
        nums = set(NUM_RE.findall(statement))
        grounded = {n for n in nums if any(n in q for q in quotes)}
        claims.append({
            "id": cid,
            "status": _field(body, "Status").lower(),
            "has_falsification": bool(_field(body, "Falsification criteria")),
            "proof_ids": re.findall(r"E\d+", _field(body, "Proof")),
            "dep_ids": re.findall(r"C\d+", _field(body, "Dependencies")),
            "statement_nums": len(nums),
            "grounded_nums": len(grounded),
            "n_source_quotes": len(quotes),
            "statement": statement,
        })
    return claims


def parse_experiments(md: str) -> list[dict]:
    exps = []
    blocks = re.split(r"(?m)^##\s+(E\d+):", md)
    for i in range(1, len(blocks), 2):
        eid, body = blocks[i], blocks[i + 1]
        setup = re.search(r"-\s*\*\*Setup\*\*:(.*?)(?=\n-\s*\*\*|\Z)", body, re.S)
        setup_txt = setup.group(1) if setup else ""
        slots = ["Model", "Hardware", "Dataset", "System"]
        filled = sum(1 for s in slots if re.search(rf"{s}\s*:\s*\S", setup_txt))
        exps.append({
            "id": eid,
            "verifies": re.findall(r"C\d+", _field(body, "Verifies")),
            "setup_slots_filled": filled,
            "setup_slots_total": len(slots),
        })
    return exps


def parse_related_work(md: str) -> dict:
    profile = {t: 0 for t in RW_TYPES}
    for _id, body in re.findall(r"(?m)^##\s+(RW\d+):(.*?)(?=(?:\n##\s)|\Z)", md, re.S):
        typ = _field(body, "Type").lower()
        for t in RW_TYPES:
            if typ.startswith(t):
                profile[t] += 1
                break
    dois = re.findall(r"(?im)-\s*\*\*DOI\*\*:\s*([^\s]+)", md)
    n_rw = len(re.findall(r"(?m)^##\s+RW\d+:", md))
    return {"profile": profile, "n_rw_blocks": n_rw, "dois": [d.strip().lower() for d in dois]}


def flatten_tree(nodes, out):
    if not isinstance(nodes, list):
        return
    for n in nodes:
        if not isinstance(n, dict):
            continue
        out.append(n)
        flatten_tree(n.get("children"), out)


def parse_tree(text: str) -> list[dict]:
    try:
        doc = yaml.safe_load(text) or {}
    except yaml.YAMLError:
        return []
    out = []
    flatten_tree(doc.get("tree", []), out)
    return out


def parse_environment(md: str) -> dict:
    present = {f: bool(re.search(rf"(?i)\*\*[^*]*{re.escape(f)}[^*]*\*\*:\s*\S", md)) for f in ENV_FIELDS}
    return {"present": present, "n_present": sum(present.values()), "n_total": len(ENV_FIELDS)}


def parse_evidence_claim_refs(md: str) -> set[str]:
    return set(re.findall(r"C\d+", md))


def count_concepts(md: str) -> int:
    return len(re.findall(r"(?m)^##\s+\S", md))


def load_sources(slug: str) -> dict:
    p = DATA_LIB / slug / "sources.yaml"
    try:
        return yaml.safe_load(read(p)) or {}
    except yaml.YAMLError:
        return {}


# ----------------------------- per-ARA metrics -----------------------------
def compute_ara(slug: str) -> dict:
    base = ARA_LIB / slug
    claims = parse_claims(read(base / "logic/claims.md"))
    exps = parse_experiments(read(base / "logic/experiments.md"))
    rw = parse_related_work(read(base / "logic/related_work.md"))
    tree = parse_tree(read(base / "trace/exploration_tree.yaml"))
    env = parse_environment(read(base / "src/environment.md"))
    ev_refs = parse_evidence_claim_refs(read(base / "evidence/README.md"))
    n_concepts = count_concepts(read(base / "logic/concepts.md"))
    src = load_sources(slug)

    claim_ids = {c["id"] for c in claims}
    exp_ids = {e["id"] for e in exps}

    # ---- D1 reproducibility ----
    links_total = links_ok = 0
    for c in claims:
        for e in c["proof_ids"]:
            links_total += 1; links_ok += (e in exp_ids)
    for e in exps:
        for c in e["verifies"]:
            links_total += 1; links_ok += (c in claim_ids)
    for c in ev_refs:
        links_total += 1; links_ok += (c in claim_ids)
    setup_filled = sum(e["setup_slots_filled"] for e in exps)
    setup_total = sum(e["setup_slots_total"] for e in exps)
    code = src.get("code") or []
    D1 = {
        "cross_layer_binding_resolvability": round(links_ok / links_total, 3) if links_total else None,
        "n_links_resolved": links_ok, "n_links_total": links_total,
        "environment_completeness": round(env["n_present"] / env["n_total"], 3),
        "env_fields_present": env["n_present"], "env_fields_total": env["n_total"],
        "spec_completeness_setup_proxy": round(setup_filled / setup_total, 3) if setup_total else None,
        "spec_completeness_rubric": {"status": "pending_model",
                                     "note": "needs LLM full/partial/absent labels vs a reproduction rubric"},
        "executable_reproduction_L3": {"status": "pending_exec",
                                       "has_code_repo": bool(code),
                                       "note": "needs sandboxed run; this library has 0 code repos so L3 is largely N/A"},
    }

    # ---- D2 claim & evidence integrity ----
    tot_nums = sum(c["statement_nums"] for c in claims)
    grounded = sum(c["grounded_nums"] for c in claims)
    statuses = {}
    for c in claims:
        statuses[c["status"] or "unspecified"] = statuses.get(c["status"] or "unspecified", 0) + 1
    claims_with_proof = sum(1 for c in claims if c["proof_ids"])
    exps_verifying = {c for e in exps for c in e["verifies"]}
    orphan_claims = [c["id"] for c in claims if not c["proof_ids"]]
    orphan_exps = [e["id"] for e in exps if not e["verifies"]]
    D2 = {
        "claim_grounding_ratio": round(grounded / tot_nums, 3) if tot_nums else None,
        "grounded_numbers": grounded, "statement_numbers": tot_nums,
        "falsifiability_presence_proxy": round(sum(c["has_falsification"] for c in claims) / len(claims), 3) if claims else None,
        "status_honesty_mix": statuses,
        "orphan_claims_no_proof": orphan_claims,
        "orphan_experiments_no_claim": orphan_exps,
        "n_claims": len(claims), "n_experiments": len(exps),
        "evidence_relevance_D1": {"status": "pending_model"},
        "falsifiability_quality_D2": {"status": "pending_model"},
        "scope_calibration_D3": {"status": "pending_model"},
    }

    # ---- D3 process transparency ----
    types = {}
    for n in tree:
        types[n.get("type", "?")] = types.get(n.get("type", "?"), 0) + 1
    n_nodes = len(tree) or 1
    dead = [n for n in tree if n.get("type") == "dead_end"]
    dead_complete = [n for n in dead if n.get("hypothesis") and n.get("failure_mode") and n.get("lesson")]
    decisions = [n for n in tree if n.get("type") == "decision"]
    alt_counts = [len(n.get("alternatives") or []) for n in decisions]
    explicit = sum(1 for n in tree if n.get("support_level") == "explicit")
    refuted = sum(1 for c in claims if c["status"] == "refuted")
    D3 = {
        "dead_end_density_per_claim": round(len(dead_complete) / len(claims), 3) if claims else None,
        "n_dead_ends": len(dead), "n_dead_ends_complete": len(dead_complete),
        "decision_branching_factor": round(statistics.mean(alt_counts), 2) if alt_counts else None,
        "explicit_vs_inferred_ratio": round(explicit / n_nodes, 3),
        "failure_knowledge_preservation": round((types.get("dead_end", 0) + types.get("pivot", 0)) / n_nodes, 3),
        "negative_result_share": round((refuted + len(dead_complete)) / (len(claims) + len(dead)), 3) if (len(claims) + len(dead)) else None,
        "node_type_counts": types,
    }

    # ---- D4 novelty & dependency ----
    prof = rw["profile"]
    D4 = {
        "typed_delta_profile": prof,
        "corrective_science_score": 2 * (prof["refutes"] + prof["bounds"]) + prof["extends"],
        "n_related_work_blocks": rw["n_rw_blocks"],
        "concept_count": n_concepts,
        "novel_claim_count": {"status": "pending_model",
                              "authored_claims": len(claims),
                              "note": "needs oshima original-flag + FOL dedup; authored_claims is an upper bound"},
    }

    # ---- D6 real-world grounding ----
    data = src.get("data") or []
    trials = src.get("clinical_trials") or []
    pdf = src.get("pdf") or {}
    D6 = {
        "n_datasets_linked": len(data),
        "n_datasets_verified": sum(1 for d in data if d.get("verified")),
        "n_clinical_trials_linked": len(trials),
        "verified_ncts": [t.get("nct") for t in trials if t.get("verified")],
        "n_code_repos": len(code),
        "pdf_open_access": bool(pdf.get("oa")),
        "pdf_downloaded": bool(pdf.get("downloaded")),
        "claim_vs_endpoint_concordance": {"status": "pending_external", "note": "needs ClinicalTrials.gov endpoint pull + LLM finding"},
        "target_compound_resolvability": {"status": "pending_external", "note": "needs ChEMBL resolution"},
    }

    # ---- D7 artifact quality (meta) ----
    core = ["PAPER.md", "logic/claims.md", "logic/experiments.md", "logic/problem.md",
            "logic/concepts.md", "logic/related_work.md", "logic/solution/constraints.md",
            "src/environment.md", "trace/exploration_tree.yaml", "evidence/README.md"]
    core_present = sum(1 for f in core if (base / f).exists())
    D7 = {
        "seal_L1_structural_score": round(core_present / len(core), 3),
        "core_files_present": core_present, "core_files_total": len(core),
        "auditor_blindspot_orphan_experiments": orphan_exps,
        "compilation_fidelity": {"status": "pending_model", "note": "needs source-vs-ARA recall sampling"},
    }

    return {
        "slug": slug,
        "doi": (src.get("paper") or {}).get("doi"),
        "n_claims": len(claims), "n_experiments": len(exps),
        "D1_reproducibility": D1, "D2_claim_evidence_integrity": D2,
        "D3_process_transparency": D3, "D4_novelty_dependency": D4,
        "D6_realworld_grounding": D6, "D7_artifact_quality": D7,
        "_claims": claims, "_rw_dois": rw["dois"],
        "_ncts": [t.get("nct") for t in trials],
    }


# ----------------------------- library graph (D5) -----------------------------
def _tokset(s: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if len(w) > 3}


def compute_library_graph(aras: list[dict]) -> dict:
    # shared clinical-trial NCT clusters
    nct_map: dict[str, list[str]] = {}
    for a in aras:
        for nct in a["_ncts"]:
            if nct:
                nct_map.setdefault(nct, []).append(a["slug"])
    shared_ncts = {n: s for n, s in nct_map.items() if len(s) > 1}

    # in-library citation reuse: does one ARA's related_work cite another ARA's DOI?
    doi_owner = {a["doi"].lower(): a["slug"] for a in aras if a.get("doi")}
    reuse_edges = []
    for a in aras:
        for d in a["_rw_dois"]:
            if d in doi_owner and doi_owner[d] != a["slug"]:
                reuse_edges.append({"from": a["slug"], "cites": doi_owner[d], "doi": d})

    # claim redundancy proxy: pairwise Jaccard over claim-statement tokens (>=0.5 = near-dup)
    all_claims = [(a["slug"], c["id"], _tokset(c["statement"])) for a in aras for c in a["_claims"]]
    near_dup = 0; dup_pairs = []
    for i in range(len(all_claims)):
        for j in range(i + 1, len(all_claims)):
            s1, c1, t1 = all_claims[i]; s2, c2, t2 = all_claims[j]
            if s1 == s2 or not t1 or not t2:
                continue
            jac = len(t1 & t2) / len(t1 | t2)
            if jac >= 0.5:
                near_dup += 1
                dup_pairs.append({"a": f"{s1}:{c1}", "b": f"{s2}:{c2}", "jaccard": round(jac, 2)})
    total_claims = len(all_claims)
    return {
        "n_papers": len(aras), "n_claims_total": total_claims,
        "shared_trial_clusters": shared_ncts,
        "n_shared_trial_clusters": len(shared_ncts),
        "in_library_citation_reuse_edges": reuse_edges,
        "claim_redundancy": {
            "near_duplicate_pairs": near_dup,
            "redundancy_rate_proxy": round(near_dup / total_claims, 4) if total_claims else 0,
            "examples": dup_pairs[:10],
            "method": "token Jaccard >=0.5 over claim statements (proxy; FOL dedup pending)",
        },
        "corroboration_via_shared_trials": {n: s for n, s in shared_ncts.items()},
        "fol_claim_graph": {"status": "pending_model",
                            "note": "corroboration/contradiction/replication need oshima typed evidence + fol_json"},
    }


# ----------------------------- writers -----------------------------
def strip_private(d: dict) -> dict:
    return {k: v for k, v in d.items() if not k.startswith("_")}


def write_ara_layer(a: dict):
    mdir = ARA_LIB / a["slug"] / "metrics"
    mdir.mkdir(exist_ok=True)
    pub = strip_private(a)
    (mdir / "metrics.json").write_text(json.dumps(pub, indent=2), encoding="utf-8")
    d1, d2, d3, d4, d6, d7 = (a["D1_reproducibility"], a["D2_claim_evidence_integrity"],
                              a["D3_process_transparency"], a["D4_novelty_dependency"],
                              a["D6_realworld_grounding"], a["D7_artifact_quality"])
    md = f"""# Metrics — {a['slug']}

Extra ARA layer computed by `research/metrics/compute_metrics.py`. `[det]` = computed exactly;
`pending_*` = needs an LLM judge / sandbox run / external DB (not fabricated).

- Claims: {a['n_claims']} · Experiments: {a['n_experiments']} · DOI: {a['doi']}

## D1 Reproducibility
- Cross-layer binding resolvability: **{d1['cross_layer_binding_resolvability']}** ({d1['n_links_resolved']}/{d1['n_links_total']} links)
- Environment completeness: **{d1['environment_completeness']}** ({d1['env_fields_present']}/{d1['env_fields_total']} fields)
- Spec-completeness (setup proxy): {d1['spec_completeness_setup_proxy']}
- Executable reproduction (L3): {d1['executable_reproduction_L3']['status']} (has code repo: {d1['executable_reproduction_L3']['has_code_repo']})

## D2 Claim & evidence integrity
- Claim-grounding ratio: **{d2['claim_grounding_ratio']}** ({d2['grounded_numbers']}/{d2['statement_numbers']} numbers)
- Falsifiability presence: {d2['falsifiability_presence_proxy']}
- Status mix: {d2['status_honesty_mix']}
- Orphan claims (no proof): {d2['orphan_claims_no_proof']}
- Orphan experiments (no claim): {d2['orphan_experiments_no_claim']}

## D3 Process transparency & negative knowledge
- Dead-end density / claim: **{d3['dead_end_density_per_claim']}** ({d3['n_dead_ends_complete']} complete dead-ends)
- Decision branching factor: {d3['decision_branching_factor']}
- Explicit-vs-inferred ratio: {d3['explicit_vs_inferred_ratio']}
- Failure-knowledge preservation: {d3['failure_knowledge_preservation']}
- Negative-result share: {d3['negative_result_share']}
- Node types: {d3['node_type_counts']}

## D4 Novelty & dependency structure
- Typed-delta profile: {d4['typed_delta_profile']}
- Corrective-science score: **{d4['corrective_science_score']}**
- Concepts defined: {d4['concept_count']} · related-work blocks: {d4['n_related_work_blocks']}

## D6 Real-world grounding & translation
- Clinical trials linked: **{d6['n_clinical_trials_linked']}** (verified NCTs: {d6['verified_ncts']})
- Datasets linked: {d6['n_datasets_linked']} ({d6['n_datasets_verified']} verified) · code repos: {d6['n_code_repos']}
- PDF: OA={d6['pdf_open_access']}, downloaded={d6['pdf_downloaded']}

## D7 Artifact quality (meta)
- Seal L1 structural: **{d7['seal_L1_structural_score']}** ({d7['core_files_present']}/{d7['core_files_total']} core files)
- Auditor blind-spot (orphan experiments): {d7['auditor_blindspot_orphan_experiments']}
"""
    (mdir / "metrics.md").write_text(md, encoding="utf-8")


def write_library_rollup(aras: list[dict], graph: dict):
    OUT_DIR.mkdir(exist_ok=True)

    def dist(path_fn):
        vals = [v for v in (path_fn(a) for a in aras) if isinstance(v, (int, float))]
        if not vals:
            return None
        return {"mean": round(statistics.mean(vals), 3), "median": round(statistics.median(vals), 3),
                "min": min(vals), "max": max(vals), "n": len(vals)}

    agg = {
        "cross_layer_binding_resolvability": dist(lambda a: a["D1_reproducibility"]["cross_layer_binding_resolvability"]),
        "environment_completeness": dist(lambda a: a["D1_reproducibility"]["environment_completeness"]),
        "claim_grounding_ratio": dist(lambda a: a["D2_claim_evidence_integrity"]["claim_grounding_ratio"]),
        "falsifiability_presence": dist(lambda a: a["D2_claim_evidence_integrity"]["falsifiability_presence_proxy"]),
        "dead_end_density_per_claim": dist(lambda a: a["D3_process_transparency"]["dead_end_density_per_claim"]),
        "decision_branching_factor": dist(lambda a: a["D3_process_transparency"]["decision_branching_factor"]),
        "explicit_vs_inferred_ratio": dist(lambda a: a["D3_process_transparency"]["explicit_vs_inferred_ratio"]),
        "corrective_science_score": dist(lambda a: a["D4_novelty_dependency"]["corrective_science_score"]),
        "clinical_trials_linked": dist(lambda a: a["D6_realworld_grounding"]["n_clinical_trials_linked"]),
        "seal_L1_structural_score": dist(lambda a: a["D7_artifact_quality"]["seal_L1_structural_score"]),
    }
    out = {"n_aras": len(aras), "aggregates": agg, "D5_library_graph": graph,
           "per_ara": [strip_private(a) for a in aras]}
    (OUT_DIR / "library_metrics.json").write_text(json.dumps(out, indent=2), encoding="utf-8")

    lines = ["# Library metrics rollup", "",
             f"Computed over **{len(aras)}** compiled ARAs by `research/metrics/compute_metrics.py`.",
             "`pending_*` metrics need an LLM judge / sandbox / external DB and are not fabricated.", "",
             "## Aggregate distributions (per-ARA [det] metrics)", "",
             "| Metric | mean | median | min | max | n |", "|---|---|---|---|---|---|"]
    for k, v in agg.items():
        if v:
            lines.append(f"| {k} | {v['mean']} | {v['median']} | {v['min']} | {v['max']} | {v['n']} |")
    g = graph
    lines += ["", "## D5 Cross-library claim graph", "",
              f"- Papers: {g['n_papers']} · total claims: {g['n_claims_total']}",
              f"- Shared clinical-trial clusters (corroboration proxy): **{g['n_shared_trial_clusters']}**",
              f"- In-library citation-reuse edges: **{len(g['in_library_citation_reuse_edges'])}**",
              f"- Claim redundancy (proxy): {g['claim_redundancy']['near_duplicate_pairs']} near-dup pairs, "
              f"rate {g['claim_redundancy']['redundancy_rate_proxy']}",
              f"- FOL claim graph: {g['fol_claim_graph']['status']}", ""]
    if g["shared_trial_clusters"]:
        lines.append("### Shared-trial clusters")
        for nct, slugs in g["shared_trial_clusters"].items():
            lines.append(f"- `{nct}`: {', '.join(slugs)}")
    if g["in_library_citation_reuse_edges"]:
        lines += ["", "### In-library citation reuse"]
        for e in g["in_library_citation_reuse_edges"]:
            lines.append(f"- {e['from']} → cites → {e['cites']} ({e['doi']})")
    (OUT_DIR / "library_metrics.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ----------------------------- main -----------------------------
def main():
    if not ARA_LIB.exists():
        sys.exit(f"no ARA library at {ARA_LIB}")
    slugs = sorted(d.name for d in ARA_LIB.iterdir()
                   if d.is_dir() and (d / "logic/claims.md").exists())
    print(f"Loading {len(slugs)} compiled ARAs from {ARA_LIB}\n")
    aras = []
    for slug in slugs:
        a = compute_ara(slug)
        aras.append(a)
        write_ara_layer(a)
        d1, d2, d3, d6 = (a["D1_reproducibility"], a["D2_claim_evidence_integrity"],
                          a["D3_process_transparency"], a["D6_realworld_grounding"])
        print(f"■ {slug}")
        print(f"    claims={a['n_claims']} exps={a['n_experiments']}  "
              f"binding={d1['cross_layer_binding_resolvability']} env={d1['environment_completeness']}")
        print(f"    grounding={d2['claim_grounding_ratio']} falsifiable={d2['falsifiability_presence_proxy']} "
              f"status={d2['status_honesty_mix']}")
        print(f"    dead_ends/claim={d3['dead_end_density_per_claim']} branching={d3['decision_branching_factor']} "
              f"explicit={d3['explicit_vs_inferred_ratio']}  trials={d6['n_clinical_trials_linked']}{d6['verified_ncts']}")

    graph = compute_library_graph(aras)
    write_library_rollup(aras, graph)

    print("\n=== LIBRARY ROLLUP ===")
    print(f"ARAs: {graph['n_papers']}  total claims: {graph['n_claims_total']}")
    print(f"shared-trial clusters (corroboration proxy): {graph['n_shared_trial_clusters']} -> "
          f"{list(graph['shared_trial_clusters'].keys())}")
    print(f"in-library citation-reuse edges: {len(graph['in_library_citation_reuse_edges'])}")
    print(f"claim redundancy (proxy): {graph['claim_redundancy']['near_duplicate_pairs']} near-dup pairs "
          f"(rate {graph['claim_redundancy']['redundancy_rate_proxy']})")
    print(f"\nWrote per-ARA /metrics layers + {OUT_DIR}/library_metrics.{{json,md}}")


if __name__ == "__main__":
    main()
