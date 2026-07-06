# Problem Specification

> Grounding: abstract-only. Observations and gaps are drawn from the abstract (`metadata.md`) and
> the verified discovery record (`sources.yaml`). Where the abstract does not supply detail, the
> field reads "Not available from provided input (no full text)".

## Observations

### O1: AD is a progressive neurodegenerative disorder with high healthcare burden
- **Statement**: Alzheimer's disease progressively impairs cognitive function and can strain global healthcare systems; early and accurate diagnosis is imperative for effective intervention.
- **Evidence**: Abstract (`metadata.md`), opening sentences.
- **Implication**: Motivates a reliable early-detection method.

### O2: EEG is a non-invasive window on AD-associated biomarkers
- **Statement**: Electroencephalography (EEG) is a non-invasive method for monitoring brain activity that can expose biomarkers useful for early AD detection.
- **Evidence**: Abstract (`metadata.md`).
- **Implication**: EEG is a viable, low-cost input modality for a screening pipeline.

### O3: Impaired olfaction correlates with early AD
- **Statement**: Recent studies report a significant correlation between an impaired sense of smell and the onset of early AD.
- **Evidence**: Abstract (`metadata.md`).
- **Implication**: Recording EEG *in response to olfactory stimuli* can surface a discriminative early biomarker, motivating an olfactory-evoked EEG paradigm.

### O4: A public olfactory-EEG cohort exists
- **Statement**: A public dataset records EEG during olfactory stimulation in mild cognitive impairment and AD patients — 35 seniors (13 AD, 7 aMCI, 15 healthy) under a rose/lemon olfactory oddball paradigm.
- **Evidence**: `sources.yaml` (data entry, DOI 10.17632/sgzbgwjfkr.5) / `metadata.md` "Discovered sources"; verified via the paper's Semantic Scholar reference list.
- **Implication**: Supplies the labelled cohort the study analyzes; also frames the small-sample constraint.

## Gaps

### G1: Practical deep-learning AD detection is blocked by data scarcity, poor generalization, and weak features
- **Statement**: Despite progress in AI/deep learning for neurodegenerative-disease diagnosis, scarce datasets, limited model generalization, and suboptimal feature extraction hinder practical AD detection.
- **Caused by**: O1, O2 (need for a deployable method) combined with the small-cohort reality of O4.
- **Existing attempts**: Deep-learning models applied to EEG for neurodegenerative diagnosis (general prior art; specific baselines not available from provided input — no full text).
- **Why they fail**: Datasets too small to generalize; feature extraction from raw EEG is suboptimal. (Exact failure analysis not available from provided input — no full text.)

### G2: The best EEG-to-image transform + classifier pairing for olfactory-evoked AD detection is unknown
- **Statement**: It is unclear which time-frequency transform (STFT vs CWT) and which deep classifier (custom CNN, CNN+CatBoost, ResNet50, VGG16, ViT) best convert olfactory-evoked EEG into an accurate AD diagnosis, and at which evaluation granularity (image vs patient).
- **Caused by**: G1, O3.
- **Existing attempts**: Not available from provided input (no full text).
- **Why they fail**: Not available from provided input (no full text).

## Key Insight
- **Insight**: Pair the olfaction–AD biomarker (EEG evoked by smell) with a strong time-frequency image representation (CWT) and a Vision Transformer classifier; CWT-based images processed by a ViT deliver the strongest patient-level diagnosis.
- **Derived from**: O2, O3, O4.
- **Enables**: A pipeline that transforms olfactory-evoked EEG into time-frequency images and classifies them, evaluated at both image and patient level.

## Assumptions
- A1: EEG responses to olfactory stimuli carry class-discriminative information for early AD.
- A2: Time-frequency image representations (STFT/CWT) preserve the discriminative EEG structure for image-based deep classifiers.
- A3: The public olfactory-EEG cohort is representative enough to train/evaluate the models. (Exact splits/validation protocol not available from provided input — no full text.)
