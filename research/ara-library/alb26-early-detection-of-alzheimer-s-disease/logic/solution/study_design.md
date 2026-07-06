# Study Design

> Grounding: abstract-only. Reconstructed from the abstract and the verified dataset record
> (`sources.yaml`, `metadata.md`). Protocol details not stated in those sources read "Not available
> from provided input (no full text)".

## Nature of study
Retrospective computational analysis on an existing, public olfactory-EEG dataset. No new data
collection and **no clinical-trial registration** (no NCT/PROSPERO) is associated — confirmed in
`sources.yaml` (`clinical_trials: []`).

## Cohort
- **Source**: Public olfactory-stimulation EEG dataset (Sedghizadeh, Aghajan, Vahabi), Mendeley
  Data DOI `10.17632/sgzbgwjfkr.5`, CC BY 4.0, open access.
- **Subjects**: 35 seniors — **13 AD, 7 aMCI, 15 healthy**.
- **Paradigm**: Rose/lemon olfactory oddball (odor stimuli evoking EEG responses).
- **Class labelling in this paper** (AD vs healthy vs aMCI grouping, or a binary vs three-class
  problem): Not available from provided input (no full text).

## Independent variables compared
- **Transform**: STFT vs CWT (EEG → time-frequency image).
- **Classifier**: ViT, custom CNN, CNN+CatBoost, ResNet50, VGG16.

## Evaluation levels
- **Image level** — accuracy per time-frequency image.
- **Patient level** — accuracy per subject (predictions aggregated). Foregrounded as the primary
  clinical metric; CWT was highest at this level.

## Reported outcomes (see claims.md / evidence)
- Best configuration: CWT + ViT — 91.43% patient-level, 85.18% image-level.
- Image-level CNN family: CNN+CatBoost 81.66%, CNN 81.25%, ResNet50 80.69%, VGG16 79.82%.

## Not available from provided input (no full text)
- Train/test split or cross-validation scheme (e.g. leave-one-subject-out vs random image split).
- Whether patient-level and image-level evaluations share the same held-out subjects.
- Statistical testing of accuracy differences.
- Handling of the class imbalance (13/7/15).
