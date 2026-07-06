# Concepts

> Grounding: abstract-only. Definitions of the paper's genuine technical terms. Standard-method
> definitions (STFT, CWT, ViT, transfer learning) are given generically because the paper's specific
> parameterizations are not available from provided input (no full text).

## Alzheimer's Disease (AD)
- **Notation**: —
- **Definition**: A progressive neurodegenerative disorder that significantly impairs cognitive function; the target condition the study aims to detect early.
- **Boundary conditions**: The study concerns *early* detection; the cohort also includes amnestic mild cognitive impairment (aMCI), a prodromal stage. Exact clinical inclusion criteria not available from provided input (no full text).
- **Related concepts**: Amnestic Mild Cognitive Impairment, Olfactory-evoked EEG.

## Amnestic Mild Cognitive Impairment (aMCI)
- **Notation**: —
- **Definition**: A prodromal cognitive-decline stage often preceding AD; present in the reused cohort (7 of 35 subjects).
- **Boundary conditions**: Whether aMCI subjects are labelled as AD, healthy, or a third class in this study is not available from provided input (no full text).
- **Related concepts**: Alzheimer's Disease.

## Olfactory-evoked EEG
- **Notation**: —
- **Definition**: EEG recorded while a subject is exposed to olfactory stimuli (odorants), capturing the brain's electrophysiological response to smell — used here as an AD biomarker because impaired olfaction correlates with early AD.
- **Boundary conditions**: In the reused dataset, evoked via a rose/lemon olfactory oddball paradigm.
- **Related concepts**: Olfactory Oddball Paradigm, EEG.

## Olfactory Oddball Paradigm
- **Notation**: —
- **Definition**: An experimental protocol presenting a stream of olfactory stimuli in which occasional deviant/target odors ("oddballs", e.g. rose vs lemon) are interspersed among standards, evoking a measurable EEG response.
- **Boundary conditions**: As used in the Sedghizadeh et al. Mendeley dataset (rose/lemon). Timing/trial parameters not available from provided input (no full text).
- **Related concepts**: Olfactory-evoked EEG.

## Short-Time Fourier Transform (STFT)
- **Notation**: $X(\tau,\omega)=\int x(t)\,w(t-\tau)\,e^{-j\omega t}\,dt$
- **Definition**: A time-frequency transform that applies the Fourier transform over sliding fixed-length windows, producing a spectrogram with uniform time-frequency resolution. One of two EEG-to-image transforms compared.
- **Boundary conditions**: Fixed window size fixes the time-frequency resolution trade-off; reported here as the weaker transform for patient-wise performance. Window/hop parameters not available from provided input (no full text).
- **Related concepts**: Continuous Wavelet Transform, Time-Frequency Representation.

## Continuous Wavelet Transform (CWT)
- **Notation**: $W(a,b)=\frac{1}{\sqrt{a}}\int x(t)\,\psi^{*}\!\left(\frac{t-b}{a}\right)dt$
- **Definition**: A time-frequency transform that correlates the signal with scaled/translated copies of a mother wavelet, giving multi-resolution (scale-dependent) time-frequency localization. The transform that gave the best patient-wise performance.
- **Boundary conditions**: Mother wavelet choice and scale range determine the output scalogram; those parameters are not available from provided input (no full text).
- **Related concepts**: Short-Time Fourier Transform, Time-Frequency Representation, Vision Transformer.

## Time-Frequency Representation (scalogram / spectrogram)
- **Notation**: —
- **Definition**: A 2-D image encoding how a signal's frequency content evolves over time; here EEG is converted into such images (STFT spectrograms, CWT scalograms) so image classifiers can be applied.
- **Boundary conditions**: Image dimensions, per-channel handling, and color mapping not available from provided input (no full text).
- **Related concepts**: STFT, CWT, Vision Transformer, Convolutional Neural Network.

## Vision Transformer (ViT)
- **Notation**: —
- **Definition**: A transformer-based image classifier that splits an image into patches, embeds them as a token sequence, and applies self-attention; here applied to CWT time-frequency images and achieving the best accuracy.
- **Boundary conditions**: Patch size, pretraining, and fine-tuning details not available from provided input (no full text).
- **Related concepts**: Time-Frequency Representation, Convolutional Neural Network, Transfer Learning.

## Transfer Learning (ResNet50 / VGG16)
- **Notation**: —
- **Definition**: Reusing a network pretrained on a large image corpus (e.g. ImageNet) and adapting it to the target task; instantiated here with ResNet50 and VGG16 backbones as CNN baselines.
- **Boundary conditions**: Which layers were frozen/fine-tuned and the pretraining source are not available from provided input (no full text).
- **Related concepts**: Convolutional Neural Network, Vision Transformer.

## CatBoost (gradient-boosted classifier on CNN features)
- **Notation**: —
- **Definition**: A gradient-boosting decision-tree classifier; used here on features from the custom CNN ("CNN paired with CatBoost") as a hybrid image-level classifier.
- **Boundary conditions**: Which CNN layer supplies features and CatBoost hyperparameters are not available from provided input (no full text).
- **Related concepts**: Convolutional Neural Network.
