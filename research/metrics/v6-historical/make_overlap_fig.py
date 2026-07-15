#!/usr/bin/env python3
"""Faithful overlap figure: a correlation NETWORK (edge width strictly ∝ |ρ|, colour = sign)
+ the exact Spearman matrix. No hand-drawn Venn geometry — equal ρ now looks equal."""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
BLUE="#2f6fb3";ORANGE="#e08a1e";GREEN="#3f8f5b";POS="#2f6fb3";NEG="#b3402f";INK="#1a1a1a";MUT="#6b7280"
fig=plt.figure(figsize=(15,6.8));fig.patch.set_facecolor("white")
gs=fig.add_gridspec(1,2,width_ratios=[1.25,1],wspace=0.15)

# ---- correlation network ----
ax=fig.add_subplot(gs[0,0]);ax.set_xlim(0,10);ax.set_ylim(0,10);ax.axis("off")
nodes={
 "Claude panel":(2.3,8.4,BLUE),
 "GPT panel":(6.0,8.4,ORANGE),
 "Claude metric":(2.0,4.6,BLUE),
 "GPT metric":(6.3,4.6,ORANGE),
 "Field reality\n(citation disruption)":(4.15,1.2,GREEN),
}
edges=[  # (a,b,rho,label_t)
 ("Claude panel","GPT panel",0.89,0.5),
 ("Claude panel","Claude metric",0.54,0.5),
 ("GPT panel","GPT metric",0.49,0.5),
 ("Claude panel","GPT metric",0.41,0.30),
 ("GPT panel","Claude metric",0.41,0.70),
 ("Claude metric","GPT metric",0.16,0.5),
 ("Claude metric","Field reality\n(citation disruption)",-0.27,0.5),
 ("GPT metric","Field reality\n(citation disruption)",-0.17,0.5),
]
def mid(a,b,t=0.5): return (nodes[a][0]+(nodes[b][0]-nodes[a][0])*t, nodes[a][1]+(nodes[b][1]-nodes[a][1])*t)
for a,b,r,lt in edges:
    x1,y1,_=nodes[a]; x2,y2,_=nodes[b]
    col=POS if r>=0 else NEG
    ax.plot([x1,x2],[y1,y2],color=col,lw=max(0.6,abs(r)*11),alpha=0.55,zorder=1,solid_capstyle="round")
    mx,my=mid(a,b, lt)
    ax.text(mx,my,f"{r:+.2f}",fontsize=9,color=col,weight="bold",ha="center",va="center",
            bbox=dict(boxstyle="round,pad=0.12",fc="white",ec="none",alpha=0.85),zorder=3)
for name,(x,y,c) in nodes.items():
    ax.scatter([x],[y],s=2400,c=c,alpha=0.22,edgecolors=c,linewidths=1.6,zorder=2)
    ax.text(x,y,name,fontsize=8.2,color=INK,weight="bold",ha="center",va="center",zorder=4)
ax.text(5,9.6,"Correlation network — edge width ∝ |ρ|, blue=+ red=−",fontsize=10.5,color=INK,weight="bold",ha="center")
ax.text(5,0.15,"panel↔field edges omitted: not co-measurable (recent papers have no mature citations)",fontsize=7.3,color=MUT,ha="center")

# ---- exact matrix ----
ax=fig.add_subplot(gs[0,1])
labels=["Claude\npanel","GPT\npanel","Claude\nmetric","GPT\nmetric","Field\n(disrupt.)"]
M=np.array([[1,0.89,0.54,0.41,np.nan],[0.89,1,0.41,0.49,np.nan],
            [0.54,0.41,1,0.16,-0.27],[0.41,0.49,0.16,1,-0.17],[np.nan,np.nan,-0.27,-0.17,1]])
im=ax.imshow(M,cmap="RdBu_r",vmin=-1,vmax=1)
ax.set_xticks(range(5));ax.set_yticks(range(5));ax.set_xticklabels(labels,fontsize=6.8);ax.set_yticklabels(labels,fontsize=6.8)
for i in range(5):
    for j in range(5):
        v=M[i,j]
        ax.text(j,i,("—" if np.isnan(v) else f"{v:.2f}"),ha="center",va="center",fontsize=7.5,
                color=(MUT if np.isnan(v) else ("white" if abs(v)>0.6 else INK)))
ax.set_title("Exact Spearman ρ (both corpora)",fontsize=10.5,color=INK,weight="bold",pad=8)
fig.colorbar(im,ax=ax,fraction=0.046,pad=0.04).ax.tick_params(labelsize=6)

fig.suptitle("LLM panels agree with each other (0.89); the two model metrics barely agree (0.16); neither tracks field disruption (−0.17, −0.27).\n"
             "Recent corpus (panels) and historical corpus (field) share only the metric nodes — hence the omitted/‘—’ panel↔field pairs.",
             fontsize=10,color=INK,y=1.03,weight="bold")
fig.savefig("overlap_figure.png",dpi=170,bbox_inches="tight",facecolor="white")
print("wrote overlap_figure.png")
