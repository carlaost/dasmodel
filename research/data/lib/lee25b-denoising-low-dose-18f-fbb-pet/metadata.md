# Denoising Low-Dose 18F-FBB PET Using Flow Matching with Multimodal Prior Guidance

- **Cite key**: Lee25b
- **Authors**: J.H. Lee; Y.J. Seol; J. Lee
- **Year**: 2025  (2025-11-01)
- **Journal**: 2025 IEEE Nuclear Science Symposium (NSS), Medical Imaging Conference (MIC) and Room Temperature Semiconductor Detector Conference (RTSD)
- **DOI**: 10.1109/NSS/MIC/RTSD57106.2025.11287264
- **URL**: https://doi.org/10.1109/NSS/MIC/RTSD57106.2025.11287264
- **Citations**: 0 (0.0/yr)

## Abstract

18F-florbetaben (FBB) PET is a radiopharmaceutical used to visualize amyloid-β plaque distribution in the brain for the diagnosis of Alzheimer's disease. While low-dose PET imaging is employed to reduce scan time and radiation exposure, it often suffers from significant image degradation due to increased noise levels. This degradation poses challenges for clinical interpretation, particularly given FBB's inherently low uptake and the limited availability of corresponding datasets compared to 18F-fluorodeoxyglucose (FDG). Recent advances in deep learning have enabled the application of generative models for PET denoising. However, conventional models often suffer from image blurring and prolonged sampling times. In this study, we investigate Flow Matching (FM), a generative framework that learns continuous velocity fields between low-dose and normal-dose PET distributions. FM leverages optimal transport theory to enable deterministic and efficient sampling without iterative denoising procedures. To further enhance denoising performance, we incorporate anatomical priors from co-registered CT and MR images to guide the FM process. We conduct experiments using paired low-dose and normal-dose FBB PET datasets to evaluate our method. The results demonstrate that FM, when combined with multimodal priors, improves both quantitative accuracy and visual quality, particularly in lowuptake regions, outperforming existing denoising approaches.
