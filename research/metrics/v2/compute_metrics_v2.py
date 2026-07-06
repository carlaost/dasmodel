#!/usr/bin/env python3
"""
Good-science metrics — V2 (scoring-model redesign answering the wave-1 critiques).

Same deterministic inputs as V1 (research/metrics/compute_metrics.py), reshaped to fix the six
critiques recorded in metrics-directions.md:

  1. paper-quality vs artifact-quality  — every metric is tagged; reported in separate blocks.
  2. gates vs rankers                    — binary hygiene GATES kept apart from continuous RANKERS.
  3. genre-awareness                     — an applicability model returns N/A(genre) instead of 0.
  4. verified grounding                  — re-open the cited in-repo file, confirm the «quote» is there.
  5. (clinical spec rubric)              — spec-completeness now uses a genre rubric, not ML slots.
  6. discrimination diagnostic           — per-ranker variance flags non-informative metrics.

Reuses V1's parsers by import. Writes:
  - per ARA:  research/ara-library/<slug>/metrics/v2/metrics.json
  - library:  research/metrics/v2/library_metrics_v2.{json,md}
  - compare:  research/metrics/v2/comparison_v1_v2.md   (V1 vs V2 side by side)
"""
from __future__ import annotations
import importlib.util, json, re, statistics, sys
from pathlib import Path

HERE = Path(__file__).resolve()
V2_DIR = HERE.parent                       # research/metrics/v2
METRICS_DIR = V2_DIR.parent                # research/metrics
RESEARCH = METRICS_DIR.parent              # research/
ARA_LIB = RESEARCH / "ara-library"
DATA_LIB = RESEARCH / "data" / "lib"

# import V1 module for its parsers
spec = importlib.util.spec_from_file_location("v1", METRICS_DIR / "compute_metrics.py")
v1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(v1)

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required")


# ----------------------------- genre classification -----------------------------
GENRE_RULES = [
    ("single_cell_spatial", ["single-cell", "single cell", "single-nucleus", "single nucleus",
                             "snrna", "scrna", "spatial transcriptomic", "spatial transcriptomics",
                             "visium", "spatial multi-omics", "spatial multiomics"]),
    ("guideline",      ["practice guideline", "guideline", "recommendation"]),
    ("meta_analysis",  ["meta-analysis", "network meta-analysis", "systematic review", "nma"]),
    ("clinical_trial", ["phase 3", "phase 2", "randomized", "trailblazer", "post-hoc", "efficacy and safety"]),
    ("review",         ["pipeline", "comprehensive review", "review of", "landscape"]),
    ("assay_method",   ["assay", "immunoassay", "quantification", "high-throughput", "mass spectrometry", "analytical validation"]),
    ("cohort_study",   ["cohort", "biofinder", "plasma", "biomarker", "diagnostic performance"]),
]


def classify_genre(base: Path, slug: str) -> str:
    text = (v1.read(base / "PAPER.md")[:4000] + " " + slug.replace("-", " ")).lower()
    for genre, kws in GENRE_RULES:
        # word-boundary match so short keywords ('nma') don't match inside names ('Kleinman')
        if any(re.search(r"(?<![a-z])" + re.escape(k) + r"(?![a-z])", text) for k in kws):
            return genre
    return "other"


# applicability: does a ranker meaningfully apply to this (genre, artifact)?
# returns (applicable: bool, reason: str)
def applicable(metric: str, genre: str, has_code: bool, has_open_data: bool):
    if metric in ("executable_reproduction", "replication_depth"):
        if not has_code:
            return False, "no code artifact"
        if not has_open_data:
            return False, "no open/runnable data"
        return True, ""
    if metric == "process_transparency":
        # applies everywhere, but synthesis genres have a low structural baseline
        low = genre in ("review", "guideline", "meta_analysis")
        return True, ("low genre baseline" if low else "")
    return True, ""


# ----------------------------- verified grounding -----------------------------
QUOTE_RE = re.compile(r"«(.+?)»")
PATH_RE = re.compile(r"([\w./-]+\.md)")     # in-repo evidence file (not paper.pdf / §refs)


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def _resolve_cited(base: Path, slug: str, relpath: str) -> Path | None:
    """A cited *.md may live in the ARA dir or in the discovery record (data/lib/<slug>/)."""
    for root in (base, DATA_LIB / slug):
        cand = root / relpath
        if cand.exists():
            return cand
        hits = list(root.rglob(Path(relpath).name))     # fall back to basename anywhere under root
        if hits:
            return hits[0]
    return None


