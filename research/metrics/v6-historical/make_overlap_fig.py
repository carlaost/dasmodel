#!/usr/bin/env python3
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import Circle
BLUE="#2f6fb3";ORANGE="#e08a1e";GREEN="#3f8f5b";RED="#b3402f";INK="#1a1a1a";MUT="#6b7280"
fig=plt.figure(figsize=(15,6.6));fig.patch.set_facecolor("white")
gs=fig.add_gridspec(1,3,width_ratios=[1.05,1.05,1.15],wspace=0.25)

# ---------- Panel A: LLM judgement agrees with itself (recent corpus) ----------
ax=fig.add_subplot(gs[0,0]);ax.set_xlim(-2.6,2.6);ax.set_ylim(-2.5,2.6);ax.axis("off");ax.set_aspect("equal")
# panels: big overlap 0.89
ax.add_patch(Circle((-0.42,0.7),1.5,facecolor=BLUE,alpha=0.14,edgecolor=BLUE,lw=1.5))
ax.add_patch(Circle(( 0.42,0.7),1.5,facecolor=ORANGE,alpha=0.14,edgecolor=ORANGE,lw=1.5))
ax.text(-1.8,2.15,"Claude panel",color=BLUE,fontsize=9.5,weight="bold",ha="center")
ax.text( 1.8,2.15,"GPT panel",color=ORANGE,fontsize=9.5,weight="bold",ha="center")
ax.text(0,0.7,"ρ=0.89",color=INK,fontsize=11,weight="bold",ha="center")
ax.text(0,0.35,"two LLM panels\nlargely agree",color=MUT,fontsize=7.5,ha="center",va="top")
# metric circles smaller, overlapping panels ~0.5 but each other ~0.16
ax.add_patch(Circle((-0.75,-1.05),0.62,facecolor=BLUE,alpha=0.30,edgecolor=BLUE,lw=1.3))
ax.add_patch(Circle(( 0.75,-1.05),0.62,facecolor=ORANGE,alpha=0.30,edgecolor=ORANGE,lw=1.3))
ax.text(-0.75,-1.05,"Claude\nmetric",color="white",fontsize=6.5,weight="bold",ha="center",va="center")
ax.text( 0.75,-1.05,"GPT\nmetric",color="white",fontsize=6.5,weight="bold",ha="center",va="center")
ax.annotate("ρ=0.16",xy=(0,-1.05),fontsize=8,color=RED,ha="center",weight="bold")
ax.annotate("",xy=(-0.2,-1.05),xytext=(0.2,-1.05),arrowprops=dict(arrowstyle="<->",color=RED,lw=1))
ax.text(-1.5,-0.15,"↕0.54",color=BLUE,fontsize=7,ha="center")
ax.text( 1.5,-0.15,"↕0.49",color=ORANGE,fontsize=7,ha="center")
ax.set_title("A. LLM signals agree with each other\n(recent corpus, n=66)",fontsize=10,color=INK,weight="bold")

# ---------- Panel B: but metrics don't track the field (historical corpus) ----------
ax=fig.add_subplot(gs[0,1]);ax.set_xlim(-2.6,2.6);ax.set_ylim(-2.5,2.6);ax.axis("off");ax.set_aspect("equal")
# three nearly-disjoint circles (rho ~0 / negative)
ax.add_patch(Circle((-1.05,0.75),1.05,facecolor=BLUE,alpha=0.16,edgecolor=BLUE,lw=1.5))
ax.add_patch(Circle(( 1.05,0.75),1.05,facecolor=ORANGE,alpha=0.16,edgecolor=ORANGE,lw=1.5))
ax.add_patch(Circle((0.0,-1.05),1.05,facecolor=GREEN,alpha=0.16,edgecolor=GREEN,lw=1.5))
ax.text(-1.05,2.05,"Claude metric",color=BLUE,fontsize=9,weight="bold",ha="center")
ax.text( 1.05,2.05,"GPT metric",color=ORANGE,fontsize=9,weight="bold",ha="center")
ax.text(0.0,-2.25,"Field reality\n(citation disruption)",color=GREEN,fontsize=9,weight="bold",ha="center")
ax.text(0,1.15,"ρ=0.17",color=RED,fontsize=8.5,weight="bold",ha="center")            # metric-metric
ax.text(-0.95,-0.2,"ρ=−0.27",color=RED,fontsize=8.5,weight="bold",ha="center")       # claude-disr
ax.text( 0.95,-0.2,"ρ=−0.17",color=RED,fontsize=8.5,weight="bold",ha="center")       # gpt-disr
ax.set_title("B. …but neither metric tracks the field\n(historical corpus, n=27)",fontsize=10,color=INK,weight="bold")

# ---------- Panel C: exact correlation matrix ----------
ax=fig.add_subplot(gs[0,2])
labels=["Claude\npanel","GPT\npanel","Claude\nmetric","GPT\nmetric","Field\n(disrupt.)"]
M=np.array([
 [1.00, 0.89, 0.54, 0.41, np.nan],
 [0.89, 1.00, 0.41, 0.49, np.nan],
 [0.54, 0.41, 1.00, 0.16,-0.27],
 [0.41, 0.49, 0.16, 1.00,-0.17],
 [np.nan,np.nan,-0.27,-0.17,1.00]])
im=ax.imshow(M,cmap="RdBu_r",vmin=-1,vmax=1)
ax.set_xticks(range(5));ax.set_yticks(range(5))
ax.set_xticklabels(labels,fontsize=6.5);ax.set_yticklabels(labels,fontsize=6.5)
for i in range(5):
    for j in range(5):
        if not np.isnan(M[i,j]):
            ax.text(j,i,f"{M[i,j]:.2f}",ha="center",va="center",fontsize=7,
                    color="white" if abs(M[i,j])>0.6 else INK)
        else:
            ax.text(j,i,"—",ha="center",va="center",fontsize=8,color=MUT)
ax.set_title("C. Every pairwise overlap (Spearman ρ)",fontsize=10,color=INK,weight="bold",pad=8)
fig.colorbar(im,ax=ax,fraction=0.046,pad=0.04).ax.tick_params(labelsize=6)

fig.suptitle("Overlaps among the signals: LLMs agree with LLMs (panels 0.89), the two model metrics barely agree (0.16),\nand NO metric tracks real field disruption (−0.17 to −0.27). '—' = not co-measurable (recent corpus has no mature citations).",
             fontsize=10.5,color=INK,y=1.02,weight="bold")
fig.savefig("overlap_figure.png",dpi=170,bbox_inches="tight",facecolor="white")
print("wrote overlap_figure.png")
