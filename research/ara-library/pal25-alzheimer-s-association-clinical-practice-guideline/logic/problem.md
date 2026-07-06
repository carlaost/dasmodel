# Problem Specification

## Observations

### O1: AD is the leading cause of dementia and a growing public-health burden
- **Statement**: AD contributes an estimated 60% to 80% of all dementias; approximately 7.2 million Americans are living with AD dementia in 2025, a number projected to double by 2060.
- **Evidence**: §1 Introduction ("contributing to an estimated 60% to 80% of all dementias"; "approximately 7.2 million Americans are living with AD dementia in 2025. This number is projected to double by 2060").
- **Implication**: Accurate, scalable in-vivo detection of AD pathology is an urgent and expanding need.

### O2: Existing ante-mortem confirmation methods are expensive, invasive, or inaccessible
- **Statement**: Historically, ante-mortem detection of AD pathology has been limited to PET (expensive) or CSF analysis (invasive but safe when properly performed); these remain out of reach for most providers, even in many specialized settings.
- **Evidence**: §1 Introduction ("expensive, such as positron emission tomography (PET), or invasive but safe when properly performed, such as cerebrospinal fluid (CSF)-based biomarker analysis"; "these tools remain out of reach to most healthcare providers").
- **Implication**: A less costly, less invasive, more accessible confirmation modality would materially expand access.

### O3: Amyloid-targeting therapies require biomarker confirmation of amyloid pathology
- **Statement**: Recent regulatory approvals of amyloid-targeting therapies require biomarker confirmation of amyloid pathology to determine treatment eligibility.
- **Evidence**: §1 Introduction ("require biomarker confirmation of amyloid pathology to determine treatment eligibility").
- **Implication**: Demand for accurate biomarker-based diagnostics to identify eligible patients is expected to rise substantially.

### O4: BBMs are available but performance varies and integration is inconsistent
- **Statement**: Multiple BBMs are commercially available and offer advantages (less costly, more accessible, more acceptable), but diagnostic performance varies across tests and clinical integration is still inconsistent.
- **Evidence**: §1 Introduction ("diagnostic performance varies across available tests, and their integration into clinical practice is still inconsistent").
- **Implication**: A formal, performance-based guideline is needed to standardize appropriate use.

### O5: Diagnostic accuracy across evaluated tests is highly variable
- **Statement**: Across all 31 tests evaluated, pooled sensitivity ranged from 49.31% to 91.41% and pooled specificity ranged from 61.54% to 96.72%.
- **Evidence**: §3.4 Diagnostic test accuracy ("Across all 31 tests, pooled Sn ranged from 49.31% to 91.41%, and Sp ranged from 61.54% to 96.72%").
- **Implication**: Many tests fall short of the thresholds needed to confidently rule in or rule out amyloid pathology with a single cut-point.

## Gaps

### G1: Absence of a formal Clinical Practice Guideline for BBMs
- **Statement**: Despite the 2022 appropriate-use recommendations, revised diagnostic criteria, and CEOi minimum-performance recommendations, no formal Clinical Practice Guideline existed to govern consistent, evidence-based BBM use in real-world settings.
- **Caused by**: O1, O2, O3, O4
- **Existing attempts**: 2022 Alzheimer's Association appropriate use recommendations (ref 18); revised AD diagnostic/staging criteria (ref 3); Global CEO Initiative (CEOi) minimum-performance recommendations (ref 15).
- **Why they fail**: These are appropriate-use recommendations, diagnostic criteria, or expert-opinion performance targets, not a systematic-review-grounded, GRADE-based CPG with formal recommendations.

### G2: No agreed, evidence-linked accuracy thresholds tied to clinical roles (triage vs confirmatory)
- **Statement**: There was no consensus, evidence-linked definition of minimum acceptable diagnostic accuracy for using a BBM as a triaging versus confirmatory test.
- **Caused by**: O4, O5
- **Existing attempts**: Expert opinion (CEOi, ref 15) used as a starting point.
- **Why they fail**: Expert opinion alone is not tied to a transparent systematic review and EtD process spanning benefits, harms, values, resources, equity, acceptability, and feasibility.

### G3: Primary studies frequently pool cognitively impaired and unimpaired populations
- **Statement**: 84 otherwise-eligible studies were excluded because cognitively impaired and unimpaired populations were analyzed together, preventing extraction of data on only cognitively impaired individuals.
- **Caused by**: heterogeneous reporting practices in primary literature.
- **Existing attempts**: None specific.
- **Why they fail**: Combined populations with bimodal amyloid distributions can make test performance appear more favorable, introducing indirectness for the target population.

## Key Insight
- **Insight**: Decouple the recommendation from any specific commercial product by issuing a **brand-agnostic, performance-based** guideline: define minimum acceptable sensitivity/specificity thresholds for two clinical roles (triaging and confirmatory) and link the CPG to a continuously updated systematic review, so the recommendations stay durable as individual tests and evidence evolve.
- **Derived from**: O4, O5, G1, G2
- **Enables**: Recommendations that remain valid as new tests appear, avoiding the need to endorse or rank named assays and protecting the guideline from perceived bias and rapid obsolescence.

## Assumptions
- A1: Clinician-relevant, real-world acceptable accuracy can be anchored to thresholds (Sn ≥90%/Sp ≥75% for triage; Sn ≥90%/Sp ≥90% for confirmatory), using recent expert opinion (CEOi) as a starting point.
- A2: Sensitivity carries greater weight for certainty in triaging decisions; specificity carries greater weight for confirmatory decisions.
- A3: Combining data from cognitively impaired and unimpaired populations would introduce indirectness and inflate apparent performance, so only cognitively impaired data are used (an a priori decision).
- A4: A BBM test = the combination of an analyte and the technology used to measure it; assays for the same analyte can differ in performance and must be evaluated separately.
- A5: Youden's-index single-cutoff performance is the primary basis for the meta-analysis; two-cutoff approaches are deferred pending more peer-reviewed evidence.
- A6: The reference standard for AD pathology is CSF AD biomarkers, amyloid PET, or neuropathological assessment.
