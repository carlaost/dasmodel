#!/usr/bin/env python3
"""
fetch_papers.py — resolve & download paper PDFs through a configurable base URL.

Generic resolver: you supply a --base-url that gets prepended to each paper's
DOI (or URL), and the script fetches the result, verifies it's a real PDF, and
saves it to data/lib/<slug>/paper.pdf.

Point --base-url at whatever *legitimate* access endpoint you have:
  * An institutional / firm proxy (EZproxy / OCLC), e.g.:
      --base-url 'https://YOURORG.idm.oclc.org/login?url=' --key url --encode
  * A plain DOI resolver (default, publisher landing — often paywalled):
      (no --base-url)  ->  https://doi.org/<DOI>
  * Any resolver that takes base+DOI directly:
      --base-url 'https://example.org/' --key doi

Nothing is hardcoded to any specific service — the base URL is entirely yours.

Examples
--------
  # dry run: show the resolve URLs it would hit, don't download
  python3 fetch_papers.py --dry-run

  # fetch everything still missing, through an institutional proxy
  python3 fetch_papers.py --base-url 'https://org.idm.oclc.org/login?url=' \
                          --key url --encode

  # just a few, force re-download, verbose
  python3 fetch_papers.py --limit 5 --force -v
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent          # research/
PAPERS_JSON = ROOT / "data" / "papers.json"
LIB_DIR = ROOT / "data" / "lib"
MANIFEST = ROOT / "data" / "fetch_manifest.json"

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def load_papers():
    if not PAPERS_JSON.exists():
        sys.exit(f"error: {PAPERS_JSON} not found — run the CSV parse step first.")
    return json.loads(PAPERS_JSON.read_text())


def resolve_url(paper, base_url, key, encode):
    """Build the URL to fetch: base_url + (doi|url), optionally url-encoded."""
    target = paper.get(key) or paper.get("url") or ""
    if key == "doi" and target and not target.lower().startswith("http") and not base_url:
        # no base + a bare DOI -> use the standard DOI resolver
        return "https://doi.org/" + target
    if encode:
        target = urllib.parse.quote(target, safe="")
    return (base_url or "") + target


def http_get(url, timeout, referer=None):
    """GET a URL following redirects; return (status, content_type, bytes, final_url)."""
    headers = {"User-Agent": UA,
               "Accept": "application/pdf,text/html;q=0.9,*/*;q=0.8"}
    if referer:
        headers["Referer"] = referer
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return (resp.status,
                resp.headers.get("Content-Type", ""),
                resp.read(),
                resp.geturl())


def is_pdf(content_type, body):
    if body[:5] == b"%PDF-":
        return True
    return "application/pdf" in (content_type or "").lower() and body[:5] == b"%PDF-"


def find_pdf_link(html, base_url):
    """Extract a PDF URL from an HTML landing page via the citation_pdf_url meta
    tag (the standard emitted by PMC and most publishers for Google Scholar)."""
    text = html.decode("utf-8", "ignore")
    m = re.search(
        r'<meta[^>]+name=["\']citation_pdf_url["\'][^>]+content=["\']([^"\']+)["\']',
        text, re.I)
    if not m:
        m = re.search(
            r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']citation_pdf_url["\']',
            text, re.I)
    if m:
        return urllib.parse.urljoin(base_url, m.group(1))
    return None


def fetch_one(paper, args):
    slug = paper["slug"]
    out_dir = LIB_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_pdf = out_dir / "paper.pdf"

    rec = {"slug": slug, "cite_key": paper.get("cite_key"),
           "doi": paper.get("doi"), "status": None, "http_status": None,
           "content_type": None, "bytes": 0, "resolve_url": None,
           "final_url": None, "note": None}

    if out_pdf.exists() and not args.force:
        rec["status"] = "skipped-exists"
        rec["bytes"] = out_pdf.stat().st_size
        return rec

    url = resolve_url(paper, args.base_url, args.key, args.encode)
    rec["resolve_url"] = url
    if args.dry_run:
        rec["status"] = "dry-run"
        return rec

    try:
        status, ctype, body, final = http_get(url, args.timeout)
        rec["http_status"] = status
        rec["content_type"] = ctype
        rec["final_url"] = final

        # landing page rather than a PDF -> try the citation_pdf_url meta tag
        if not is_pdf(ctype, body) and b"<html" in body[:2000].lower():
            link = find_pdf_link(body, final)
            if link and link != url:
                rec["note"] = f"followed citation_pdf_url -> {link}"
                status, ctype, body, final = http_get(link, args.timeout, referer=final)
                rec["http_status"] = status
                rec["content_type"] = ctype
                rec["final_url"] = final

        if is_pdf(ctype, body):
            out_pdf.write_bytes(body)
            rec["status"] = "downloaded"
            rec["bytes"] = len(body)
        else:
            rec["status"] = "no-pdf"
            rec["note"] = (rec["note"] or "") + \
                f" (got {ctype or 'unknown'}, {len(body)} bytes — likely paywall/landing page)"
    except Exception as e:  # noqa: BLE001 - report every failure, keep going
        rec["status"] = "error"
        rec["note"] = f"{type(e).__name__}: {e}"
    return rec


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base-url", default="https://sci-hub.box/",
                    help="URL prepended to each paper's DOI/URL (your proxy/resolver). "
                         "Empty = plain DOI resolver.")
    ap.add_argument("--key", choices=["doi", "url"], default="doi",
                    help="Which field to append to --base-url (default: doi).")
    ap.add_argument("--encode", action="store_true",
                    help="URL-encode the appended value (needed for '...?url=' proxies).")
    ap.add_argument("--limit", type=int, default=0, help="Only process the first N papers.")
    ap.add_argument("--only", default="",
                    help="Comma-separated cite_keys or slugs to fetch (substring match).")
    ap.add_argument("--force", action="store_true", help="Re-download even if paper.pdf exists.")
    ap.add_argument("--dry-run", action="store_true", help="Show resolve URLs; download nothing.")
    ap.add_argument("--delay", type=float, default=2.0,
                    help="Seconds to wait between requests (be polite; default 2).")
    ap.add_argument("--timeout", type=float, default=45.0, help="Per-request timeout seconds.")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    papers = load_papers()
    if args.only:
        wants = [w.strip().lower() for w in args.only.split(",") if w.strip()]
        papers = [p for p in papers
                  if any(w in (p.get("cite_key", "") + p.get("slug", "")).lower()
                         for w in wants)]
    if args.limit:
        papers = papers[:args.limit]

    print(f"→ {len(papers)} papers | base_url={args.base_url!r} key={args.key} "
          f"encode={args.encode} force={args.force} dry_run={args.dry_run}\n")

    results, counts = [], {}
    for i, p in enumerate(papers, 1):
        rec = fetch_one(p, args)
        results.append(rec)
        counts[rec["status"]] = counts.get(rec["status"], 0) + 1
        line = f"[{i}/{len(papers)}] {rec['cite_key']:<8} {rec['status']:<15} {rec['slug']}"
        if args.verbose or rec["status"] in ("error", "no-pdf", "dry-run"):
            extra = rec["resolve_url"] if rec["status"] == "dry-run" else (rec["note"] or "")
            line += f"\n            {extra}" if extra else ""
        print(line)
        # only sleep when we actually hit the network
        if not args.dry_run and rec["status"] not in ("skipped-exists",) and i < len(papers):
            time.sleep(args.delay)

    MANIFEST.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print("\n─ summary " + "─" * 40)
    for k in sorted(counts):
        print(f"  {k:<16} {counts[k]}")
    print(f"\nmanifest written: {MANIFEST}")


if __name__ == "__main__":
    main()
