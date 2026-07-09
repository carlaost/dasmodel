#!/usr/bin/env python3
"""Breakthrough metric v1 — graph signals (disruption + uptake) over a LABELLED set,
computed against the REAL citation graph (all-papers.csv corpus, resolved via OpenAlex).

Two of the three tier-separated signals from shapes/12_breakthrough.md are computable
purely from the graph (the third, significance, needs GRO L8 sidecars — separate pass):

  UPTAKE      = # corpus papers that cite the focal work (measured downstream in-corpus).
  DISRUPTION  = CD-index-style over the focal's in-corpus citers:
                among papers citing focal F, do they ALSO cite F's own references
                (consolidating, i) or not (disrupting, j)?  CD = (j - i) / (i + j).
                +1 => disruptive (citers ignore F's predecessors), -1 => consolidating.

Positives = landmark ancestors (known breakthroughs) fetched live.
Negatives = derivative-cluster corpus papers (GBD-burden + DL-detection + facts/figures).
NOTE the recency confound (positives are 2017-23, negatives 2025-26) — disruption is a
ratio (age-robust); raw uptake is NOT, so we also report uptake-per-year.
"""
import json, os, time, urllib.parse, urllib.request
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
MAILTO = "carla@positron.vc"
API = "https://api.openalex.org/works"

refs_raw = json.load(open(os.path.join(HERE, "refs_raw.json")))
CORPUS_REFS = refs_raw["refs_raw"]          # cite_key -> [openalex ref ids]
ID2KEY = refs_raw["id2key"]
works = json.load(open(os.path.join(HERE, "works.json")))["meta"]

# --- POSITIVES: landmark ancestors, by DOI (known breakthroughs) ---
POS_DOIS = {
    "lecanemab":  "10.1056/nejmoa2212948",
    "donanemab":  "10.1001/jama.2023.13239",
    "ptau217":    "10.1001/jama.2020.12134",
    "dam_microglia": "10.1016/j.cell.2017.05.018",
    "nia_aa_framework": "10.1016/j.jalz.2018.02.018",
}
# --- NEGATIVES: derivative-cluster corpus papers (cite keys as they appear in the CSV) ---
# resolved by DOI->key below from the ARA front matter set we know is derivative
NEG_ARA_DOIS = {
    # GBD global-burden cluster + facts/figures + DL-detection (all 2025-26 derivative work)
    "gbd_wan25c": None, "gbd_zhu25b": None, "gbd_yu25": None, "dl_raz25": None,
}


def get(url):
    for a in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "gro-bt/1.0 (mailto:%s)" % MAILTO})
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception:
            if a == 3:
                raise
            time.sleep(2 * (a + 1))


def fetch_by_doi(dois):
    out = {}
    filt = "doi:" + "|".join(dois)
    url = "%s?filter=%s&per-page=50&mailto=%s&select=id,doi,publication_year,cited_by_count,referenced_works,title" % (
        API, urllib.parse.quote(filt, safe="|:"), MAILTO)
    r = get(url)
    for w in r.get("results", []):
        d = (w.get("doi") or "").replace("https://doi.org/", "").lower()
        out[d] = w
    return out


def in_corpus_citers(focal_id):
    """corpus papers whose reference list includes focal_id"""
    return [k for k, refs in CORPUS_REFS.items() if focal_id in refs]


def disruption(focal_id, focal_refs):
    """CD-index over in-corpus citers of focal."""
    focal_refs = set(focal_refs)
    citers = in_corpus_citers(focal_id)
    i = j = 0
    for c in citers:
        cset = set(CORPUS_REFS.get(c, []))
        if cset & focal_refs:
            i += 1          # cites focal AND its predecessors -> consolidating
        else:
            j += 1          # cites focal, ignores its predecessors -> disruptive
    n = i + j
    cd = (j - i) / n if n else 0.0
    return {"n_citers_in_corpus": n, "consolidating_i": i, "disrupting_j": j, "cd_index": round(cd, 3)}


def score(label, name, w):
    fid = w["id"]
    yr = w.get("publication_year") or 0
    up = len(in_corpus_citers(fid))
    age = max(1, 2026 - yr)
    dis = disruption(fid, w.get("referenced_works", []))
    return {"label": label, "name": name, "year": yr, "oa_cited_by": w.get("cited_by_count", 0),
            "uptake_in_corpus": up, "uptake_per_year": round(up / age, 2),
            **dis, "title": w.get("title", "")[:80]}


def main():
    pos_w = fetch_by_doi(list(POS_DOIS.values()))
    rows = []
    for name, doi in POS_DOIS.items():
        w = pos_w.get(doi)
        if w:
            rows.append(score("POSITIVE", name, w))
        else:
            print("  WARN positive not resolved:", name, doi)

    # negatives: pick derivative corpus papers by title keyword, fetch their works for refs
    neg_keys = []
    for k, m in works.items():
        t = m["title"].lower()
        if ("global burden" in t or "facts and figures" in t or
                "deep learning" in t and "detection" in t or "disability-adjusted" in t):
            neg_keys.append((k, m))
    neg_keys = neg_keys[:8]
    neg_dois = [m["doi"] for _, m in neg_keys if m.get("doi")]
    neg_w = fetch_by_doi(neg_dois)
    for k, m in neg_keys:
        w = neg_w.get(m["doi"])
        if w:
            rows.append(score("NEGATIVE", k, w))

    json.dump(rows, open(os.path.join(HERE, "breakthrough_v1_results.json"), "w"), indent=2)

    def avg(label, field):
        v = [r[field] for r in rows if r["label"] == label]
        return round(sum(v) / len(v), 3) if v else 0.0

    print("\n=== BREAKTHROUGH v1 — graph signals over the labelled set ===")
    hdr = "%-9s %-16s %4s %7s %7s %8s  %s" % ("LABEL", "name", "yr", "uptake", "up/yr", "CD-index", "title")
    print(hdr); print("-" * len(hdr))
    for r in sorted(rows, key=lambda x: (x["label"], -x["uptake_in_corpus"])):
        print("%-9s %-16s %4s %7d %7.2f %8.3f  %s" % (
            r["label"], r["name"][:16], r["year"], r["uptake_in_corpus"], r["uptake_per_year"],
            r["cd_index"], r["title"][:46]))
    print("\n--- means ---")
    for f in ("uptake_in_corpus", "uptake_per_year", "cd_index"):
        print("  %-18s POSITIVE=%s  NEGATIVE=%s" % (f, avg("POSITIVE", f), avg("NEGATIVE", f)))
    print("\nNOTE: positives are 2017-23 landmarks, negatives 2025-26 derivative -> raw uptake is")
    print("age-confounded; CD-index and uptake/year are the fairer contrasts.")


if __name__ == "__main__":
    main()
