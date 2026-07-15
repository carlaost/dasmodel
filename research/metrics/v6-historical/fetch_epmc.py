#!/usr/bin/env python3
import json, subprocess, re, time
def get(u):
    try: return subprocess.run(["curl","-sL","--max-time","40",u],capture_output=True,text=True).stdout
    except: return ""
corpus=json.load(open("corpus.json"))
ft={}
for p in corpus:
    doi=(p.get("doi") or "").replace("https://doi.org/","")
    if not doi: continue
    r=get(f'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%22{doi}%22&format=json&resultType=core')
    try: res=json.loads(r).get("resultList",{}).get("result",[])
    except: res=[]
    if not res: continue
    pmcid=res[0].get("pmcid")
    if not pmcid: continue
    xml=get(f'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC/{pmcid}/fullTextXML')
    if not xml or len(xml)<3000: continue
    # crude XML -> text: keep body, drop tags/refs
    body=re.split(r'<ref-list',xml)[0]
    txt=re.sub(r'<[^>]+>',' ',body)
    txt=re.sub(r'\s+',' ',txt)
    if len(txt)>3000:
        ft[p["id"]]=txt[:16000]
        print(p["id"].split("/")[-1],pmcid,len(txt),flush=True)
    time.sleep(0.2)
json.dump(ft,open("fulltext_epmc.json","w"))
print(f"\nEurope PMC full text: {len(ft)}/{len(corpus)} papers")
