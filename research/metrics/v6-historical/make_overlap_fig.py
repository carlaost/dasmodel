#!/usr/bin/env python3
"""Historical corpus: do LLM JUDGES / METRICS (by model + converged) predict the FIELD?
Two field targets — disruption (breakthrough) and citations (attention). Grouped bars + exact 6x6."""
import json, math, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
def sp(x,y):
    def rk(v):
        o=sorted(range(len(v)),key=lambda i:v[i]);r=[0]*len(v);i=0
        while i<len(v):
            j=i
            while j+1<len(v) and v[o[j+1]]==v[o[i]]:j+=1
            a=(i+j)/2+1
            for k in range(i,j+1):r[o[k]]=a
            i=j+1
        return r
    rx,ry=rk(x),rk(y);n=len(x);mx=sum(rx)/n;my=sum(ry)/n
    c=sum((rx[i]-mx)*(ry[i]-my) for i in range(n));sx=math.sqrt(sum((v-mx)**2 for v in rx));sy=math.sqrt(sum((v-my)**2 for v in ry))
    return c/(sx*sy) if sx and sy else 0
jc=json.load(open('judge_ft_claude.json')); jg=json.load(open('judge_ft_gpt.json'))
mc={k:v['metric'] for k,v in json.load(open('metric_pubtime_ft_claude.json')).items()}
mg={k:v.get('metric') for k,v in json.load(open('metric_pubtime_ft_gpt.json')).items()}
disr=json.load(open('disruption.json')); id2s={p['id']:p['id'].split('/')[-1] for p in json.load(open('corpus.json'))}
corpus={p['id'].split('/')[-1]:p for p in json.load(open('corpus.json'))}
mdi={id2s[k]:(v.get('mDI') if v.get('n_citers',0)>=10 else None) for k,v in disr.items()}
K=[s for s in jc if jg.get(s) is not None and mc.get(s) is not None and mg.get(s) is not None and mdi.get(s) is not None]
D=[mdi[s] for s in K]; CIT=[corpus[s]['cited_by_count'] for s in K]
pred={"Claude\njudge":[jc[s] for s in K],"GPT\njudge":[jg[s] for s in K],
 "Converged\njudge":[(jc[s]+jg[s])/2 for s in K],"Consensus\nmetric":[(mc[s]+mg[s])/2 for s in K]}
BLUE="#2f6fb3";ORANGE="#e08a1e";INK="#1a1a1a";MUT="#6b7280";GRID="#e6e8eb"
fig=plt.figure(figsize=(15,6.4));fig.patch.set_facecolor("white")
gs=fig.add_gridspec(1,2,width_ratios=[1.1,1],wspace=0.22)

# ---- grouped bars: predictor vs {disruption, citations} ----
ax=fig.add_subplot(gs[0,0])
names=list(pred); x=np.arange(len(names)); w=0.36
disr_r=[sp(pred[n],D) for n in names]; cit_r=[sp(pred[n],CIT) for n in names]
ax.axhline(0,color="#999",lw=0.8)
b1=ax.bar(x-w/2,disr_r,w,color="#7a1f2b",label="vs field DISRUPTION (breakthrough)",zorder=3)
b2=ax.bar(x+w/2,cit_r,w,color="#2f6fb3",label="vs CITATIONS (attention)",zorder=3)
for xi,v in zip(x-w/2,disr_r): ax.text(xi,v+(0.02 if v>=0 else -0.05),f"{v:+.2f}",ha="center",fontsize=8,color=INK)
for xi,v in zip(x+w/2,cit_r): ax.text(xi,v+0.02,f"{v:+.2f}",ha="center",fontsize=8,color=INK)
ax.set_xticks(x);ax.set_xticklabels(names,fontsize=8.5);ax.set_ylim(-0.45,0.72)
ax.set_ylabel("Spearman ρ vs field (n=%d)"%len(K),fontsize=9,color=INK)
ax.set_title("LLMs predict ATTENTION, not BREAKTHROUGH\nboth judges track citations (~0.5); none track disruption (~0)",fontsize=10.5,color=INK,weight="bold")
for s in ("top","right"): ax.spines[s].set_visible(False)
ax.grid(True,axis="y",color=GRID,lw=0.8,zorder=0);ax.set_axisbelow(True);ax.tick_params(labelsize=8,colors=MUT)
ax.legend(fontsize=7.8,loc="lower right",frameon=False)

# ---- exact 6x6 historical matrix ----
ax=fig.add_subplot(gs[0,1])
cols={"Claude judge":[jc[s] for s in K],"GPT judge":[jg[s] for s in K],"Claude metric":[mc[s] for s in K],
      "GPT metric":[mg[s] for s in K],"Disruption\n(breakthrough)":D,"Citations\n(attention)":CIT}
nm=list(cols); M=np.array([[sp(cols[a],cols[b]) for b in nm] for a in nm])
im=ax.imshow(M,cmap="RdBu_r",vmin=-1,vmax=1)
short=["Claude\njudge","GPT\njudge","Claude\nmetric","GPT\nmetric","Disrupt.","Cites"]
ax.set_xticks(range(6));ax.set_yticks(range(6));ax.set_xticklabels(short,fontsize=6.3);ax.set_yticklabels(short,fontsize=6.3)
for i in range(6):
    for j in range(6):
        ax.text(j,i,f"{M[i,j]:.2f}",ha="center",va="center",fontsize=6.8,color=("white" if abs(M[i,j])>0.6 else INK))
ax.set_title("Exact Spearman ρ — historical corpus (all co-measurable, n=%d)"%len(K),fontsize=9.5,color=INK,weight="bold",pad=8)
fig.colorbar(im,ax=ax,fraction=0.046,pad=0.04).ax.tick_params(labelsize=6)

fig.suptitle("LLM judges agree with each other (0.70) and predict what gets CITED (0.46–0.53) — but neither judges nor metrics predict what DISRUPTED the field (≈0).\n"
             "(recent-corpus judge↔judge agreement was 0.89, v5; disruption and citations are near-orthogonal — attention ≠ breakthrough.)",
             fontsize=9.6,color=INK,y=1.03,weight="bold")
fig.savefig("overlap_figure.png",dpi=170,bbox_inches="tight",facecolor="white")
print("wrote overlap_figure.png")
