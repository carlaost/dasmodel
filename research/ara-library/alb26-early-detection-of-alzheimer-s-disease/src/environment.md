# Environment

> Grounding: abstract-only. No full text and no released code (`sources.yaml` `code: []`), so the
> software/hardware environment is largely **not available from provided input (no full text)**.
> Fields below record only what the abstract and the verified sources support.

- **Language/runtime**: Not available from provided input (no full text). (Deep-learning image
  pipeline; a Python + deep-learning stack is typical for ViT/CNN/CatBoost work but is not stated.)
- **Framework**: Not available from provided input (no full text). Models named: Vision Transformer,
  custom CNN, ResNet50, VGG16 (transfer learning), and CatBoost (gradient boosting).
- **Hardware**: Not available from provided input (no full text).
- **Data sources**:
  - **Olfactory-stimulation EEG dataset (MCI/AD)** — Sedghizadeh, Aghajan, Vahabi.
    - Repository: **Mendeley Data**
    - Identifier: **DOI 10.17632/sgzbgwjfkr.5**
    - Access: **open** (CC BY 4.0)
    - Cohort: 35 seniors (13 AD, 7 aMCI, 15 healthy); rose/lemon olfactory oddball paradigm.
    - Verified: yes (`sources.yaml`; via the paper's Semantic Scholar reference list). See
      `data/dataset.md`.
  - No other dataset, and **no clinical-trial registration** (`sources.yaml` `clinical_trials: []`).
- **Key dependencies**: Not available from provided input (no full text).
- **Protocols**: Retrospective computational analysis; transform (STFT/CWT) + deep classification
  pipeline (see `logic/solution/method.md`). Preprocessing/training protocol not available from
  provided input (no full text).
- **Random seeds**: Not available from provided input (no full text).
- **Code location**: None. No GitHub/GitLab/Zenodo/OSF repository is cited by the paper or
  discoverable via web search (`sources.yaml` `code: []`); expected for this applied study.
