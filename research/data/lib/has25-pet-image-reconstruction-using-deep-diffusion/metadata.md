# PET Image Reconstruction Using Deep Diffusion Image Prior

- **Cite key**: Has25
- **Authors**: F. Hashimoto; K. Gong
- **Year**: 2025  (2025-07-20)
- **Journal**: IEEE transactions on medical imaging
- **DOI**: 10.1109/TMI.2026.3659792
- **URL**: https://doi.org/10.1109/TMI.2026.3659792
- **Citations**: 5 (5.2/yr)

## Abstract

Diffusion models have shown great promise in medical image denoising and reconstruction, but their application to Positron Emission Tomography (PET) imaging remains limited by tracer-specific contrast variability and high computational demands. In this work, we proposed an anatomical prior–guided PET image reconstruction method based on diffusion models, inspired by the deep diffusion image prior (DDIP) framework. The proposed method alternated between diffusion sampling and model fine-tuning guided by the PET sinogram, enabling the reconstruction of high-quality images from various PET tracers using a score function pretrained on a dataset of another tracer. To improve computational efficiency, the half-quadratic splitting (HQS) algorithm was adopted to decouple network optimization from iterative PET reconstruction. The proposed method was evaluated using one simulation and two clinical datasets. For the simulation study, a model pretrained on [<inline-formula> <tex-math notation="LaTeX">${}^{{18}}\text {F}$ </tex-math></inline-formula>]FDG data was tested on [<inline-formula> <tex-math notation="LaTeX">${}^{{18}}\text {F}$ </tex-math></inline-formula>]FDG data and amyloid-negative PET data to assess out-of-distribution (OOD) performance. For the clinical-data validation, ten low-dose [<inline-formula> <tex-math notation="LaTeX">${}^{{18}}\text {F}$ </tex-math></inline-formula>]FDG datasets and one [<inline-formula> <tex-math notation="LaTeX">${}^{{18}}\text {F}$ </tex-math></inline-formula>]Florbetapir dataset were tested on a model pretrained on data from another tracer. Experiment results show that the proposed PET reconstruction method can generalize robustly across tracer distributions and scanner types, providing an efficient and versatile reconstruction framework for low-dose PET imaging.
