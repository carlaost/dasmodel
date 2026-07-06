# Constraints, Assumptions, and Limitations

## Boundary conditions
- Findings are from cross-sectional postmortem human tissue (Braak 0–VI) plus a mouse overexpression model; they establish association and a proof-of-principle causal test, not longitudinal human causation.
- "Resilience" is defined as *relative* (compositional) preservation and early upregulation of protective genes — not absolute cell-count preservation.
- Region-specific findings are explicitly framed by the authors as **hypothesis-generating**.

## Assumptions (see also problem.md A1–A5)
- Low/intermediate/high pathology approximates monotonic disease progression; late-BA17 changes are expected to be concordant with early-BA9 changes.
- CaMKIIa-driven broad AAV overexpression of mouse Kcnip4 is an acceptable model of the cell-type-specific human upregulation, despite not recapitulating cell-type specificity.
- c-Fos and Arc are valid activation/hyperexcitability readouts.

## Known limitations (verbatim-grounded)
1. **Partially overlapping regional cohorts** → inherent differences in age, sex, and neuropathological severity across regional subcohorts; covariates were modeled but residual confounding remains. Donor cohorts contributing to each region do not fully overlap.
2. **Multiple sequencing platforms** (Drop-seq and 10x v2/v3) introduce technical variability; BA17 was predominantly Drop-seq while BA9/BA7 used 10x v3, so differences in sensitivity/detection may contribute to apparent regional differences and to the *directionality* of DE genes. Batch correction and platform covariates were applied but residual effects may persist.
3. **Conservative multi-method DGE** likely prioritizes higher-baseline, larger-effect, more stable genes and may underrepresent subtler, context-dependent, or donor-restricted changes → the gene set is a robust conservative catalog, not exhaustive.
4. **hdWGCNA does not natively support covariates**; age/sex/APOE were not included in network construction, so residual confounding may affect module composition / hub-gene identification.
5. **Small donor numbers and different donor subsets across regions** limit power to detect subtle changes, especially in rare cell types or gradient-like populations (e.g., SST interneurons, L2/3 IT showed trends, not robust changes, despite literature vulnerability).
6. **Ex5 likely comprises several finer molecular subtypes**; resolution is limited relative to high-granularity taxonomies (matches Jorstad L4_IT2/3/5).
7. **Mouse model**: only male mice used (due to small sample size; prior work reported sex differences in behavior but not pathology); broad overexpression does not reproduce cell-type-specific regulation; investigators were not blinded during analysis.
8. **QC cutoffs matter for Ex5**: Ex5 neurons have small somata / low gene counts; a rescue analysis of 200–300-gene nuclei was required to confirm the QC filter (<300 genes) did not distort Ex5 preservation.
9. **Low case numbers limit cross-region L4 comparisons** (BA9/BA17/BA18) in Xenium.

## Ethics / governance
- Human tissue deidentified; study granted Not Human Subjects Research (NHSR) determination; informed consent for donation obtained. IRBs: UCLA/Easton; NIH Neurobiobank (Sepulveda PCC# 2015-060672 / VA #0002; Mt. Sinai HAR-13-059); Stanford IRB-33727. Animal protocol Stanford APLAC ID 33824.
