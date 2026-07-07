# Problem

## Observations

1. Brain connectomes (white-matter tractography networks) encode pathological variation on ROIs
   relevant to Alzheimer's Disease (AD), motivating the use of Graph Neural Networks (GNNs) on
   brain graphs for AD classification (§1, Introduction).
2. Conventional convolution-based GNNs (e.g. GCN [12], GAT [22]) and diffusion-kernel GNNs (e.g.
   GraphHeat [26], GDC [7], ADC [27], LSAP [18]) rely on a **homophily assumption**: node features
   locally connected by edges are assumed to behave similarly. This means they "ineffectively
   aggregate information from distant neighborhoods" and "overlook the relationships between nodes
   far apart" (§1–2).
3. Graph Transformers (e.g. NodeFormer [24], DIFFormer [23], SGFormer [25]) use global attention
   to capture far-distance influence, but "often disregard sufficient expressive power of the
   central nodes, lacking interpretation of the result" (§1).
4. The problem is compounded when classification uses **multiple biomarker modalities** as nodal
   features (cortical thickness, FDG-PET, β-Amyloid PET): "the interaction among multiple
   biomarkers and their diverse characteristics introduce heterogeneity, further complicating the
   analysis" (§1).
5. Empirically (Table 1), plain convolutional GNNs (GCN 0.861–0.888 accuracy) and single-mechanism
   diffusion GNNs (GraphHeat/GDC 0.842–0.893) trail graph-transformer baselines (DIFFormer/SGFormer
   0.930–0.959) across all four modality combinations, consistent with observation 2–3.

## Gaps

- **G1 — Local/global trade-off**: no existing single mechanism jointly (a) adaptively sizes each
  node's effective receptive field per modality (local, short-range) *and* (b) lets that node
  attend to arbitrary distant nodes (global, long-range) while retaining node-centric expressive
  power.
- **G2 — Interpretability under multi-modality**: attention-only graph transformers do not expose
  a per-node, per-modality quantity that can be read as "how local vs. how global is this ROI's
  information need," which limits clinical interpretation of *which ROIs* and *which modalities*
  drive a prediction.
- **G3 — Heterogeneous multi-modal fusion**: existing GNN baselines are largely designed for a
  single feature channel per node; naively concatenating multiple biomarker features at each ROI
  does not respect the fact that different modalities may need different local/global balances at
  the same ROI (evidenced by Table 1's degraded accuracy for GCN/GAT/GraphHeat/GDC when using
  paired vs. single modalities, e.g. GDC drops to 0.842 accuracy on Cortical Thickness & FDG).

## Key Insight

Guide a **per-node, per-modality diffusion (heat-kernel) scale** with a **downstream transformer**
so that (a) an adaptive-convolution block first produces a locally-effective representation per
modality by learning how far each node's heat-kernel should diffuse, and (b) a self-attention
block — with one attention head per modality — then mixes these representations globally across
all ROIs. The scale parameters and attention scores are both learned end-to-end via the
classification loss, and both are retained after training as interpretable artifacts: node-wise
scales indicate local vs. distant information need per modality, and attention scores indicate
which ROIs receive long-range influence per modality (§2, §4).

## Assumptions

- The brain graph is fixed per subject (structural connectome from DTI tractography over a
  Destrieux-atlas parcellation) and does not change across modalities; only the *nodal features*
  (imaging measures) vary by modality (§3, Dataset).
- The normalized graph Laplacian `L̂ = D^(-1/2) L D^(-1/2)` is real, symmetric and positive
  semi-definite with a complete orthonormal eigenbasis, which is required for the heat-kernel /
  spectral-graph-theory formulation to be well-defined (§2, Prelim).
- Node-wise scales `s^m ∈ R^N` are assumed to be positive (an ℓ1-penalty with an indicator
  function enforces this during training; §2, Eq. 7).
- A single attention head per modality is sufficient to represent that modality's global
  (long-range) characteristics; multiple modalities' single-head outputs are then linearly mixed
  (§2, Modality-wise Self-Attention Block, `Φ(Q,K,V) = [h1|h2|...|hm]W^Φ`).
