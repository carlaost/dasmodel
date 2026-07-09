#!/usr/bin/env python3
"""Build the intra-corpus citation graph over all-papers.csv via OpenAlex, and
surface the shared landmark ancestors (the lineage backbone) + impact labels.

Outputs (to this dir):
  works.json        — per corpus paper: openalex id, year, cited_by_count, referenced_works
  graph.json        — intra-corpus edges (A cites B, both in corpus) + components
  ancestors.json    — most-shared external ancestors (candidate landmark positives/negatives)
"""
import csv, json, os, time, urllib.parse, urllib.request
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "..", "..", "..", "..", "all-papers.csv")
MAILTO = "carla@positron.vc"
API = "https://api.openalex.org/works"


def get(url):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "gro-lineage/1.0 (mailto:%s)" % MAILTO})
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as e:
            if attempt == 3:
                raise
            time.sleep(2 * (attempt + 1))


def batch(dois):
    """Fetch works for up to 50 DOIs in one filtered call."""
    out = {}
    for i in range(0, len(dois), 50):
        chunk = dois[i:i + 50]
        filt = "doi:" + "|".join(chunk)
        url = "%s?filter=%s&per-page=50&mailto=%s&select=id,doi,publication_year,cited_by_count,referenced_works,title" % (
            API, urllib.parse.quote(filt, safe="|:"), MAILTO)
        r = get(url)
        for w in r.get("results", []):
            doi = (w.get("doi") or "").replace("https://doi.org/", "").lower()
            out[doi] = w
        time.sleep(0.3)
        print("  fetched %d/%d" % (min(i + 50, len(dois)), len(dois)), flush=True)
    return out


def main():
    rows = list(csv.DictReader(open(CSV, encoding="utf-8-sig")))
    doi_rows = [(r["Cite Key"], (r.get("DOI") or "").strip().lower(), r.get("Year", ""),
                 int(r["Citation Count"]) if r.get("Citation Count", "").strip().isdigit() else 0,
                 r.get("Title", "")) for r in rows if (r.get("DOI") or "").strip()]
    dois = [d for _, d, *_ in doi_rows]
    print("resolving %d DOIs via OpenAlex..." % len(dois), flush=True)
    works = batch(dois)
    print("resolved %d/%d" % (len(works), len(dois)), flush=True)

    # map openalex id -> corpus cite key
    id2key = {}
    meta = {}
    for key, doi, year, cc, title in doi_rows:
        w = works.get(doi)
        if not w:
            continue
        oid = w["id"]
        id2key[oid] = key
        meta[key] = {"oid": oid, "doi": doi, "year": w.get("publication_year") or year,
                     "oa_cited_by": w.get("cited_by_count", 0), "csv_cited_by": cc,
                     "n_refs": len(w.get("referenced_works", [])), "title": title[:120]}
    corpus_ids = set(id2key)

    # intra-corpus edges + external ancestor tally
    edges = []
    ancestor_count = Counter()
    for key, doi, *_ in doi_rows:
        w = works.get(doi)
        if not w:
            continue
        for ref in w.get("referenced_works", []):
            if ref in corpus_ids:
                edges.append([key, id2key[ref]])  # key CITES id2key[ref]
            else:
                ancestor_count[ref] += 1

    # connected components (undirected) over intra edges
    adj = defaultdict(set)
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    seen, comps = set(), []
    for node in adj:
        if node in seen:
            continue
        stack, comp = [node], []
        while stack:
            n = stack.pop()
            if n in seen:
                continue
            seen.add(n); comp.append(n)
            stack.extend(adj[n] - seen)
        comps.append(sorted(comp))
    comps.sort(key=len, reverse=True)

    # persist raw referenced_works per corpus paper (for disruption/CD-index) + id->key map
    refs_raw = {}
    for key, doi, *_ in doi_rows:
        w = works.get(doi)
        if w:
            refs_raw[key] = w.get("referenced_works", [])
    json.dump({"id2key": id2key, "refs_raw": refs_raw},
              open(os.path.join(HERE, "refs_raw.json"), "w"), indent=2)

    json.dump({"n_corpus": len(doi_rows), "n_resolved": len(works), "meta": meta},
              open(os.path.join(HERE, "works.json"), "w"), indent=2)
    json.dump({"n_intra_edges": len(edges), "edges": edges,
               "n_components": len(comps), "component_sizes": [len(c) for c in comps],
               "largest_components": comps[:5]},
              open(os.path.join(HERE, "graph.json"), "w"), indent=2)

    # resolve top ancestors to titles (candidate landmark positives/negatives)
    top = [a for a, _ in ancestor_count.most_common(60)]
    anc_meta = {}
    for i in range(0, len(top), 50):
        chunk = top[i:i + 50]
        filt = "openalex_id:" + "|".join(a.split("/")[-1] for a in chunk)
        url = "%s?filter=%s&per-page=50&mailto=%s&select=id,doi,publication_year,cited_by_count,title" % (
            API, urllib.parse.quote(filt, safe="|:"), MAILTO)
        r = get(url)
        for w in r.get("results", []):
            anc_meta[w["id"]] = {"title": w.get("title", "")[:140], "year": w.get("publication_year"),
                                 "cited_by": w.get("cited_by_count", 0), "doi": w.get("doi"),
                                 "shared_by_n_corpus_papers": ancestor_count[w["id"]]}
        time.sleep(0.3)
    ancestors = sorted(anc_meta.values(), key=lambda x: x["shared_by_n_corpus_papers"], reverse=True)
    json.dump({"top_shared_ancestors": ancestors},
              open(os.path.join(HERE, "ancestors.json"), "w"), indent=2)

    print("\n=== SUMMARY ===")
    print("corpus papers with DOI:", len(doi_rows), "| resolved on OpenAlex:", len(works))
    print("intra-corpus citation edges (A cites B, both in corpus):", len(edges))
    print("connected components:", len(comps), "| largest sizes:", [len(c) for c in comps[:6]])
    print("\nTop shared landmark ancestors (lineage backbone):")
    for a in ancestors[:15]:
        print("  [%s] cited_by=%d shared_by=%d  %s" % (a["year"], a["cited_by"], a["shared_by_n_corpus_papers"], a["title"]))


if __name__ == "__main__":
    main()
