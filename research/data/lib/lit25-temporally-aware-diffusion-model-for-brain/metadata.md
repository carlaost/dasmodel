# Temporally-Aware Diffusion Model for Brain Progression Modelling with Bidirectional Temporal Regularisation

- **Cite key**: Lit25
- **Authors**: Mattia Litrico; Francesco Guarnera; M. Giuffrida; Daniele Ravì; S. Battiato
- **Year**: 2025  (2025-09-03)
- **Journal**: Computerized medical imaging and graphics : the official journal of the Computerized Medical Imaging Society
- **DOI**: 10.48550/arXiv.2509.03141
- **URL**: https://doi.org/10.48550/arXiv.2509.03141
- **Citations**: 0 (0.0/yr)

## Abstract

Generating realistic MRIs to accurately predict future changes in the structure of brain is an invaluable tool for clinicians in assessing clinical outcomes and analysing the disease progression at the patient level. However, current existing methods present some limitations: (i) some approaches fail to explicitly capture the relationship between structural changes and time intervals, especially when trained on age-imbalanced datasets; (ii) others rely only on scan interpolation, which lack clinical utility, as they generate intermediate images between timepoints rather than future pathological progression; and (iii) most approaches rely on 2D slice-based architectures, thereby disregarding full 3D anatomical context, which is essential for accurate longitudinal predictions. We propose a 3D Temporally-Aware Diffusion Model (TADM-3D), which accurately predicts brain progression on MRI volumes. To better model the relationship between time interval and brain changes, TADM-3D uses a pre-trained Brain-Age Estimator (BAE) that guides the diffusion model in the generation of MRIs that accurately reflect the expected age difference between baseline and generated follow-up scans. Additionally, to further improve the temporal awareness of TADM-3D, we propose the Back-In-Time Regularisation (BITR), by training TADM-3D to predict bidirectionally from the baseline to follow-up (forward), as well as from the follow-up to baseline (backward). Although predicting past scans has limited clinical applications, this regularisation helps the model generate temporally more accurate scans. We train and evaluate TADM-3D on the OASIS-3 dataset, and we validate the generalisation performance on an external test set from the NACC dataset. The code is available at https://github.com/MattiaLitrico/TADM-3D.