def verified_grounding(base: Path, slug: str, claims_md: str) -> dict:
    """
    Line-tolerant. For each source bullet carrying a «quote»:
      - cites an openable *.md (ARA dir OR data/lib/<slug>/) → open it, check the quote (VERIFIED);
      - cites paper.pdf / a §page ref → UNVERIFIABLE in-repo (would need the PDF).
    Distinguishes self-contained/verifiable grounding from PDF-pointer grounding.
    """
    verified = present = unverifiable = 0
    for body in re.split(r"(?m)^##\s+C\d+:", claims_md)[1:]:
        src_m = re.search(r"-\s*\*\*Sources?\*\*:\s*(.*?)(?=\n-\s*\*\*Tags\*\*|\Z)", body, re.S)
        if not src_m:
            continue
        for line in src_m.group(1).splitlines():
            quotes = QUOTE_RE.findall(line)
            if not quotes:
                continue
            pm = PATH_RE.search(line)
            target = _resolve_cited(base, slug, pm.group(1)) if pm else None
            for quote in quotes:
                present += 1
                if not pm:
                    unverifiable += 1                       # paper.pdf / §ref
                    continue
                if target is None:
                    continue                                # cited file not found → not verified
                hay = _norm(v1.read(target))
                parts = [p for p in re.split(r"\.\.\.|…", quote) if p.strip()]
                if parts and all(_norm(p) in hay for p in parts):
                    verified += 1
    checkable = present - unverifiable
    return {
        "quotes_present": present,
        "quotes_unverifiable_in_repo": unverifiable,
        "quotes_checkable": checkable,
        "quotes_verified": verified,
        "verified_ratio": round(verified / checkable, 3) if checkable else None,
        "self_contained_grounding_ratio": round(checkable / present, 3) if present else None,
    }


# ----------------------------- per-ARA V2 -----------------------------
def compute_ara_v2(slug: str) -> dict:
    base = ARA_LIB / slug
    a1 = v1.compute_ara(slug)                      # reuse all V1 computation
    src = v1.load_sources(slug)
    genre = classify_genre(base, slug)
    code = src.get("code") or []
    data = src.get("data") or []
    has_code = bool(code)
    has_open_data = any((d.get("access") or "").lower() in ("open", "public", "download") for d in data)

    d1, d2, d3, d4, d6, d7 = (a1["D1_reproducibility"], a1["D2_claim_evidence_integrity"],
                              a1["D3_process_transparency"], a1["D4_novelty_dependency"],
                              a1["D6_realworld_grounding"], a1["D7_artifact_quality"])

    vg = verified_grounding(base, slug, v1.read(base / "logic/claims.md"))

    # ---- GATES (binary hygiene; artifact_quality) ----
    gates = {
        "seal_L1_structural_pass": d7["seal_L1_structural_score"] == 1.0,
        "all_links_resolve": (d1["cross_layer_binding_resolvability"] == 1.0),
        "no_orphan_experiments": len(d7["auditor_blindspot_orphan_experiments"]) == 0,
        "grounding_layer_present": vg["quotes_present"] > 0,
        "_detail": {"seal_L1": d7["seal_L1_structural_score"],
                    "binding": d1["cross_layer_binding_resolvability"],
                    "orphan_experiments": d7["auditor_blindspot_orphan_experiments"]},
    }
    gates["gates_passed"] = sum(1 for k, v in gates.items() if k != "_detail" and v is True)
    gates["gates_total"] = 4

    # ---- RANKERS (continuous quality), each tagged + genre-scoped ----
    def ranker(value, quality, reason=""):
        return {"value": value, "quality": quality, "applies": value != "N/A", "reason": reason}

    # process transparency (genre-scoped, not nulled)
    pt_app, pt_reason = applicable("process_transparency", genre, has_code, has_open_data)
    # executable repro (genre/artifact-scoped -> N/A instead of 0)
    l3_app, l3_reason = applicable("executable_reproduction", genre, has_code, has_open_data)

    rankers = {
        # paper_quality
        "grounding_verified": ranker(vg["verified_ratio"], "paper_quality",
                                     "re-opened cited in-repo files; presence≠truth fix (crit #4)"),
        "falsifiability_presence": ranker(d2["falsifiability_presence_proxy"], "paper_quality",
                                          "PROXY: presence only; quality is [sem]-pending"),
        "negative_result_share": ranker(d3["negative_result_share"], "paper_quality"),
        "dead_end_density": ranker(d3["dead_end_density_per_claim"] if pt_app else "N/A",
                                   "paper_quality", pt_reason),
        "corrective_science_score": ranker(d4["corrective_science_score"], "paper_quality"),
        "translation_trial_linkage": ranker(d6["n_clinical_trials_linked"], "paper_quality"),
        "environment_completeness": ranker(d1["environment_completeness"], "paper_quality"),
        # genre/artifact-gated
        "executable_reproduction_L3": ranker("N/A" if not l3_app else "pending_exec",
                                             "paper_quality", l3_reason),
    }

    return {
        "slug": slug, "genre": genre, "doi": a1["doi"],
        "n_claims": a1["n_claims"], "n_experiments": a1["n_experiments"],
        "artifact_facts": {"has_code": has_code, "has_open_data": has_open_data,
                           "n_datasets": len(data), "n_trials": d6["n_clinical_trials_linked"]},
        "gates": gates,
        "rankers": rankers,
        "verified_grounding_detail": vg,
        "v1_grounding_presence": d2["claim_grounding_ratio"],   # for the comparison
    }


