# Constraints, Assumptions, and Limitations

## Boundary conditions
- **Neurotypical, middle-aged donors only** (age 30–68, minimal-to-no AD pathology). Findings describe *risk*, not established AD; extrapolation to symptomatic AD is not warranted.
- **Single brain region**: ERC only. AD involves multiple regions (e.g. locus coeruleus–ERC circuit); cross-region generalization is untested here.
- **APOE grouping**: E2+ vs E4+ carrier contrast; no E3/E3 reference group.
- **k=9 SpDs / 38 subclusters** are resolution-dependent; L5 sublayers were not resolved at k=9.

## Assumptions
- Pseudobulk covariate-adjusted models adequately control Sex, Age, Ancestry, and technical batch.
- Ancestry labels (next-of-kin + death records + FLARE genotype inference) are accurate.
- pTau visual scoring (≥3 discrete AT8 signals, blinded) is a valid proxy for early pathology (used because only 18/30 donors had Braak staging).
- APOE effect on Oligo.3 is indirect (Oligo.3 expresses low APOE); astrocyte mediation is hypothesized, not proven.

## Known limitations (stated by authors)
- **Female underpowering**: only 9 female donors (30%); sex-specific DEGs are male-dominated (e.g. 948 vs 2 broad; 1,830 vs 0 in Oligo.3) and female-specific conclusions are limited. Larger female cohorts needed.
- **Rare-subcluster power**: few cells/donor for vascular (~53/donor) and some neuronal subclusters yield few DEGs; absence of DEGs there is likely a power issue, not biology (cf. muscat, ref 74).
- **snRNA-seq vs SRT discrepancies**: vascular DEGs abundant in SRT but sparse in snRNA-seq; attributed to snRNA-seq measuring only nuclear transcripts while SRT captures cytosolic + neuropil transcripts.
- **Fine-resolution RCTD deconvolution unreliable**: only one subcluster per non-neuronal cell type commonly detected, due to difficulty distinguishing highly similar subclusters.
- **Composition analysis bias**: crumblr proportion results in snRNA-seq can be biased; orthogonal-assay validation recommended.
- **Cross-dataset comparison caveats**: differences vs Grubman/Blanchard may stem from statistical methods (marker-finding vs pseudobulk), demographics, brain region (PFC vs ERC), sample size, and presence of AD pathology.
- **Causality**: cannot determine whether APOE-associated changes originate in Oligo.3 or reflect signaling from APOE-high cell types (astrocytes); iPSC co-culture / assembloid follow-up proposed.
- **Trajectory identity**: Oligo.3 non-myelinating identity is supported by trajectory + markers, but a definitive pre-myelinating classification "needs further work to profile oligodendrocyte maturation process in the human ERC."
- **Braak staging incomplete**: only 18 donors staged; motivated the pTau immunostaining workaround.

## Preprint status
- Not peer reviewed (bioRxiv, Version 1, 2025-11-20). Values may change in later versions.
