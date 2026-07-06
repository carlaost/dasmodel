# Study Design

## Rationale
Exploit the stereotyped spatiotemporal spread of AD (association → primary cortex) so that a
resilient region at late stage can be contrasted with a vulnerable region at early stage, and a
prototype resilient subtype (Ex5 L4 IT) can be contrasted with a prototype vulnerable subtype
(Ex2 L2/3 IT) across a region × stage grid. Resilience genes are expected to be *upregulated,
early, and BA17-enriched*.

## Regions compared
| Region | Area | Role in AD | Notes |
|--------|------|-----------|-------|
| BA9 | Prefrontal cortex | Early-affected (association) | thin, discontinuous L4 (~8.6% of ribbon); mostly 10x v3 |
| BA7 | Precuneus | Early-affected (association) | included in snRNA-seq cohort |
| BA17 | Primary visual cortex (striate) | Late-affected (Braak VI); considered resilient | expanded, myelinated L4 (~38% of ribbon; line of Gennari); predominantly Drop-seq |

## Cohort and grouping
- 46 donors, Braak stages 0–VI. Region participation: 42 BA9, 15 BA7, 24 BA17 (cohorts only partially overlap → residual confounding noted as a limitation).
- 243 snRNA-seq samples (184 Drop-seq + 59 10x Genomics), 37 sequencing batches.
- Pathology groups by ABC/Braak/CERAD criteria (overall donor counts): **low 18** (6F/12M), **intermediate 10** (7F/3M), **high 18** (12F/6M).
  - Low: no tau/amyloid, low ADNC, or PART (Braak I–III, no amyloid).
  - Intermediate: Braak III–IV + diffuse or sparse (C1) neuritic plaques.
  - High: Braak V–VI + moderate (C2) or abundant (C3) neuritic plaques.
- Mean age (low/int/high): 70.5±9.2 / 81.9±13.6 / 82.4±10.4 years. RIN: 5.8±0.7 / 6.2±0.7 / 6.2±0.7. PMI (h): 15.6±8.2 / 12.8±8.2 / 13.8±9.7.
- **Note (reproduced from source):** Fig. 4 caption gives *region-specific* donor counts that differ from the overall grouping — BA9: low 17, intermediate 10, high 15; BA17: low 7, intermediate 5, high 12. These are the per-region subcohorts used in the compositional models, distinct from the 18/10/18 overall counts.

## Modalities integrated
1. **snRNA-seq** (Drop-seq + 10x v2/v3): 655,407 nuclei → 424,528 after QC (362,224 neuronal: 282,930 excitatory, 79,294 inhibitory; 62,304 non-neuronal). 18 Ex + 19 In clusters.
2. **Xenium single-cell spatial** (266-gene + custom 100-gene panels): 16 sections (8 BA9, 8 BA17), 4 AD + 4 control → 765,992 cells after QC.
3. **Visium spatial** (1186-gene Human Neuroscience panel + custom 197-gene = 1383 genes): 16 sections; Stereoscope deconvolution.
4. **Reference-dataset validation**: scANVI/ingest label transfer + cosine distance vs SEA-AD DLPFC/MTG, BICCN, Jorstad, Mathys, Green.
5. **Functional validation**: AAV Kcnip4 overexpression in vitro (calcium imaging) and in vivo (AppSAA mouse; c-Fos/Arc/amyloid/GFAP/IBA1).

## Analytical strategy
- Neuronal-subtype composition: scCODA + GLMM (with sensitivity/stress tests) → resilience/vulnerability calls.
- Differential expression: multi-method "high-confidence" consensus (LMM ∩ bootstrap/pseudobulk/hdWGCNA) → conservative resilience gene catalog.
- Systems level: hdWGCNA co-expression modules and hub genes.
- Proof-of-principle: KCNIP4 selected as a consistently upregulated, hub, AD-risk-associated excitability regulator, then functionally tested.
