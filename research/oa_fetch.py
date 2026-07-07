#!/usr/bin/env python3
"""
oa_fetch.py — resolve a legitimate Open-Access PDF for a paper via Unpaywall
and Europe PMC, download it into data/lib/<slug>/paper.pdf, and write sources.yaml.

Only uses legitimate OA endpoints (Unpaywall, Europe PMC, publisher OA links).
Never touches piracy mirrors.

Usage:
  python3 oa_fetch.py <slug> [<slug> ...]
  python3 oa_fetch.py --all-missing            # every paper without an ARA
  python3 oa_fetch.py --check <slug> ...       # resolve only, don't download
"""
import json, os, sys, time, urllib.parse, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, "data", "lib")
EMAIL = "carla@positron.vc"
UA = "Mozilla/5.0 (research OA fetcher; mailto:%s)" % EMAIL


BROWSER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/pdf,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def _get(url, timeout=30, accept=None, browser=False):
    headers = dict(BROWSER_HEADERS) if browser else {"User-Agent": UA}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(req, timeout=timeout)


def unpaywall_pdf(doi):
    if not doi:
        return None
    url = "https://api.unpaywall.org/v2/%s?email=%s" % (urllib.parse.quote(doi), EMAIL)
    try:
        with _get(url, accept="application/json") as r:
            d = json.load(r)
    except Exception:
        return None
    loc = d.get("best_oa_location") or {}
    pdf = loc.get("url_for_pdf")
    if pdf:
        return ("unpaywall", pdf)
    # try any oa location
    for loc in d.get("oa_locations", []) or []:
        if loc.get("url_for_pdf"):
            return ("unpaywall", loc["url_for_pdf"])
    return None


def epmc_pdf(doi, title):
    q = ('DOI:"%s"' % doi) if doi else ('TITLE:"%s"' % title)
    url = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query="
           + urllib.parse.quote(q) + "&format=json&pageSize=1")
    try:
        with _get(url, accept="application/json") as r:
            d = json.load(r)
    except Exception:
        return None
    results = d.get("resultList", {}).get("result", [])
    if not results:
        return None
    res = results[0]
    pmcid = res.get("pmcid")
    if pmcid and res.get("isOpenAccess") == "Y":
        # Europe PMC PDF endpoint requires source=PMC literally, plus NCBI direct fallback
        return ("pmc", [
            "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC/%s/fullTextPDF" % pmcid,
            "https://pmc.ncbi.nlm.nih.gov/articles/%s/pdf/" % pmcid,
        ])
    return None


def _curl(url, dest):
    import subprocess
    try:
        subprocess.run(
            ["curl", "-sL", "--max-time", "25", "--connect-timeout", "10",
             "-A", BROWSER_HEADERS["User-Agent"],
             "-H", "Accept: application/pdf,*/*", "-o", dest, url],
            check=False, timeout=30)
    except Exception:
        return False
    if os.path.exists(dest) and os.path.getsize(dest) > 20000:
        with open(dest, "rb") as f:
            if f.read(5) == b"%PDF-":
                return True
    return False


def download(urls, dest):
    if isinstance(urls, str):
        urls = [urls]
    last = "no url"
    for url in urls:
        for browser in (True, False):
            try:
                with _get(url, timeout=30, browser=browser) as r:
                    data = r.read()
            except Exception as e:
                last = str(e); continue
            if data[:5] == b"%PDF-":
                with open(dest, "wb") as f:
                    f.write(data)
                return True, len(data)
            last = "not a PDF (got %r)" % data[:20]
        # curl fallback (different TLS stack, follows redirects)
        if _curl(url, dest):
            return True, os.path.getsize(dest)
    if os.path.exists(dest) and os.path.getsize(dest) < 20000:
        os.remove(dest)
    return False, last


def resolve(slug):
    mpath = os.path.join(LIB, slug, "metadata.json")
    if not os.path.exists(mpath):
        return None
    m = json.load(open(mpath))
    doi, title = m.get("doi"), m.get("title")
    for fn in (lambda: unpaywall_pdf(doi), lambda: epmc_pdf(doi, title)):
        got = fn()
        if got:
            return got + (m,)
    return (None, None, m)


def main():
    args = sys.argv[1:]
    check_only = False
    if args and args[0] == "--check":
        check_only = True
        args = args[1:]
    if args and args[0] == "--all-missing":
        existing = set(os.listdir(os.path.join(HERE, "ara-library")))
        papers = json.load(open(os.path.join(HERE, "data", "papers_all.json")))
        args = [p["slug"] for p in papers if p["slug"] not in existing]

    results = {}
    for slug in args:
        src, url, m = resolve(slug)
        if not src:
            print("MISS   %s" % slug)
            results[slug] = {"oa": False}
            continue
        if check_only:
            print("OA     %-8s %s  %s" % (src, slug, url))
            results[slug] = {"oa": True, "source": src, "url": url}
            continue
        dest = os.path.join(LIB, slug, "paper.pdf")
        if os.path.exists(dest) and os.path.getsize(dest) > 20000:
            print("HAVE   %-8s %s" % (src, slug))
            results[slug] = {"oa": True, "source": src, "have": True}
            continue
        url_show = url[0] if isinstance(url, list) else url
        ok, info = download(url, dest)
        if ok:
            print("GOT    %-8s %s  (%s bytes)" % (src, slug, info))
            # write sources.yaml
            with open(os.path.join(LIB, slug, "sources.yaml"), "w") as f:
                f.write("paper:\n  slug: %s\n  doi: %s\n  title: %r\n" % (slug, m.get("doi"), m.get("title")))
                f.write("pdf:\n  oa: true\n  downloaded: true\n  path: paper.pdf\n  url: %s\n  source: %s\n" % (url_show, src))
                f.write("code: []\ndata: []\nclinical_trials: []\n")
            results[slug] = {"oa": True, "source": src, "url": url, "bytes": info}
        else:
            print("FAIL   %-8s %s  (%s)" % (src, slug, info))
            results[slug] = {"oa": True, "source": src, "url": url, "error": info}
        time.sleep(0.5)

    outp = os.path.join(HERE, "data", "oa_fetch_result.json")
    prev = {}
    if os.path.exists(outp):
        try: prev = json.load(open(outp))
        except: pass
    prev.update(results)
    json.dump(prev, open(outp, "w"), indent=2)
    n_oa = sum(1 for v in results.values() if v.get("oa"))
    print("\n%d/%d have OA%s" % (n_oa, len(results), "" if check_only else " downloaded"))


if __name__ == "__main__":
    main()
