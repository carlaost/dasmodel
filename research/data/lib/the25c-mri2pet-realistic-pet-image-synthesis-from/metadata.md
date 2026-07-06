# MRI2PET: Realistic PET Image Synthesis from MRI for Automated Inference of Brain Atrophy and Alzheimer’s

- **Cite key**: The25c
- **Authors**: Brandon Theodorou; Anant Dadu; B. Avants; Mike A. Nalls; Jimeng Sun; F. Faghri
- **Year**: 2025  (2025-04-25)
- **Journal**: medRxiv
- **DOI**: 10.1101/2025.04.23.25326302
- **URL**: https://doi.org/10.1101/2025.04.23.25326302
- **Citations**: 5 (4.2/yr)

## Abstract

Background: Positron Emission Tomography (PET) scans are a crucial tool in the diagnosing and monitoring of a number of complex conditions, including cancer, heart health, and especially cognitive brain function. However, they are also often much more expensive than comparable imaging modalities such as X-Ray and magnetic resonance imaging (MRI), which can limit their availability and the impact of their use in both medical and machine learning settings. We propose to address this problem by using generative models to simulate the PET scan results based on prior MRI. Methods: While recent work has yielded impressive realism in image generation, this PET synthesis task presents a series of technical challenges based on the scarcity of paired data as well as the complexity and nuance of the 3D images. So, we propose MRI2PET to generate AV45-PET scans from T1-weighted MRI images. MRI2PET is a 3D diffusion-based method which makes use of style transferred pre-training and a Laplacian pyramid loss to address these challenges by utilizing larger available unpaired MRI datasets and structural similarities between the MRI and PET images while simultaneously emphasizing the crucial details. Findings: We evaluate MRI2PET through a series of studies on the ADNI dataset where we show that it both generates realistic images and improves clinically-based disease classification. When compared to training on only the original AV45-PET data, MRI2PET augmentation increases AUROC of brain scan classification to 0.780 {+/-} 0.005 from 0.688 {+/-} 0.014 when classifying brain scans into one of three clinically defined groups: cognitively normal, mild cognitive impairment, and Alzheimer's Disease. Interpretation The capability to generate high quality, clinically relevant PET scans from MRI has the potential to expand the utility of cost-effective and accessible imaging workflows and improve both image-based machine learning capabilities and patient care.
