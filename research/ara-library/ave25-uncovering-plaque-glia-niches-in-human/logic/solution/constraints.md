# Constraints, Assumptions, and Limitations

Source: paper's own "Limitations" subsection (Discussion, Page 21 of 23) plus constraints implicit
in the Methods.

## Boundary conditions

- **Sex and age**: All 21 ST donors are female with a mean age of 92 (chosen because there were
  insufficient age-matched males meeting the selection criteria — RIN>5, age-matched, minimal
  freezing artifacts — in the available ROSMAP cohort at the time of selection). Generalization to
  younger age groups or males is untested.
- **AD-status confound with Aβ stratum**: Because Aβ-positive spots came primarily from AD cases,
  the study is underpowered to separately assess the intersection of clinical AD status with the
  detected plaque-glia transcriptional signatures.
- **Spatial resolution**: The Visium platform's ~55 µm spot resolution, combined with the fact that
  both astrocytes and microglia typically co-occur in plaque-containing spots, leaves the study
  underpowered to resolve astrocyte-specific vs. microglia-specific transcriptional responses
  within a spot — the in vitro iMGL/astrocyte co-culture (E10) is one way the paper compensates
  for this limitation.
- **Plaque-type scoring on frozen tissue**: Frequent freezing artifacts in the postmortem frozen
  ST sections, combined with the large dataset size (258,986/258,987 spots), precluded
  definitively categorizing individual plaques as diffuse/compact/dense-core at scale; the study
  instead used continuous Aβ-intensity-derived no/low/high categories (validated against manual
  plaque typing on a subset, C05).
- **Marker panel breadth**: IHC was limited to three proteins (Aβ, GFAP, IBA1) per section pair (plus
  supplementary panels with NeuN/SYP/CD68/cleaved-caspase-3 in separate validation cohorts), so
  the study focused on extracellular Aβ pathology and surrounding glia rather than intracellular
  pathologies such as neurofibrillary tangles.
- **In vitro exposure window**: The iPSC co-culture Aβ-oligomer treatment lasted only 24 h; longer
  exposure might elicit more pronounced astrocyte/neuron responses not detected in this study.
- **Cultured-microglia divergence from in vivo microglia**: iMGLs are known to diverge
  transcriptionally from in vivo microglia in the absence of brain-specific environmental cues
  (refs 71-72), so the iMGL cross-validation (C08, C09) should be read as partial recapitulation,
  not full equivalence, of the in vivo signature.

## Assumptions

(See `logic/problem.md` Assumptions A1-A5 for the full list — repeated here as they directly bound
the solution/method's validity.)

- A1: Adjacent-section IHC intensity (registered via manual landmark correspondence) is a valid
  proxy for the pathology present in each ST spot of the sequenced middle section.
- A2: Manually calibrated Aβ/glia intensity thresholds (derived from 781 annotated plaques)
  generalize across all 78 sections and 21 donors.
- A3: Section-level pseudobulk aggregation is an adequate representation of niche-specific
  expression for LMM contrasts, despite discarding intra-niche, intra-section spot heterogeneity.
- A4: Mouse-derived (PIG/OLIG/DAM/DAA) and human-derived (MG0-MG12) reference gene modules are
  appropriate external genesets for interpreting this dataset's GSEA results.
- A5: A 24 h Aβ-oligomer exposure in a 2-cell-type-source iPSC co-culture is sufficient to elicit a
  transcriptional response informative about the chronic, multicellular in vivo niche.

## Known limitations (paper's own statement)

1. Aged, all-female cohort (mean age 92) — generalization to younger/male populations untested.
2. Underpowered to test AD-status × niche-type interaction (Aβ-positive spots came mostly from AD cases).
3. Underpowered to separate astrocyte-specific from microglia-specific responses within a spot
   (~55 µm Visium resolution).
4. Could not definitively classify plaque type (diffuse/compact/dense-core) at scale on frozen
   sections due to freezing artifacts; used intensity-based no/low/high grouping instead.
5. Limited to 3 co-stained IHC markers per adjacent-section pair, restricting focus to extracellular
   Aβ/glia pathology (not intracellular pathologies such as neurofibrillary tangles).
6. In vitro Aβ-oligomer exposure was short (24 h); cultured iMGLs are known to diverge
   transcriptionally from in vivo microglia absent brain-specific environmental cues.
