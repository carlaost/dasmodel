# Environment

> Grounding: abstract-only. Software stack is taken from the verified `sources.yaml` notes (which
> record the versions the implementation used). Everything not present in the abstract or
> `sources.yaml` is marked "Not available from provided input (no full text)" — the paper's full
> text was unavailable (the provided PDF is a different article; see PAPER.md).

- **Language/runtime**: Python (version not available from provided input).
- **Framework**: PyTorch 2.5.1; TIMM 1.0.15 (image-model library). Source: `sources.yaml` notes.
- **Explainability**: Saliency library — XRAI module. Source: `sources.yaml` notes.
- **Interface**: Gradio (web UI). Source: abstract + `sources.yaml` notes. Version not available from provided input.
- **Hardware**: Not available from provided input (no full text). Reported inference latency: sub-20 seconds (abstract) — deployment hardware unspecified.
- **Data sources**:
  - **Augmented Alzheimer MRI Dataset** (Kaggle, uploader: uraninjo).
    - Identifier: `kaggle.com/datasets/uraninjo/augmented-alzheimer-mri-dataset`
    - Repository: Kaggle
    - Access type: **open** (verified live, per `sources.yaml`)
    - Contents: T1/T2 axial 2D brain MRI slices in four dementia severity classes (MildDemented, ModerateDemented, NonDemented, VeryMildDemented); 33,984 augmented images + 6,400 original source images.
    - Role: training (augmented set) and evaluation (augmented test set + original set).
  - No other external dataset. Paper's Data Availability Statement reads verbatim: "Data contained within the article." (per `sources.yaml`).
- **Code location**: **None.** No code/software repository (GitHub/GitLab/Zenodo/OSF) is cited and there is no Code Availability statement (per `sources.yaml`). A bioRxiv preprint of the same work exists (DOI 10.1101/2025.08.16.670652) but surfaces no code link. No `src/execution/` stub is produced because no repo code and no printed pseudocode were available (Rule 14).
- **Key dependencies**: torch==2.5.1, timm==1.0.15, saliency (XRAI), gradio (versions beyond those listed not available from provided input).
- **Protocols**: Retrospective analysis of a public dataset. IRB and informed-consent statements are "Not applicable"; no clinical-trial (NCT) or PROSPERO registration (per `sources.yaml`).
- **Random seeds**: Not available from provided input (no full text).