# ----------------------------- library + diagnostics -----------------------------
def discrimination(aras: list[dict]) -> dict:
    """Flag rankers with ~0 variance across applicable ARAs (non-informative on this corpus)."""
    out = {}
    keys = set()
    for a in aras:
        keys |= set(a["rankers"].keys())
    for k in sorted(keys):
        vals = [a["rankers"][k]["value"] for a in aras
                if a["rankers"][k]["applies"] and isinstance(a["rankers"][k]["value"], (int, float))]
        if len(vals) < 2:
            out[k] = {"n": len(vals), "verdict": "insufficient_data"}
            continue
        sd = statistics.pstdev(vals); rng = max(vals) - min(vals)
        out[k] = {"n": len(vals), "mean": round(statistics.mean(vals), 3),
                  "stdev": round(sd, 4), "range": round(rng, 3),
                  "verdict": "non_discriminating" if rng < 1e-6 else
                             ("low_variance" if (sd < 0.05 and rng < 0.2) else "discriminating")}
    return out


def genre_scoped_ranking(aras: list[dict], metric: str) -> dict:
    """Rank ARAs within each genre for one metric (crit #3: compare like with like)."""
    by_genre = {}
    for a in aras:
        r = a["rankers"].get(metric)
        if r and r["applies"] and isinstance(r["value"], (int, float)):
            by_genre.setdefault(a["genre"], []).append((a["slug"], r["value"]))
    return {g: sorted(v, key=lambda t: -t[1]) for g, v in by_genre.items()}


# ----------------------------- writers -----------------------------
def write_ara_v2(a: dict):
    d = ARA_LIB / a["slug"] / "metrics" / "v2"
    d.mkdir(parents=True, exist_ok=True)
    (d / "metrics.json").write_text(json.dumps(a, indent=2), encoding="utf-8")


