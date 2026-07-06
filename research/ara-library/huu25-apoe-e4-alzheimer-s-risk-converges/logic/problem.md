# Problem Specification

## Observations

### O1: The ERC is one of the earliest sites of AD pathology
- **Statement**: "AD pathology progressively appears in brain regions in a specific order, with the entorhinal cortex (ERC) being one of the first cortical regions impacted in AD". "Molecular characterization of AD pathology in ERC has identified pTau tangles in Layer 2 ERC neurons and revealed AD-associated changes in white matter".
- **Evidence**: Introduction (§1), refs 9, 10, 14, 15.
- **Implication**: Molecular events in the ERC prior to clinical AD are a promising window into early, potentially reversible disease biology.

### O2: APOE genotype is the strongest genetic risk factor, and its effect is modified by ancestry and sex
- **Statement**: "the strongest genetic risk factor for AD is allelic variation at the Apolipoprotein E (APOE) locus, with APOE E4 increasing risk and APOE E2 reducing risk". "E2 and E4 alleles are more common in AA compared to EA populations, but the protective and risk effects are stronger in EA". "Females are at overall higher risk of developing AD, but the effect of sex on risk is modified by both age and ancestry".
- **Evidence**: Introduction (§1), refs 4, 5, 6, 7.
- **Implication**: Studying APOE risk without stratifying by ancestry and sex would confound the biology; a diverse cohort is required.

### O3: AD gene-expression changes are cell-type-specific, with oligodendrocytes prominent
- **Statement**: "Single-nucleus RNA-seq (snRNA-seq) studies in postmortem human prefrontal and entorhinal cortex demonstrate that many AD-related gene expression changes are cell type-specific, with oligodendrocytes showing many transcriptional differences". Prior work also reports AD-associated cell states in microglia, astrocytes and oligodendrocytes.
- **Evidence**: Introduction (§1), refs 18, 19, 20, 21.
- **Implication**: Resolving fine cell subtypes and their spatial context is needed to localize risk.

### O4: Existing AD transcriptomic studies profile disease, not neurotypical risk, and lack spatial context
- **Statement**: Prior snRNA-seq atlases (Grubman et al. ERC; Blanchard et al. PFC; Mathys et al.) study donors with AD pathology, use cell-level marker-finding statistics rather than covariate-adjusted pseudobulk, and are not spatially resolved.
- **Evidence**: §2.7, §3 (Discussion), refs 17, 18, 19; Methods (Differential expression analysis).
- **Implication**: The molecular biology of *risk before pathology*, and its spatial localization, is largely uncharacterized in the human ERC.

## Gaps

### G1: No spatially-resolved, cell-type-resolved map of APOE risk in neurotypical human ERC
- **Statement**: There is no paired SRT + snRNA-seq characterization of the human ERC stratified by APOE carrier status in middle-aged donors without clinical AD.
- **Caused by**: O1, O3, O4.
- **Existing attempts**: Disease-focused snRNA-seq atlases (refs 17–19) and DLPFC spatial atlases (refs 27, 28).
- **Why they fail**: They study advanced AD, single modalities, or different brain regions; they cannot localize risk-associated changes to specific ERC spatial domains and fine subtypes simultaneously.

### G2: Ancestry × APOE and sex × APOE interactions in brain gene expression are unresolved
- **Statement**: Whether and how ancestry and sex modify APOE-associated gene expression in the ERC is unknown.
- **Caused by**: O2, O4.
- **Existing attempts**: Epidemiological/genetic studies (refs 4, 5, 6) establish interaction at the risk level, not the molecular level.
- **Why they fail**: Cohorts are rarely balanced across ancestry, sex, and APOE simultaneously with matched multi-omic data.

### G3: The specific cell subtype and spatial compartment that carry APOE risk are unknown
- **Statement**: Broad cell types are heterogeneous; the responsible fine subtype and its maturation state / spatial niche are not identified.
- **Caused by**: O3.
- **Existing attempts**: Broad-cell-type DGE.
- **Why they fail**: Broad resolution masks subtype-specific convergence.

## Key Insight
- **Insight**: Assaying neurotypical middle-aged donors balanced across APOE carrier status, ancestry, and sex — with *paired* spatial and single-nucleus data plus covariate-adjusted pseudobulk DGE and multi-omic factor integration — localizes APOE risk to a single non-myelinating oligodendrocyte subcluster (Oligo.3) and to white-matter/vascular spatial domains, before AD pathology.
- **Derived from**: O1, O2, O3, O4.
- **Enables**: Identifying a maturation-stalled oligodendrocyte state as a candidate early-risk mechanism, with ancestry/sex modifiers and a pTau-linked multicellular signature.

## Assumptions
- A1: Donors were "middle aged brain donors with no clinical signs of AD" with "only minimal to no AD-associated pathology"; findings reflect *risk*, not established disease.
- A2: APOE carrier grouping (E2+ = E2/E2, E2/E3; E4+ = E3/E4, E4/E4) is a valid axis of AD risk (refs 7, 22, 23).
- A3: Ancestry reported by next-of-kin and death records, confirmed by DNA genotyping/FLARE, is accurate.
- A4: Pseudobulk DGE with covariate adjustment (Sex, Age, Ancestry, technical batch) appropriately controls confounders for cross-donor comparison.
- A5: snRNA-seq measures nuclear transcripts and SRT measures cytosolic + neuropil transcripts; the two are complementary rather than redundant.
