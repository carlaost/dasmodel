# Claims

> Grounding: abstract-only. Every numeric value below is copied verbatim from the abstract in
> `metadata.md` (line 13) — the only quantitative source available. No full text, so no evidence
> tables/figures were extracted; `Proof` points to directional experiment plans (E01–E04), and the
> underlying numbers are cited here against the abstract text. Numbers are reproduced exactly, never
> rounded.

## C01: CWT + Vision Transformer gives the highest patient-level accuracy
- **Statement**: Using CWT time-frequency images, a Vision Transformer (ViT) achieves 91.43% diagnostic accuracy at the patient level — the best patient-level result reported.
- **Status**: supported
- **Falsification criteria**: A reported patient-level accuracy for CWT+ViT that differs from 91.43%, or another model/transform configuration in the paper exceeding it at the patient level.
- **Proof**: [E01, E03]
- **Evidence basis**: The abstract states patient-wise performance was highest using CWT and that the ViT "produced the best diagnostic accuracy (91.43% at the patient level ...)".
- **Interpretation**: Suggests patient-level aggregation of CWT+ViT predictions is the most clinically relevant configuration among those tried; full per-model patient-level table not available from provided input (no full text).
- **Sources**: 91.43% ← `metadata.md`:13 «the Vision Transformer (ViT) produced the best diagnostic accuracy (91.43% at the patient level and 85.18% at the image level)» [result]; "patient-wise highest using CWT" ← `metadata.md`:13 «patient-wise performance was highest using the CWT» [result]
- **Dependencies**: C03
- **Tags**: vision-transformer, CWT, patient-level, accuracy, best-result

## C02: CWT + Vision Transformer gives the highest image-level accuracy, above all CNN baselines
- **Statement**: Using CWT images, the ViT reaches 85.18% image-level accuracy, exceeding the image-level accuracies of CNN+CatBoost (81.66%), the custom CNN (81.25%), ResNet50 transfer learning (80.69%), and VGG16 (79.82%).
- **Status**: supported
- **Falsification criteria**: Any of the quoted image-level accuracies differing from the stated values, or a CNN-family model exceeding 85.18% at the image level.
- **Proof**: [E01, E02]
- **Evidence basis**: The abstract reports "85.18% at the image level" for ViT and, for image-level evaluation, 81.66% (CNN+CatBoost), 81.25% (CNN), 80.69% (ResNet50), 79.82% (VGG16).
- **Interpretation**: ViT's advantage over CNN-family models holds at image granularity as well as patient granularity; whether the gap is statistically significant is not available from provided input (no full text).
- **Sources**: 85.18% ← `metadata.md`:13 «91.43% at the patient level and 85.18% at the image level» [result]; 81.66% ← `metadata.md`:13 «custom Convolutional Neural Network (CNN) paired with CatBoost achieved 81.66% accuracy» [result]; 81.25% ← `metadata.md`:13 «the CNN reached 81.25%» [result]; 80.69% ← `metadata.md`:13 «transfer learning with ResNet50 yielded 80.69%» [result]; 79.82% ← `metadata.md`:13 «VGG16 attained 79.82%» [result]
- **Dependencies**: C03
- **Tags**: vision-transformer, image-level, accuracy, baselines, CNN, ResNet50, VGG16, CatBoost

## C03: CWT is the superior EEG-to-image transform for patient-wise performance
- **Statement**: Continuous Wavelet Transform (CWT) images yield higher patient-wise classification performance than Short-Time Fourier Transform (STFT) images for this olfactory-EEG AD-detection task.
- **Status**: supported
- **Falsification criteria**: A reported patient-wise result in which STFT matches or exceeds CWT for the same classifier.
- **Proof**: [E03]
- **Evidence basis**: The abstract states "patient-wise performance was highest using the CWT"; STFT and CWT are the two transforms compared.
- **Interpretation**: CWT's multi-resolution time-frequency localization appears better suited to olfactory-evoked EEG than STFT's fixed-window analysis; per-transform numeric comparison not available from provided input (no full text).
- **Sources**: "highest using CWT" ← `metadata.md`:13 «patient-wise performance was highest using the CWT» [result]; transforms compared ← `metadata.md`:13 «signal transformation techniques, such as the Short-Time Fourier Transform (STFT) and Continuous Wavelet Transform (CWT)» [input]
- **Dependencies**: none
- **Tags**: CWT, STFT, transform-comparison, time-frequency, patient-level

## C04: Olfactory-evoked EEG is a usable biomarker for early AD detection via deep learning
- **Statement**: EEG signals generated in response to olfactory stimuli can be leveraged as a biomarker to classify early AD with deep-learning models, motivated by the reported correlation between impaired smell and early AD onset.
- **Status**: supported
- **Falsification criteria**: Classification accuracy on olfactory-evoked EEG no better than chance / a resting-state baseline (would refute the biomarker's usefulness).
- **Proof**: [E01, E04]
- **Evidence basis**: The abstract motivates the approach by the smell–AD correlation and reports above-chance multi-model accuracies (79.82%–91.43%) on olfactory-evoked EEG.
- **Interpretation**: Supports olfactory-evoked EEG as a candidate early-screening signal; generalization beyond this 35-subject cohort is not available from provided input (no full text).
- **Sources**: smell–AD link ← `metadata.md`:13 «a significant correlation between an impaired sense of smell and the onset of early AD» [input]; olfactory-evoked EEG approach ← `metadata.md`:13 «Our approach analyzes EEG signals generated in response to olfactory stimuli to leverage this biomarker» [input]
- **Dependencies**: C01, C02
- **Tags**: olfactory-stimuli, biomarker, EEG, early-detection

## C05: A single olfactory-EEG cohort (35 seniors) underlies the study
- **Statement**: The study analyzes a public olfactory-EEG cohort of 35 seniors — 13 AD, 7 aMCI, 15 healthy — recorded under a rose/lemon olfactory oddball paradigm (Mendeley Data, DOI 10.17632/sgzbgwjfkr.5).
- **Status**: supported
- **Falsification criteria**: The paper's methods section reporting a different dataset, cohort size, or class breakdown than stated.
- **Proof**: [E04]
- **Evidence basis**: The verified discovery record identifies this reused dataset and cohort via the paper's Semantic Scholar reference list; the abstract's methodology (olfactory-stimulus EEG) matches.
- **Interpretation**: The small, single-site cohort bounds the strength of all accuracy claims (see constraints.md); whether aMCI is grouped with AD or excluded is not available from provided input (no full text).
- **Sources**: 35 seniors / 13 AD / 7 aMCI / 15 healthy ← `sources.yaml`:16-20 & `metadata.md`:19 «Cohort: 35 seniors (13 AD, 7 aMCI, 15 healthy), rose/lemon olfactory oddball paradigm» [input]; DOI ← `sources.yaml`:17 «identifier: 10.17632/sgzbgwjfkr.5» [input]
- **Dependencies**: none
- **Tags**: dataset, cohort, olfactory-oddball, Mendeley, aMCI
