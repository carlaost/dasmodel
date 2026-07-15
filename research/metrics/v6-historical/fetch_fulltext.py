#!/usr/bin/env python3
import json, subprocess, os, re
oa=json.load(open("oa_locations.json"))
corpus={p["id"]:p for p in json.load(open("corpus.json"))}
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/537.36"
got={}
for wid,loc in oa.items():
    slug=wid.split("/")[-1]
    url=loc.get("pdf")
    if not url:
        # try PMC landing -> pdf
        lp=loc.get("landing") or ""
        if "pmc/articles" in lp:
            url=lp.rstrip("/")+"/pdf/"
    if not url: continue
    pdf=f"/tmp/{slug}.pdf"
    subprocess.run(["curl","-sL","-A",UA,url,"-o",pdf,"--max-time","50"],capture_output=True)
    if not os.path.exists(pdf) or os.path.getsize(pdf)<20000: 
        got[wid]=None; continue
    # confirm it's a pdf
    with open(pdf,"rb") as f:
        if f.read(5)!=b"%PDF-": got[wid]=None; continue
    txt=f"fulltext/{slug}.txt"
    subprocess.run(["pdftotext","-q",pdf,txt],capture_output=True)
    if os.path.exists(txt) and os.path.getsize(txt)>3000:
        t=open(txt,errors="ignore").read()
        # keep intro+results region: strip refs tail
        t=re.split(r'\n\s*[Rr]eferences\s*\n',t)[0]
        got[wid]=t[:16000]
    else: got[wid]=None
    print(slug, "OK" if got.get(wid) else "fail", flush=True)
json.dump({k:v for k,v in got.items() if v},open("fulltext.json","w"))
n=sum(1 for v in got.values() if v)
print(f"\nfull text extracted for {n}/{len(oa)} OA papers")