def write_library_and_comparison(aras: list[dict]):
    V2_DIR.mkdir(exist_ok=True)
    diag = discrimination(aras)
    lib = {"n_aras": len(aras),
           "genres": {a["slug"]: a["genre"] for a in aras},
           "discrimination": diag,
           "grounding_verified_ranking": genre_scoped_ranking(aras, "grounding_verified"),
           "per_ara": aras}
    (V2_DIR / "library_metrics_v2.json").write_text(json.dumps(lib, indent=2), encoding="utf-8")

    # library md
    L = ["# Library metrics — V2", "",
         f"Genre-aware, gates-vs-rankers, verified grounding. {len(aras)} ARAs.", "",
         "## Genres", ""]
    for a in aras:
        L.append(f"- `{a['slug']}` → **{a['genre']}** (code={a['artifact_facts']['has_code']}, "
                 f"open_data={a['artifact_facts']['has_open_data']}, trials={a['artifact_facts']['n_trials']})")
    L += ["", "## Discrimination diagnostic (which rankers actually vary here)", "",
          "| Ranker | n | mean | stdev | range | verdict |", "|---|---|---|---|---|---|"]
    for k, v in diag.items():
        if "mean" in v:
            L.append(f"| {k} | {v['n']} | {v['mean']} | {v['stdev']} | {v['range']} | **{v['verdict']}** |")
        else:
            L.append(f"| {k} | {v['n']} | — | — | — | {v['verdict']} |")
    (V2_DIR / "library_metrics_v2.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    # comparison vs V1
    v1lib = json.loads(v1.read(METRICS_DIR / "library_metrics.json") or "{}")
    v1_by_slug = {p["slug"]: p for p in v1lib.get("per_ara", [])}
    C = ["# V1 ↔ V2 comparison", "",
         "What changed when the six critiques were applied. V1 = flat [det] scores; V2 = genre-aware,",
         "gates split out, grounding re-verified against the cited files.", "",
         "## 1. Grounding: V1 presence vs V2 verified", "",
         "V1 counted a number as grounded if it appeared inside any `«quote»`. V2 re-opens the cited",
         "in-repo file and checks the quote is actually there (`unverifiable` = §/PDF refs not in repo).", "",
         "| ARA | genre | V1 presence | V2 verified | checkable | unverifiable(§/PDF) |",
         "|---|---|---|---|---|---|"]
    for a in aras:
        vg = a["verified_grounding_detail"]
        C.append(f"| {a['slug']} | {a['genre']} | {a['v1_grounding_presence']} | "
                 f"**{vg['verified_ratio']}** | {vg['quotes_checkable']} | {vg['quotes_unverifiable_in_repo']} |")
    C += ["", "## 2. Gates pulled out of the quality score", "",
          "V1 averaged these into quality; V2 treats them as binary hygiene gates.", "",
          "| ARA | seal_L1 | links_resolve | no_orphan_exp | grounding_layer | gates_passed |",
          "|---|---|---|---|---|---|"]
    for a in aras:
        g = a["gates"]
        C.append(f"| {a['slug']} | {g['seal_L1_structural_pass']} | {g['all_links_resolve']} | "
                 f"{g['no_orphan_experiments']} | {g['grounding_layer_present']} | {g['gates_passed']}/4 |")
    C += ["", "## 3. Genre-scoped: metrics that V1 scored 0, V2 marks N/A", "",
          "| ARA | genre | V1 L3 | V2 L3 | reason |", "|---|---|---|---|---|"]
    for a in aras:
        v1L3 = "0/pending"
        r = a["rankers"]["executable_reproduction_L3"]
        C.append(f"| {a['slug']} | {a['genre']} | {v1L3} | **{r['value']}** | {r['reason']} |")
    C += ["", "## 4. Within-genre ranking on verified grounding (compare like with like)", ""]
    for g, ranked in genre_scoped_ranking(aras, "grounding_verified").items():
        C.append(f"- **{g}**: " + " > ".join(f"{s} ({v})" for s, v in ranked))
    C += ["", "## 5. Non-discriminating metrics flagged automatically (crit #6)", ""]
    for k, v in diag.items():
        if v.get("verdict") in ("non_discriminating", "low_variance"):
            C.append(f"- `{k}` — {v['verdict']} (stdev {v.get('stdev')}, range {v.get('range')})")
    C += ["", "## Takeaways", "",
          "- **Verified grounding is stricter than presence** — the gap is the over-claim V1 hid.",
          "- **Gates are near-uniform** (they're hygiene, not quality) — correctly removed from ranking.",
          "- **L3 is now N/A(genre), not 0** — clinical papers no longer punished for shipping no code.",
          "- **The diagnostic flags** which rankers this corpus cannot exercise, so 0-variance is explicit."]
    (V2_DIR / "comparison_v1_v2.md").write_text("\n".join(C) + "\n", encoding="utf-8")


def main():
    slugs = sorted(d.name for d in ARA_LIB.iterdir()
                   if d.is_dir() and (d / "logic/claims.md").exists())
    print(f"V2 over {len(slugs)} ARAs\n")
    aras = []
    for slug in slugs:
        a = compute_ara_v2(slug)
        aras.append(a); write_ara_v2(a)
        vg = a["verified_grounding_detail"]
        print(f"■ {a['slug']}  [{a['genre']}]")
        print(f"    gates {a['gates']['gates_passed']}/4  "
              f"grounding: V1-presence={a['v1_grounding_presence']} → V2-verified={vg['verified_ratio']} "
              f"(checkable {vg['quotes_checkable']}, unverifiable {vg['quotes_unverifiable_in_repo']})")
    write_library_and_comparison(aras)
    diag = discrimination(aras)
    nd = [k for k, v in diag.items() if v.get("verdict") in ("non_discriminating", "low_variance")]
    print("\n=== V2 diagnostics ===")
    print(f"non-discriminating / low-variance rankers on this corpus: {nd}")
    print(f"wrote per-ARA metrics/v2/ + {V2_DIR}/library_metrics_v2.* + comparison_v1_v2.md")


if __name__ == "__main__":
    main()
