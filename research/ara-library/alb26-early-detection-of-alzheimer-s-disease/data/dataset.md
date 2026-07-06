# Dataset — Olfactory-stimulation EEG (MCI/AD)

> Grounding: verified discovery record (`sources.yaml`, `metadata.md`). This dataset is treated as
> first-class grounded input per the compile instructions and is **not re-verified** here. Details
> beyond the discovery record (channel montage, sampling rate, trial counts) are **not available
> from provided input (no full text of either paper)**.

## Provenance
- **Title**: "Brain Electrophysiological Recording during Olfactory Stimulation in Mild Cognitive
  Impairment and Alzheimer Disease Patients: An EEG Dataset"
- **Authors**: Sedghizadeh, Aghajan, Vahabi.
- **Repository**: Mendeley Data
- **DOI / identifier**: `10.17632/sgzbgwjfkr.5`
- **License**: CC BY 4.0
- **Access type**: Open access (open download).
- **Verification**: Confirmed as the reused dataset via this paper's Semantic Scholar reference list
  (`metadata.md` "Discovered sources"; `sources.yaml` data entry, `verified: true`).

## Cohort / contents
- **Subjects**: 35 seniors.
  - **13** Alzheimer's disease (AD)
  - **7** amnestic mild cognitive impairment (aMCI)
  - **15** healthy controls
- **Stimulation paradigm**: Rose/lemon **olfactory oddball** — odor stimuli presented to evoke EEG
  responses.
- **Modality**: Scalp EEG recorded during olfactory stimulation.

## Role in this study
- Sole input cohort for the transform (STFT/CWT) + deep-learning classification pipeline.
- Supplies AD/aMCI/healthy labels underlying all reported accuracies (C01–C05).

## Not available from provided input (no full text)
- EEG channel count/montage, sampling rate, recording duration, and trial structure.
- Exact odorant delivery timing and oddball ratios.
- How this paper splits the cohort (train/test) and groups the three classes.
