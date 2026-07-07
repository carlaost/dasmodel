# Constraints

## Technological/methodological limitations (stated in the paper)

- **Resolution-vs-coverage trade-off**: img-ST methods provide sub-cellular/single-molecule resolution but require a pre-selected gene panel ("the drawback of img-ST is the pre-selection of a gene-panel," paper.pdf p.2); seq-ST methods capture the whole transcriptome but at coarser native spot resolution (from ~50 μm down to ~220 nm depending on platform), and "current methods often involve trade-offs between transcriptome coverage, resolution of spatial context, and multi-module detection" (paper.pdf p.3).
- **img-ST throughput limits**: Traditional FISH is "limited in multiplexing capacity due to spectral overlap among fluorophores" (paper.pdf p.2); FISSEQ, despite subcellular resolution, has sensitivity "limited to detecting approximately 100–200 transcripts per cell under standard experimental conditions" (paper.pdf p.3).
- **Time and process cost**: img-ST "typically involves extended hybridization periods, imaging time and complicated decoding process to resolve 'pre-decided' genes" (paper.pdf p.2).
- **Mouse-model-to-human generalizability gap**: "Experimental mouse models of AD are crucial for understanding disease mechanisms but studies have proved the limitations in fully representing human AD brain environment and molecular complexities" (paper.pdf p.9).
- **Limited ST coverage of vulnerable neurons**: "Despite its promise, the use of spatial transcriptomics (ST) to study vulnerable neurons in AD brains remains relatively limited" (paper.pdf p.8), in contrast to the more extensive ST literature on glia.
- **mRNA-protein dissociation**: "Elevated levels of certain pro-inflammatory mRNAs do not necessarily correlate with their corresponding protein abundance," limiting the functional interpretability of transcriptomic (including spatial transcriptomic) findings alone (paper.pdf p.10).
- **No spatial epigenomics yet paired at scale**: "The determination of spatially resolved single-cell gene expression is the starting point ... but doesn't reveal the underlying transcriptional mechanisms. To achieve this goal, the parallel development of spatial epigenomics assays is required" (paper.pdf p.10) — implying current ST findings describe expression state but not its upstream regulatory cause.
- **2D tissue sectioning limits 3D interaction mapping**: The Conclusions explicitly flag the need for "deep tissue imaging together with ST to map comprehensive interaction cellular networks in a 3D brain" (paper.pdf p.10), implying current studies are largely limited to 2D tissue sections.

## Scope limitations of this review (self-declared)

- **No new primary data**: "No datasets were generated or analysed during the current study" (paper.pdf p.10, Data availability).
- **Focus is narrative synthesis, not systematic/meta-analytic**: The review synthesizes findings across independently designed mouse and human studies using different ST platforms, distance-masking protocols, gene panels, and disease models; no attempt is made to statistically pool or directly compare effect sizes across studies.
- **Species and model scope**: The bulk of spatially resolved cellular-interaction findings synthesized (plaque niche distance gradients, RL interaction analysis, aging clocks) derive from mouse models (5xFAD, APP/PS1, AppNL−G−F, TauPS2APP, Trem2R47H;5xFAD, LPC-induced demyelination, EAE); human-brain ST findings are comparatively sparse in the reviewed literature and are discussed in a separate, shorter section ("AD in human samples," paper.pdf p.9).

## Assumptions carried into claims (see also logic/problem.md)

- Plaque-relative distance bands (10/20/30/40 μm) are treated as broadly comparable across studies despite being generated with different plaque-masking definitions (e.g., a fixed 50 μm mask expansion vs. 20 μm grid squares vs. per-study custom binning).
- Gene-panel-based scores (activation score, Spatial Ageing Clock) are treated as valid summary readouts of broader cellular activation/aging states, even though each is derived from a specific, non-overlapping curated gene list (421-gene vs. 300-gene panels).
- Findings from single studies (e.g., the 130-candidate RL-pair count, the 14% DAA-like fraction) are reported as established rather than independently replicated across multiple cohorts.
