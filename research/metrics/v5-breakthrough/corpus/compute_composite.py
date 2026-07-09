#!/usr/bin/env python3
"""Breakthrough metric — FULL 3-signal composite + blind validation against labels.

Joins the SIGNIFICANCE signal (compute_significance.py, from GRO L8 sidecars) with the two
GRAPH signals (uptake / disruption) from breakthrough_v1_results.json, over the labelled set.

GRAPH-SIGNAL PROVENANCE (honest note):
  - POSITIVES: read straight from breakthrough_v1_results.json (landmark ancestors, resolved
    live via OpenAlex and scored against the in-corpus citer set). All 5 positives (incl.
    donanemab) now carry a GRO L8 shape, so every one gets a significance score and joins.
  - NEGATIVES: the GRO negatives (guo25c, yu25, zhu25b, ...) are mostly NOT the same papers
    v1 happened to sample, so we recompute their graph signals here using the *identical* v1
    logic (in_corpus_citers + CD-index) over the SAME local corpus graph (refs_raw.json /
    works.json). This was verified to reproduce v1 exactly on the two overlapping papers
    (Ami25: uptake=3, cd=-0.333; Hao25: uptake=6, cd=-0.333).

COMPOSITE:
  A breakthrough should show BOTH real novelty (significance) AND field response (uptake).
  We z-score uptake_per_year and significance across the labelled set and average them.
  cd_index is REPORTED but heavily down-weighted: in v1 it did NOT discriminate (positive
  landmarks span -0.84..+0.06, negatives span -1.0..0.0 — CD is dominated by lineage density,
  not breakthrough status on this shallow corpus).
      composite_z = 0.45*z(uptake_per_year) + 0.45*z(significance) + 0.10*z(cd_index)

RECENCY CONFOUND (stated, not hidden): positives are 2017-2023 landmarks; negatives are
  2025-2026. uptake_per_year is only partly age-robust and negatives simply have not had time
  to accumulate downstream edges. So every paper also gets a not_yet_vs_failed flag from its
  publication-date age against the corpus observation window, and the composite is reported
  BOTH with and without the uptake term so the reader can see how much of the separation is
  significance (age-independent) vs uptake (age-confounded).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OBS_WINDOW_END = 2026          # corpus observation window end (compile year)
YOUNG_AGE_MAX = 2              # <= this many years old => too young to have "failed"

# --- graph data for local negative computation (same corpus graph v1 used) ---------------
_refs = json.load(open(os.path.join(HERE, "refs_raw.json")))
CORPUS_REFS = _refs["refs_raw"]
WORKS = json.load(open(os.path.join(HERE, "works.json")))["meta"]

# GRO negative slug -> corpus cite key (CamelCase) in refs_raw/works
NEG_CITEKEY = {
    "guo25c": "Guo25c", "hao25": "Hao25", "yu25": "Yu25", "ami25": "Ami25",
    "zhu25b": "Zhu25b", "wan25c": "Wan25c", "raz25": "Raz25", "kho25": "Kho25",
    "ali26": "Ali26", "aks25": "Aks25",
}


def graph_signals_local(citekey):
    """Reproduce v1's uptake + CD-index for a corpus paper, purely from the local graph."""
    meta = WORKS[citekey]
    oid = meta["oid"]
    frefs = set(CORPUS_REFS.get(citekey, []))
    citers = [k for k, rr in CORPUS_REFS.items() if oid in rr]
    i = j = 0
    for c in citers:
        cs = set(CORPUS_REFS.get(c, []))
        if cs & frefs:
            i += 1                      # cites focal AND its predecessors -> consolidating
        else:
            j += 1                      # cites focal, ignores predecessors -> disrupting
    n = i + j
    cd = (j - i) / n if n else 0.0
    yr = meta.get("year") or 0
    age = max(1, OBS_WINDOW_END - yr)
    return {"year": yr, "oa_cited_by": meta.get("oa_cited_by", 0),
            "uptake_in_corpus": n, "uptake_per_year": round(n / age, 2),
            "consolidating_i": i, "disrupting_j": j, "cd_index": round(cd, 3)}


def zscores(values):
    n = len(values)
    mu = sum(values) / n
    var = sum((v - mu) ** 2 for v in values) / n
    sd = var ** 0.5
    if sd == 0:
        return [0.0] * n
    return [(v - mu) / sd for v in values]


