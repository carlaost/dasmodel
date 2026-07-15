#!/usr/bin/env python3
"""GPT (codex/gpt-5.5) types contributions from FULL TEXT — dual-model half B."""
import json, os, subprocess, glob
HERE=os.path.dirname(os.path.abspath(__file__))
SCHEMA=os.path.join(HERE,"typing_schema.json")  # reuse the one from corpus/ if present else write
open(SCHEMA,"w").write(json.dumps({"type":"object","additionalProperties":False,"required":["contributions"],
 "properties":{"contributions":{"type":"array","items":{"type":"object","additionalProperties":False,
   "required":["type","confidence"],
   "properties":{"type":{"type":"string","enum":["new_paradigm","new_method","new_finding","refutation","synthesis","incremental_improvement","replication"]},
                 "confidence":{"type":"number","minimum":0,"maximum":1}}}}}}))
NOVW={"new_paradigm":1.0,"new_method":0.8,"new_finding":0.7,"refutation":0.6,"synthesis":0.35,"incremental_improvement":0.15,"replication":0.1}
PROMPT="""List each DISTINCT scientific contribution this paper makes and classify each with a novelty TYPE from this closed taxonomy plus confidence [0,1]:
new_paradigm > new_method > new_finding > refutation > synthesis > incremental_improvement > replication.
Judge ONLY from the text at its publication time — NO hindsight about later impact; do not reward quantity. Output only the JSON.

PAPER FULL TEXT:
"""
out=json.load(open("metric_pubtime_ft_gpt.json")) if os.path.exists("metric_pubtime_ft_gpt.json") else {}
files=sorted(glob.glob("fulltext/*.txt"))
for i,fp in enumerate(files):
    slug=os.path.splitext(os.path.basename(fp))[0]
    if slug in out: continue
    txt=open(fp,errors="ignore").read()[:14000]
    try:
        r=subprocess.run(["codex","exec","-s","read-only","--skip-git-repo-check","--ephemeral","--output-schema",SCHEMA,"-"],
                         input=PROMPT+txt,capture_output=True,text=True,timeout=150)
        obj=None
        for line in reversed(r.stdout.strip().splitlines()):
            line=line.strip()
            if line.startswith("{") and "contributions" in line: obj=json.loads(line); break
        cs=(obj or {}).get("contributions") or []
        if cs:
            wc=[NOVW.get(c.get("type"),0.1)*float(c.get("confidence",0.3)) for c in cs]
            peak=max(wc); cw=sum(wc)/ (sum(float(c.get("confidence",0.3)) for c in cs) or 1)
            out[slug]={"slug":slug,"metric":round(max(peak,cw),4),"peak":round(peak,4),"cwmean":round(cw,4),"n":len(cs)}
        else: out[slug]={"slug":slug,"metric":None,"n":0}
        print(i+1,slug,"->",out[slug].get("metric"),flush=True)
    except Exception as e:
        out[slug]={"slug":slug,"metric":None,"n":0}; print(i+1,slug,"ERR",str(e)[:40],flush=True)
    json.dump(out,open("metric_pubtime_ft_gpt.json","w"),indent=1)
print("done:",sum(1 for v in out.values() if v.get("metric") is not None),"typed")
