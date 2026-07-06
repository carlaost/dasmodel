# Concepts — TRAILBLAZER-ALZ 4

## Amyloid plaque (AP) clearance
- **Notation**: AP clearance ⇔ florbetapir PET < 24.1 CL
- **Definition**: The primary efficacy construct: achievement of a brain amyloid PET level below 24.1 Centiloids on florbetapir F18 PET, interpreted as clearance of amyloid plaque (refs 17, 18).
- **Boundary conditions**: Threshold applies to florbetapir-derived Centiloids; distinct from the more stringent donanemab dosing-cessation criteria (< 11 CL on one scan, or ≥11 to < 25 CL on two consecutive scans).
- **Related concepts**: Centiloid scale, florbetapir F18 PET, donanemab cessation criteria

## Centiloid (CL) scale
- **Notation**: CL
- **Definition**: Standardized quantitative scale for brain amyloid PET, anchoring the mean cortical standardized uptake value ratio (SUVR, whole-cerebellar reference) to a 0–100 scale; used to define clearance (< 24.1 CL) and eligibility (≥37 CL positive scan / ≥50 CL negative scan).
- **Boundary conditions**: Derived here from florbetapir SUVR via an established semi-automated pipeline (ref 16); values are amyloid-tracer-specific.
- **Related concepts**: AP clearance, florbetapir F18 PET, SUVR

## Florbetapir F18 PET
- **Notation**: —
- **Definition**: Positron-emission-tomography amyloid imaging with the F18 florbetapir tracer; 5-minute frames motion-corrected and averaged, aligned to a standard template, mean cortical SUVR (whole-cerebellar reference) measured and converted to CL. Read by personnel blinded to treatment.
- **Boundary conditions**: Used for eligibility, clearance endpoints, and change-from-baseline; distinct from flortaucipir (tau) PET.
- **Related concepts**: Centiloid scale, flortaucipir PET, AP clearance

## Low–medium tau subpopulation
- **Notation**: —
- **Definition**: Prespecified subpopulation defined by visual and quantitative flortaucipir F18 PET reads (as in TRAILBLAZER-ALZ / ALZ 2, refs 13,14,19,20); ~50% of enrollees anticipated; forms the second co-primary analysis set.
- **Boundary conditions**: Requires a baseline flortaucipir PET; tau PET was not used for overall eligibility.
- **Related concepts**: Flortaucipir PET, co-primary endpoint

## ARIA-E (amyloid-related imaging abnormalities — edema/effusion)
- **Notation**: ARIA-E
- **Definition**: Class-effect adverse event of anti-amyloid antibodies, comprising vasogenic edema/effusion detected on MRI; here identified via TEAE cluster (ARIA edema/effusion, brain edema, vasogenic cerebral edema) plus central MRI.
- **Boundary conditions**: An AE of special interest; graded by radiographic severity and symptomatic status; excluded at screening.
- **Related concepts**: ARIA-H, safety MRI, APOE ε4

## ARIA-H (amyloid-related imaging abnormalities — microhemorrhage/hemosiderin)
- **Notation**: ARIA-H
- **Definition**: Class-effect adverse event comprising microhemorrhage, hemosiderin deposits, and superficial siderosis; identified via a TEAE cluster (microhemorrhage, brainstem/cerebellar microhemorrhage, cerebral hemosiderin deposit, cerebral microhemorrhage, CNS superficial siderosis) plus central MRI.
- **Boundary conditions**: AE of special interest; > 4 microhemorrhages or > 1 superficial siderosis focus at screening were exclusionary.
- **Related concepts**: ARIA-E, superficial siderosis, APOE ε4

## Donanemab dosing-cessation criteria
- **Notation**: —
- **Definition**: Prespecified rule to stop donanemab infusions once amyloid is sufficiently cleared: AP level < 11 CL on any single florbetapir PET scan, or ≥11 to < 25 CL on two consecutive scans (assessed at weeks 24 and 52). Participants meeting criteria continued all other assessments.
- **Boundary conditions**: Applies only to the donanemab arm; distinct from the 24.1-CL clearance endpoint.
- **Related concepts**: AP clearance, florbetapir F18 PET

## Gated (hierarchical) multiplicity control
- **Notation**: —
- **Definition**: Testing procedure in which key secondary endpoints are evaluated only if both co-primary endpoints are significant, in a fixed order: mean change in AP at 6 months → 12 months → time to AP clearance (at study completion) → mean change at 18 months.
- **Boundary conditions**: Two-sided α = 0.05; preserves family-wise error across primary and key secondary endpoints.
- **Related concepts**: Co-primary endpoints, MMRM, ANCOVA

## MMRM / ANCOVA amyloid-change models
- **Notation**: —
- **Definition**: The mean-change analysis models: ANCOVA at 6 months (single postbaseline PET; treatment fixed effect + APOE ε4 status, baseline amyloid, baseline age covariates) and MMRM at 12/18 months (treatment, time, treatment-by-time interaction + same covariates).
- **Boundary conditions**: Applied identically to absolute (CL) and percent-change endpoints, and to overall and low–medium tau sets.
- **Related concepts**: Gated multiplicity control, AP clearance

## Plasma AD biomarkers (p-tau217, p-tau181, GFAP, NfL)
- **Notation**: p-tau217, p-tau181, GFAP, NfL
- **Definition**: Exploratory blood-based markers: phosphorylated tau 217/181 (AD-specific pathology), glial fibrillary acidic protein (astrocytic reactivity), neurofilament light chain (neuroaxonal injury); log-transformed and analyzed by MMRM.
- **Boundary conditions**: Exploratory endpoints, higher variability; not part of the gated efficacy hierarchy.
- **Related concepts**: MMRM, AP clearance