def not_yet_vs_failed(year, uptake):
    """Distinguish young-empty (not-yet-determined) from old-empty (failed-to-become)."""
    age = OBS_WINDOW_END - year
    if age <= YOUNG_AGE_MAX:
        return "not_yet_determined"        # inside window, too young to judge downstream
    if uptake == 0:
        return "failed_to_become"          # old AND no downstream edges formed
    return "established_downstream"         # old with a real downstream footprint


def main():
    sig_rows = json.load(open(os.path.join(HERE, "significance_results.json")))
    v1_rows = {r["name"]: r for r in json.load(open(os.path.join(HERE, "breakthrough_v1_results.json")))}

    rows = []
    for s in sig_rows:
        name, label = s["name"], s["label"]
        if not s.get("gro_present", True):
            continue  # (none in practice; all 14 GRO dirs exist)
        if label == "POSITIVE":
            g = v1_rows.get(name)
            if not g:
                print("  WARN positive has no v1 graph row, skipping:", name)
                continue
            graph = {k: g[k] for k in ("year", "oa_cited_by", "uptake_in_corpus",
                                       "uptake_per_year", "consolidating_i", "disrupting_j", "cd_index")}
            graph_src = "v1_openalex"
        else:
            ck = NEG_CITEKEY.get(name)
            if ck not in WORKS:
                print("  WARN negative not in corpus graph, skipping:", name)
                continue
            graph = graph_signals_local(ck)
            graph_src = "local_corpus_graph"
        rows.append({
            "name": name, "label": label, "significance": s["significance"],
            "graph_source": graph_src, **graph,
        })

    # z-score the three signals across the whole labelled set
    up = zscores([r["uptake_per_year"] for r in rows])
    sg = zscores([r["significance"] for r in rows])
    cd = zscores([r["cd_index"] for r in rows])
    for r, zu, zs, zc in zip(rows, up, sg, cd):
        r["z_uptake_per_year"] = round(zu, 4)
        r["z_significance"] = round(zs, 4)
        r["z_cd_index"] = round(zc, 4)
        r["composite"] = round(0.45 * zu + 0.45 * zs + 0.10 * zc, 4)
        # significance-only composite (age-independent) to expose the recency confound
        r["composite_sig_only"] = round(zs, 4)
        r["not_yet_vs_failed"] = not_yet_vs_failed(r["year"], r["uptake_in_corpus"])

    out_json = os.path.join(HERE, "breakthrough_final_results.json")
    with open(out_json, "w") as f:
        json.dump(rows, f, indent=2)

    def mean(label, field):
        v = [r[field] for r in rows if r["label"] == label]
        return round(sum(v) / len(v), 4) if v else 0.0

    def sep(field):
        return "%s (POS=%s NEG=%s)" % (field, mean("POSITIVE", field), mean("NEGATIVE", field))

    print("=== BREAKTHROUGH FINAL — 3-signal composite over the labelled set ===")
    hdr = "%-9s %-17s %5s %6s %6s %6s | %7s %7s | %s" % (
        "LABEL", "name", "yr", "up/yr", "cd", "SIG", "comp", "sigOnly", "not_yet_vs_failed")
    print(hdr)
    print("-" * len(hdr))
    for r in sorted(rows, key=lambda x: -x["composite"]):
        print("%-9s %-17s %5s %6.2f %6.2f %6.3f | %7.3f %7.3f | %s" % (
            r["label"], r["name"], r["year"], r["uptake_per_year"], r["cd_index"],
            r["significance"], r["composite"], r["composite_sig_only"], r["not_yet_vs_failed"]))

    print("\n--- means POSITIVE vs NEGATIVE ---")
    for f in ("uptake_per_year", "cd_index", "significance", "composite", "composite_sig_only"):
        print("  " + sep(f))

    # separation check: does the composite fully separate the two classes?
    pos_c = [r["composite"] for r in rows if r["label"] == "POSITIVE"]
    neg_c = [r["composite"] for r in rows if r["label"] == "NEGATIVE"]
    pos_s = [r["significance"] for r in rows if r["label"] == "POSITIVE"]
    neg_s = [r["significance"] for r in rows if r["label"] == "NEGATIVE"]
    print("\n--- separation ---")
    print("  composite:    min(POS)=%.3f  max(NEG)=%.3f  -> clean=%s" % (
        min(pos_c), max(neg_c), min(pos_c) > max(neg_c)))
    print("  significance: min(POS)=%.3f  max(NEG)=%.3f  -> clean=%s" % (
        min(pos_s), max(neg_s), min(pos_s) > max(neg_s)))
    print("\nwrote", out_json)
    return rows


if __name__ == "__main__":
    main()
