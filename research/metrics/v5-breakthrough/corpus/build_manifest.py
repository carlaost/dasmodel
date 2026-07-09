#!/usr/bin/env python3
"""Build the expert-judgement manifest: one record per recent GRO-extended paper with the
content an expert needs to rate breakthrough-ness (title, year, venue, abstract, claim summary)
plus the metric's significance score (kept SEPARATE so the judge is blind to it — it is only
here so the downstream correlation step can join without a second pass).

Reads PAPER.md YAML frontmatter from each ara-library paper that scored in corpus_scored.json.
Writes corpus_manifest.json.
"""
import json
import os

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ARALIB = "/Users/carlaostmann/code/dasmodel/research/ara-library"


def frontmatter(paper_md):
    if not os.path.exists(paper_md):
        return {}
    with open(paper_md) as f:
        text = f.read()
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(text[3:end]) or {}
    except Exception:
        return {}


def main():
    scored = {r["slug"]: r for r in json.load(open(os.path.join(HERE, "corpus_scored.json")))}
    out = []
    for slug, row in scored.items():
        fm = frontmatter(os.path.join(ARALIB, slug, "PAPER.md"))
        claims = fm.get("claims_summary") or []
        out.append({
            "slug": slug,
            "title": fm.get("title", slug),
            "year": fm.get("year"),
            "venue": fm.get("venue", ""),
            "domain": fm.get("domain", ""),
            "abstract": fm.get("abstract", ""),
            "claims_summary": claims[:12],
            "_significance": row["significance"],   # blind field, prefixed; not shown to judges
        })
    out.sort(key=lambda x: x["slug"])
    outp = os.path.join(HERE, "corpus_manifest.json")
    with open(outp, "w") as f:
        json.dump(out, f, indent=2)
    n_abs = sum(1 for r in out if r["abstract"])
    print(f"wrote {len(out)} records -> {outp}  ({n_abs} with abstract, "
          f"{sum(1 for r in out if r['claims_summary'])} with claims)")


if __name__ == "__main__":
    main()
