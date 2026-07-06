# Datasets

Source: §4 (Datasets), Table 2. Six public AD cohorts; all secondary-use, publicly available but
registration/DUA-gated (access: request per `sources.yaml`). No new dataset was released.

## Summary (Table 2)
| Dataset | Subjects | Diagnostic categories | Imaging modalities | Longitudinal | Intended use |
|---|---|---|---|---|---|
| ADNI | >2000 | 3 (CN, MCI, AD) | MRI; PET (amyloid, FDG, tau); CSF, etc. | Yes — multi-year | Diagnosis & Prognosis |
| OASIS-3 | ~1100 | 2–3 (CN, MCI/AD) | MRI (T1, fMRI, DTI, etc.); PET (amyloid) | Yes — up to 15 yrs | Diagnosis & Prognosis |
| AIBL | 2359 (expanded) | 3 (CN, MCI, AD) | MRI; PET (amyloid) | Yes — 18 mo intervals | Diagnosis & Prognosis |
| BioFINDER | ~2000 | 3 (CN, MCI, AD) | MRI; PET (amyloid & tau); CSF | Yes — 2–5+ yrs | Diagnosis & Prognosis |
| TADPOLE | 219 (ADNI subset) | 3 (CN, MCI, AD) | MRI; PET; CSF; clinical tests | Yes — predict 5 yrs | Prognosis (Challenge) |
| MIRIAD | 69 | 2 (AD, CN) | MRI (T1-weighted) | Yes — up to 2 yrs | Reliability (Atrophy) |

CN = cognitively normal; MCI = mild cognitive impairment; AD = Alzheimer's dementia.

## Per-cohort provenance (§4)
- **ADNI** (2004–present): longitudinal multi-center program validating imaging/fluid biomarkers for AD trials; serial 3D MRI and PET (amyloid, tau, FDG), CSF, genetics, standardized clinical assessments at ~6–12-month intervals. Phase enrollment reported by cohort (ADNI-1: 819; ADNI-GO/2/3 expanding). Access via LONI portal. Refs [28].
- **OASIS-3**: ~15 years of imaging/clinical data from the Knight ADRC; ~1098 participants in the release; >2100 MRI sessions and ~1400–1500 PET sessions (amyloid and FDG) plus processed derivatives; many with multi-year follow-up; open access. Refs [29,30]. Figure 7 shows 3 processed samples (T1w + FreeSurfer + DL segmentation + DL+DiReCT thickness map, radiological view).
- **AIBL** (launched 2006): prospective lifestyle/biomarker cohort; baseline 1112 older adults (768 CN / 133 MCI / 211 AD) with ~18-month reassessments; high-resolution MRI + amyloid-PET subset (e.g. [11C]PiB); expanded to 2359 in later waves. Refs [32,33].
- **BioFINDER**: ongoing Swedish longitudinal multimodal biomarker program across the AD spectrum; MRI, amyloid PET, tau PET, FDG-PET, CSF, cognition; BioFINDER-2 reports ~1400–2000 participants. Rich PET/biofluid profiling supports ATN-framework alignment. Refs [34,35].
- **TADPOLE**: prognosis benchmark built from ADNI; forecast 5-year outcomes — diagnosis (CN/MCI/AD), ADAS-Cog13, ventricular volume — for 219 "rollover" subjects using multimodal baselines (MRI, PET, CSF, APOE, cognition). Challenge attracted 33 teams and 92 algorithms; provides standard splits/evaluation. Refs [36,37]. (In §5 the conversion horizon is described as "3-year" and tdAUC is reported "@36m" — note the 5-yr vs 3-yr discrepancy in `logic/solution/constraints.md`.)
- **MIRIAD**: 69 adults (46 AD, 23 CN) scanned up to eight times over 2 years on the same 1.5T system with tightly controlled intervals (weeks to months). Standardized T1 MRI and consistent setup enable separation of true atrophy from measurement noise; used for test–retest reliability and minimal detectable change. Refs [38]. Figure 8 shows (a) normal and (b) Alzheimer's samples.

## Data split roles (Figure 6)
- **Unlabeled SSL pool**: ADNI, OASIS-3, AIBL, BioFINDER.
- **Labeled fine-tuning**: ADNI (diagnosis & MCI→AD), OASIS-3, TADPOLE (prognosis labels).
- **Reliability only**: MIRIAD (held out; never pretrained on when reported as external test).

## Licensing / ethics
All cohorts are de-identified secondary-use public datasets requiring registration/DUA. IRB and
informed-consent statements are "Not applicable" for this secondary-use study. No accession IDs,
DOIs for a released split file, or repository URL for the authors' own CV splits/seeds were provided.
