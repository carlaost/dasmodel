# Constraints, Assumptions, and Limitations

Source: paper's own Discussion "limitations" content (Page 12 of 17) plus constraints implicit in
the Methods.

## Boundary conditions

- **Cohort size**: The primary TC cohort comprises 40 individuals (80 samples: paired GM+WM), which
  the authors explicitly note is "smaller than those from recent studies on the prefrontal cortex"
  (citing Green et al. 2024, 424 individuals, and Mathys et al. 2023), "suggesting again that there
  may be some false negatives masked by the heterogeneous presentation of AD and the need for
  larger cohort studies."
- **QC exclusions**: Samples AD001 and AD002 were excluded from all trait-association and
  differential-expression analyses for not meeting QC criteria; two samples from one individual
  were also excluded from the TC dataset for low quality (fewer than 500 cells, low UMI/gene
  counts, elevated mitochondrial read percentage).
- **CARTANA probe-design sparsity**: "our use of multiplexed ISH through the CARTANA platform does
  suffer from sparsity, leading to noncomprehensive assignment of individual cells to broad cell
  classes or subtypes." Several snRNA-seq-derived subclusters could not be validated because their
  optimal marker genes were not available in the 155-gene probe panel; alternative (non-optimal)
  markers were substituted, and it is not possible to distinguish, from CARTANA data alone, whether
  a differential-expression signal reflects depletion of a specific cell cluster versus reduced
  gene expression within an unchanged cluster.
- **2-D spatial resolution only**: "another important limitation of the CARTANA analyses is that
  they are constrained to 2-D sections, which limits the ability to capture the effect of
  pathological inclusions above and below the plane, in 3-D," which the authors note likely
  increases expression variability and obscures additional pathology-proximal signal.
- **Microenvironment (tile-based) analysis restricted to plaques**: The tile-based plaque-density
  analysis was performed only for amyloid-beta plaques, not tangles, "because individuals with
  cortical tangle pathology did not have sufficient tangle-free tiles."
- **Global (non-cell-type-resolved) ISH signal underpowered**: The all-cell-class CARTANA
  differential expression analysis (both by Braak stage and by binarized pathology group) yielded
  no genes surviving multiple-testing correction, only nominal (2-4-fold-over-null) enrichment.
- **Unresolved discordance**: The TMEM119-vs-P2RY12 discrepancy in the CARTANA data (C11) is
  explicitly flagged by the authors as unexplained ("the underlying cause of this unusual pattern
  remains unclear"), with only partial literature precedent offered, not a mechanistic resolution.
- **Cross-sectional design**: Because the study is cross-sectional (not longitudinal), the authors
  explicitly caveat that observed proportional shifts (e.g., RPL19+ microglia depletion, TNC+
  astrocyte enrichment) "does not provide information as to whether these signatures are
  protective, reactionary, or pathological."
- **Causality from proximity-based spatial analysis**: "Although we cannot establish causality from
  proximity-based studies such as this one, we can nonetheless refine the set of candidate
  signatures that are most likely to be interacting directly with pathological inclusions in AD."

## Assumptions

(See `logic/problem.md` Assumptions A1-A6 for the full list — repeated here as they directly bound
the solution/method's validity.)

- A1: Braak stage (tau/NFT spread) adequately proxies overall AD pathological progression, chosen
  over amyloid-beta pathology per Bennett et al. 2012's finding that post-mortem tau correlates
  more strongly with cognitive impairment.
- A2: Discretizing Braak stage into three bins (0-1, 2-4, 5-6) for both ANCOM-BC and glmmTMB models
  captures disease-stage-dependent effects without losing critical granularity.
- A3: TC-derived subcluster labels transfer validly onto external datasets (EC, PFC, SFG, WM-PFC,
  SEA-AD MTG, ROSMAP PFC) via Harmony integration / Cell Type Mapper, despite region-of-origin
  differences.
- A4: Alternative (non-optimal) CARTANA marker genes, substituted due to probe-design constraints,
  still adequately discriminate the corresponding snRNA-seq-derived subclusters.
- A5: The empirically-derived plaque (<70/70-154/>154 µm) and tangle (<98/98-262/>262 µm) distance
  cutoffs capture biologically meaningful near/intermediate/far pathology microenvironments.
- A6: The 100x100-pixel (1056 µm²) tile size is an appropriate spatial unit for detecting
  microenvironment-level (plaque-density-dependent) transcriptional effects distinct from
  nearest-plaque-distance effects.

## Known limitations (paper's own statement)

1. Cohort size (40 individuals) smaller than some recent comparable single-region AD snRNA-seq
   studies, raising the possibility of false negatives from AD's heterogeneous presentation.
2. CARTANA (ISH) sparsity precludes comprehensive cell-to-subcluster assignment; differential
   expression at the CARTANA level cannot distinguish cluster depletion from within-cluster
   expression change.
3. CARTANA analysis is limited to 2-D tissue sections, omitting out-of-plane (3-D) pathology context.
4. The tile-based (plaque-density) microenvironment analysis could not be performed for tangles due
   to insufficient tangle-free tiles.
5. The global (all-cell-class) ISH differential-expression signal is statistically underpowered
   (no genes survive multiple-testing correction; only nominal enrichment detected).
6. The TMEM119-vs-P2RY12 CARTANA discordance (higher TMEM119, expected-direction P2RY12) is
   explicitly left mechanistically unresolved.
7. Cross-sectional design cannot establish whether observed compositional/expression shifts are
   protective, reactive, or directly pathological, nor establish causality between pathology
   proximity and the observed gene-expression gradients.
