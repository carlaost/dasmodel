# Limitations → Future Research Directions

Mirrors §12 and the roadmap diagram Fig. 44, which maps identified limitations (above the diagram)
to future research directions (below).

## The four future-research pathways (§12.2)

### Pathway 1 — Embrace longitudinal and multimodal complexity
- Move beyond sMRI volumetrics to functional (fMRI, EEG), molecular (advanced PET tracers), and microstructural (DTI) data.
- Deepen multimodal integration: genetics (GWAS, PRS), CSF biomarkers, plus unstructured data (exam videos, clinical-note text).
- Prioritize longitudinal modeling (temporal attention, RNNs, State-Space Models within CViTs) to shift from static classification to dynamic, personalized prognosis (building on [131, 292]).

### Pathway 2 — Next-generation architectures for integration and efficiency
- Lightweight/efficient transformers for clinical deployability: sparse attention, linear attention, quantization, knowledge distillation, token compression [31, 202].
- Integrate LLMs/LVMs via **modular** (not monolithic) frameworks — preserving component interpretability, tolerating missing modalities, and allowing independent updates/validation.

### Pathway 3 — From black boxes to integrated clinical partners via advanced XAI
- Holistic multimodal explanations that articulate cross-modal interactions (beyond single-modality saliency maps), for fusion models like MCAD [155] and 3MT [50].
- Clinician-centric interactivity: natural-language querying, "what-if" exploration.
- Evidence-based, verifiable reasoning via Retrieval-Augmented Generation (RAG) — linking predictions to clinical guidelines/landmark studies ("citing its sources").

### Pathway 4 — Build a robust and ethical research ecosystem
- Establish open benchmark platforms (fixed splits, standardized preprocessing, common eval; e.g. Clinica [243]) to mitigate data leakage and inconsistent reporting.
- Pioneer privacy-preserving distributed learning — innovate Federated Learning specifically for high-resolution imaging and large transformers (gradient compression, robust aggregation, split learning), respecting GDPR/HIPAA.
- Mandate fairness and bias audits across demographic subgroups (age, sex, ethnicity, socioeconomic status).

## Minimum reproducibility reporting standards (§9.4.1)
Proposed as publication minimums: (1) public code + trained model weights; (2) containerized
environment (Dockerfile capturing OS/framework/library versions); (3) explicit hyperparameters and
fixed random seeds; (4) fully documented/scripted preprocessing pipeline (software+version+parameters;
adherence to BIDS [239, 240]); (5) unambiguous subject-level data splits (exact IDs) to prevent
leakage and hidden stratification.

## Systemic solutions (§9.4.2)
- Open, standardized benchmark platforms (e.g. Clinica [243]).
- Cultural shift driven by journals/funders requiring code+data availability and rewarding replication studies.

## Two levels of reproducibility (§9.3)
- **Exact reproduction**: bit-for-bit identical results — rarely achievable given DL stochasticity and hardware/software variability; usually not the goal.
- **Close reproduction (replicability)**: consistent trends and statistically similar metrics — the practical, meaningful standard, yet still hard to meet given pervasive missing implementation detail.
