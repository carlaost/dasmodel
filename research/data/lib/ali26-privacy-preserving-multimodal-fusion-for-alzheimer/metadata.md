# Privacy-preserving multimodal fusion for Alzheimer's staging: A federated vision transformer framework with explainable AI

- **Cite key**: Ali26
- **Authors**: Marwa Ben Gara Ali; A. Smiti
- **Year**: 2026  (2026-02-19)
- **Journal**: Computerized medical imaging and graphics : the official journal of the Computerized Medical Imaging Society
- **DOI**: 10.1016/j.compmedimag.2026.102730
- **URL**: https://doi.org/10.1016/j.compmedimag.2026.102730
- **Citations**: 0 (0.0/yr)

## Abstract

Accurate, early-stage staging of Alzheimer's disease (AD) is critical for therapeutic intervention but is hampered by data privacy regulations, multimodal data heterogeneity, and the "black-box" nature of complex Artificial Intelligence (AI) models. To address these interconnected challenges, we introduce a novel, privacy-preserving federated learning framework for robust and interpretable AD staging. Our method integrates four clinically relevant modalities, 3D structural Magnetic Resonance Imaging (MRI), Image Biomarker Standardization Initiative (IBSI)-compliant radiomics, cognitive assessments, and U.S. Food and Drug Administration (FDA) cleared plasma biomarkers, within a parameter-efficient Swin-UNet transformer architecture. Key innovations include: (1) Low-Rank Adaptation (LoRA) and dynamic token gating, reducing communication overhead by 99% (to 140 KB/round) compared to standard federated averaging; (2) A hierarchical attention fusion mechanism that dynamically weights modalities based on predictive uncertainty; and (3) A fuzzy-rough hybrid explainability pipeline that synthesizes client-specific saliency maps into a consensus-driven, clinically coherent interpretation without sharing raw data. Evaluated on a stratified four-client federation derived from the Alzheimer's Disease Neuroimaging Initiative (ADNI) cohort, our framework achieved a state-of-the-art balanced accuracy of 80.7%, closely approaching the centralized upper bound (82.1%) while demonstrating superior robustness to simulated domain shifts and consistent cross-site interpretability (Dice similarity: 0.84). This work establishes a foundational blueprint for the next generation of healthcare AI systems that are simultaneously accurate, efficient, privacy-preserving, and trustworthy, enabling scalable collaboration across distributed clinical networks.

## Discovered sources

- **PDF / OA:** Closed access. Unpaywall (`oa_status: closed`, no OA locations) and Europe PMC ("Subscription required", `inPMC: N`) confirm no licit open-access copy. No PDF downloaded. Best publisher URL: https://linkinghub.elsevier.com/retrieve/pii/S0895611126000339 (PII S0895-6111(26)00033-9). PMID 41723900.
- **Code:** None found. No repository (GitHub/GitLab/Zenodo/OSF) located via web search. A GitHub user `marwabentaleb` appeared but is a different person (Marwa BEN TALEB ALI) with unrelated repos — not this paper's code.
- **Data:** Alzheimer's Disease Neuroimaging Initiative (ADNI) cohort — a stratified four-client federation derived from ADNI. Access is controlled/request-based via the LONI Image and Data Archive (adni.loni.usc.edu). No new datasets or accessions released by the authors.
- **Clinical trials:** None. This is a methods/imaging-AI paper (federated Swin-UNet transformer for AD staging), not a trial, and it cites no NCT registration.
- **Data/code availability statement:** No explicit Data Availability or Code Availability statement found in the available metadata (Elsevier landing, Europe PMC core record, PubMed).
- **Authors/affiliation:** Marwa Ben Gara Ali; Abir Smiti — LARODEC, Higher Institute of Management of Tunis, University of Tunis, Tunisia.
