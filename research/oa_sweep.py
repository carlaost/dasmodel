#!/usr/bin/env python3
"""Parallel OA sweep over all missing papers using oa_fetch.resolve/download."""
import os, json, concurrent.futures as cf
import oa_fetch as of

HERE = os.path.dirname(os.path.abspath(__file__))
existing = set(os.listdir(os.path.join(HERE, "ara-library")))
papers = json.load(open(os.path.join(HERE, "data", "papers_all.json")))
missing = [p for p in papers if p["slug"] not in existing]


def work(p):
    slug = p["slug"]
    dest = os.path.join(of.LIB, slug, "paper.pdf")
    if os.path.exists(dest) and os.path.getsize(dest) > 20000:
        return (slug, "have")
    src, url, m = of.resolve(slug)
    if not src:
        return (slug, "miss")
    ok, info = of.download(url, dest)
    if ok:
        url_show = url[0] if isinstance(url, list) else url
        with open(os.path.join(of.LIB, slug, "sources.yaml"), "w") as f:
            f.write("paper:\n  slug: %s\n  doi: %s\n  title: %r\n" % (slug, m.get("doi"), m.get("title")))
            f.write("pdf:\n  oa: true\n  downloaded: true\n  path: paper.pdf\n  url: %s\n  source: %s\n" % (url_show, src))
            f.write("code: []\ndata: []\nclinical_trials: []\n")
        return (slug, "got")
    return (slug, "fail")


done = 0
counts = {}
with cf.ThreadPoolExecutor(max_workers=12) as ex:
    for slug, status in ex.map(work, missing):
        done += 1
        counts[status] = counts.get(status, 0) + 1
        if status in ("got", "have"):
            print("%-6s %s" % (status.upper(), slug), flush=True)
        if done % 50 == 0:
            print("... %d/%d  %s" % (done, len(missing), counts), flush=True)
print("DONE", counts, flush=True)
