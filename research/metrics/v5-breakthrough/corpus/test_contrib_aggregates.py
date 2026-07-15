#!/usr/bin/env python3
"""Test count-INDEPENDENT contribution aggregates vs the grounded panel, held-out.
Carla's point: a paper with 1 huge contribution should score like 1 huge + 10 small
(the small ones must NOT drag it down). wmean violates this; peak/noisy-or don't.
"""
import glob, json, os, yaml
from apply_formula import spearman, load_split
ARALIB="/Users/carlaostmann/code/dasmodel/research/ara-library"
NOVW={"new_paradigm":1.0,"new_method":0.8,"new_finding":0.7,"refutation":0.6,
      "synthesis":0.35,"incremental_improvement":0.15,"replication":0.1}
def contribs(gro):
    fp=os.path.join(gro,"contributions.yaml")
    if not os.path.exists(fp): return []
    doc=yaml.safe_load(open(fp)) or {}
    out=[]
    for c in (doc.get("contributions") or []):
        cat=(c.get("compiler_assessed_type") or {})
        w=NOVW.get(cat.get("primary"),0.10)
        conf=cat.get("confidence"); conf=float(conf) if isinstance(conf,(int,float)) else 0.3
        if not (c.get("realized_in") or []): w=0.0   # anti-puffery
        out.append((w,conf))
    return out
def aggs(cs):
    if not cs: return {}
    wc=sorted((w*conf for w,conf in cs),reverse=True)
    w=sorted((w for w,_ in cs),reverse=True)
    prod=1.0
    for x in wc: prod*= (1-x)
    return {
      "peak_wconf": wc[0],
      "peak_w": w[0],
      "top2_mean": sum(wc[:2])/min(2,len(wc)),
      "top3_mean": sum(wc[:3])/min(3,len(wc)),
      "noisy_or": 1-prod,
      "wmean": sum(wc)/len(wc),                       # the current (bad) one
      "sum_capped": min(sum(wc),3.0)/3.0,
      "n_strong": sum(1 for x in w if x>=0.6)/1.0,    # count of genuinely-novel contributions
    }
rows={}
for gro in glob.glob(f"{ARALIB}/*/gro"):
    slug=os.path.basename(os.path.dirname(gro))
    rows[slug]=aggs(contribs(gro))
exp=json.load(open("expert_scores.json")); test=load_split("test")
def rho(key,slugs):
    xs=[];ys=[]
    for s in slugs:
        if s in exp and rows.get(s,{}).get(key) is not None:
            xs.append(rows[s][key]); ys.append(exp[s])
    return spearman(xs,ys),len(xs)
alls=list(rows); tests=[s for s in rows if s in test]
print("%-14s %12s %12s"%("aggregate","all66","TEST(n=26)"))
for k in ["peak_wconf","peak_w","top2_mean","top3_mean","noisy_or","sum_capped","n_strong","wmean"]:
    a,na=rho(k,alls); t,nt=rho(k,tests)
    print("%-14s %6.3f(%2d) %6.3f(%2d)"%(k,a,na,t,nt))
json.dump(rows,open("contrib_aggregates.json","w"),indent=1)
