# Constraints — Boundary Conditions, Assumptions, Limitations

> Grounding: abstract-only. Constraints drawn from the abstract and the verified dataset record.
> The paper's own stated limitations section is **not available from provided input (no full text)**;
> limitations below marked "(inferred)" are reconstructed from the abstract, not quoted from the paper.

## Boundary conditions
- **Signal**: EEG evoked by **olfactory stimuli** specifically (rose/lemon oddball). Findings are
  not claimed for resting-state or other-modality EEG.
- **Cohort**: A single public cohort of **35 seniors** (13 AD, 7 aMCI, 15 healthy). All results are
  within this cohort; external validation is not available from provided input (no full text).
- **Inputs to models**: 2-D time-frequency images (STFT spectrograms / CWT scalograms), not raw
  time-series — the models are image classifiers.
- **Reported metric**: Accuracy (%), at image and patient level. Other metrics not available from
  provided input (no full text).

## Assumptions (from problem.md)
- A1: Olfactory-evoked EEG carries class-discriminative information for early AD.
- A2: STFT/CWT image representations preserve that discriminative structure for image classifiers.
- A3: The 35-subject cohort is adequate to train and evaluate the deep models.

## Limitations
- **Small, single-site cohort (inferred)**: 35 subjects with class imbalance (13/7/15) bounds
  generalization and inflates the risk of optimistic accuracy estimates — the abstract itself names
  "scarce datasets" and "model generalization" as obstacles in the field.
- **No external validation (inferred)**: Only one dataset is used; cross-dataset transfer is not
  available from provided input (no full text).
- **Handling of aMCI unclear**: Whether the prodromal aMCI group is merged with AD, with healthy, or
  treated as a third class is not available from provided input (no full text) — this materially
  affects interpretation of "early detection".
- **Evaluation-protocol opacity (compile-time)**: Because only the abstract was available, the
  train/test split, cross-validation scheme, and whether patient-level evaluation avoids subject
  leakage cannot be assessed. This is a limitation of THIS ARA's grounding, not necessarily of the
  paper.
- **No code released**: No software repository is cited or discoverable (`sources.yaml` `code: []`),
  limiting exact reproducibility.
