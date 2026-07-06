# Study Design — PRISMA-2020 Systematic Review Methodology

Mirrors §3 (Methodology) and the PRISMA flow diagram (Fig. 2). Exact stage counts live in
`evidence/figures/figure2.md` and `evidence/tables/table2.md`; this file records the *design*.

## Reporting framework
- Conducted per the methodological framework for literature reviews [59] and reported per **PRISMA 2020** [60].
- Primary objective: evaluate the effectiveness of ViT and CViT models in AD classification and MCI-conversion prediction across three input configurations: single-modality; multimodal neuroimaging; combined neuroimaging + clinical (structured/unstructured) data.
- "Clinical data" defined broadly: demographics, patient history, cognitive tests, fluid biomarkers, genetics.

## Search strategy (§3.1)
- **Databases (5)**: Scopus, Web of Science, ScienceDirect, IEEE Xplore, PubMed.
- **Date executed**: 20 February 2025.
- **Query construction**: four Boolean-combined concept domains, each enriched with synonyms/abbreviations:
  1. Disease & patient cohort — "Alzheimer's disease", "AD", "Dementia", "Mild Cognitive Impairment", "MCI", "pMCI", "sMCI", "Cognitive Decline", "Neurodegenerative".
  2. Core technology & architecture — "Vision Transformer", "ViT", "Convolutional Vision Transformer", "CViT", "Swin Transformer", "self-attention", "Transformer-based model", "Attention-based".
  3. Primary objective & task — "classification", "prediction", "diagnosis", "detection", "prognosis", "staging".
  4. Data & methodology — "multimodal", "multimodality", "data fusion", "integration", "neuroimaging", "MRI", "PET", "fMRI", "clinical data", "biomarkers" (supplementary/manual screening).
- Final string: (domain 1) AND (domain 2) AND (domain 3), with per-database syntactic adjustments.

## Eligibility criteria (Table 3, §3.2)
| Parameter | Include | Exclude |
|-----------|---------|---------|
| Investigation | AD classification or MCI conversion prediction with neuroimaging/clinical data | Neither task, nor neuroimaging/clinical data |
| AI algorithm | Any form of ViT or CViT | ViT/CViT absent (CNN/3DCNN/ML-only) |
| Study type | Journal articles only | Non-journal |
| Experimental results | Reports performance metrics | No metrics; reviews, patents, conf. abstracts, book chapters, surveys, preprints |
| Year | 2021–2025 | Outside range |
| Language | English | Non-English |
| Database | Found in the five listed databases | Elsewhere |

## Screening pipeline (§3.2, Fig. 2)
1. **Identification**: 564 records from the 5 databases.
2. **Duplicate removal**: → 404 unique records.
3. **Title/abstract screening**: 261 excluded → 144 retained.
4. **Full-text eligibility**: 76 excluded (with reasons) → **68 included**.
- Two independent reviewers; consensus-based final selection to minimize selection bias.
- During full-text review, studies were explicitly assessed for **data leakage** (a known cause of inflated ML performance in medical imaging).

## Data extraction & analysis (§3.3)
For each included study, extracted: publication year; diagnostic focus (AD classification / MCI
conversion); modality configuration (single/multi); medical modality (MRI, PET, DTI, CT, CSF,
genetic, …); fusion strategy (for multimodal); dataset specifics; AI technique; classification
categories; internal validation; external validation; and performance metrics (accuracy, AUC,
sensitivity, specificity, precision). Findings were then organized via the four taxonomies (see
`taxonomies.md`) and synthesized into Tables 4–8 and Figs. 15–17, 25, 42.
