#!/usr/bin/env python3
import json, os, re, subprocess, time
EMAIL="carla@positron.vc"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16 Safari/605.1.15"
corpus={p['id'].split('/')[-1]:p for p in json.load(open('corpus.json'))}
have=set(os.path.splitext(f)[0] for f in os.listdir('fulltext') if f.endswith('.txt'))
# user's 10 manually-verified direct links
VERIFIED={
 "W2153828345":"https://jamanetwork.com/journals/jamaneurology/articlepdf/10.1001/archneur.65.11.1509",
 "W1970353438":None,"W2162906229":None,"W2088617390":None,  # JAMA — try unpaywall/landing
}
def curl(url,out):
    subprocess.run(["curl","-sL","-A",UA,"-e","https://scholar.google.com/",url,"-o",out,"--max-time","60"],capture_output=True)
    return os.path.exists(out) and os.path.getsize(out)>15000
def extract(pdf,slug):
    with open(pdf,'rb') as f:
        if f.read(5)!=b'%PDF-': return False
    txt=f"fulltext/{slug}.txt"
    subprocess.run(["pdftotext","-q",pdf,txt],capture_output=True)
    if os.path.exists(txt) and os.path.getsize(txt)>3000:
        t=re.split(r'\n\s*[Rr]eferences\s*\n',open(txt,errors='ignore').read())[0]
        open(txt,'w').write(t[:16000]); return True
    return False
def unpaywall(doi):
    try:
        r=subprocess.run(["curl","-sL","--max-time","30",f"https://api.unpaywall.org/v2/{doi}?email={EMAIL}"],capture_output=True,text=True).stdout
        d=json.loads(r); loc=d.get("best_oa_location") or {}
        return d.get("is_oa"), loc.get("url_for_pdf"), loc.get("url")
    except: return None,None,None
manifest=[]
for slug,p in corpus.items():
    if slug in have: manifest.append((slug,"","have","","")); continue
    doi=(p.get('doi') or '').replace('https://doi.org/','')
    is_oa=pdf=land=None
    if doi: is_oa,pdf,land=unpaywall(doi)
    urls=[u for u in [VERIFIED.get(slug),pdf] if u]
    ok=False
    for u in urls:
        if curl(u,f"/tmp/{slug}.pdf") and extract(f"/tmp/{slug}.pdf",slug): ok=True; break
    manifest.append((slug,doi,"OK" if ok else ("oa_no_pdf" if is_oa else "closed"),pdf or "",land or ""))
    print(slug, "OK" if ok else f"miss(is_oa={is_oa})", flush=True)
    time.sleep(0.2)
import csv
with open("oa_manifest.tsv","w") as f:
    w=csv.writer(f,delimiter="\t"); w.writerow(["slug","doi","status","pdf_url","landing"]); w.writerows(manifest)
have=set(os.path.splitext(f)[0] for f in os.listdir('fulltext') if f.endswith('.txt'))
print(f"\nfull text now: {len(have)}/72")
