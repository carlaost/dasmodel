# Classification Method: Manly et al. (2022) Decision Rule

This is the classification algorithm applied to the SHARE-HCAP validation subsample (Step (b) of
`logic/solution/study_design.md`), imported unchanged from Manly et al. (2022) — see
`logic/related_work.md` RW02. Reconstructed from the paper's own prose description (p.3,
"Classification in the SHARE-HCAP sample"); full technical detail is in Supplementary Section S1
(not available from provided input).

## Grounding
`# Grounding: reconstructed` — from the paper's stated prose description (p.3), which references
Manly et al. (2022, JAMA Neurology, ref 24) and NIA-AA diagnostic-guideline workgroups (refs 25, 26)
as the source of the underlying diagnostic criteria. No code or pseudocode for this rule is printed
in the paper; the decision logic below is transcribed directly from the text, not invented.

## Inputs
- **Factor score estimates** for five domains of cognition, derived for every SHARE-HCAP respondent:
  memory, executive functioning, visuospatial skills, language and fluency, orientation.
- **Normative sample benchmark**: factor scores are evaluated against a normative sample to set the
  classification threshold (1.5 SDs below the normative mean).
- **Informant report**: a family member or friend's report of the respondent's functional
  impairment.
- **Self-report**: the respondent's own report of memory concerns (used only in one branch, see
  below).

## Decision rule (verbatim logic from paper, p.3)
1. **Demented**: factor scores of **at least two** cognitive domains are ≥1.5 SDs below the
   normative-sample mean, **AND** functional impairment is reported by an informant.
2. **MCI**, if any of the following holds:
   - Exactly **one** cognitive domain is below the 1.5-SD threshold **AND** an informant reports
     functional impairment; or
   - **At least one** cognitive domain is below the threshold **without** an informant report of
     functional impairment; or
   - **One** cognitive domain is below the threshold, **no** informant report of functional
     impairment, **but** the respondent self-reports memory concerns.
3. **Normal**, if either of the following holds:
   - **No** cognitive domain meets the impairment criteria; or
   - **One** cognitive domain is below the threshold but **neither** a self-report **nor** an
     informant-report of cognitive concerns is present.

## Rationale for adopting this specific algorithm (not a paper-original design choice)
> "We choose this approach to allow cross-HCAP study comparisons" (p.3, citing refs 27, 28 — Gross
> et al. 2024 LASI-DAD India; Farrell et al. 2024 rural South Africa).

This is the same classification rule Manly et al. (2022) used to estimate US dementia/MCI
prevalence, itself grounded in NIA-AA diagnostic criteria for MCI (Albert et al. 2011, ref 25) and
dementia due to Alzheimer's disease (McKhann et al. 2011, ref 26) — see `logic/related_work.md`
RW02, RW07.

## Boundary conditions and known limitation
- The five-domain factor structure follows Jones et al. (2024, ref 22), developed for the US HRS
  HCAP battery — see `logic/related_work.md` (Measurement instruments imported without modification).
- The 1.5-SD normative threshold and the overall decision-rule structure are assumed (not
  independently re-validated for Europe) to transfer unchanged from the US context; see assumption
  A2 in `logic/solution/constraints.md`.

## Downstream use
This classification (applied only within the 5-country, N=2,687 SHARE-HCAP validation subsample)
is the "ground truth" that Step (c)'s Hurd et al. regression relates to shared SHARE-parent cognition
items, in order to extend cognitive-status prediction to the full 28-unit SHARE parent sample where
this classification itself is not directly observable — see `logic/claims.md` C06, C12, C13 and
`logic/experiments.md` E01, E02.
