# An Explainable Web-Based Diagnostic System for Alzheimer’s Disease Using XRAI and Deep Learning on Brain MRI

- **Cite key**: Aks25
- **Authors**: Serra Aksoy; Arij Daou
- **Year**: 2025  (2025-08-21)
- **Journal**: Diagnostics
- **DOI**: 10.3390/diagnostics15202559
- **URL**: https://doi.org/10.3390/diagnostics15202559
- **Citations**: 1 (1.1/yr)

## Abstract

Background Alzheimer’s disease (AD) is a progressive neurodegenerative condition marked by cognitive decline and memory loss. Despite advancements in AI-driven neu-roimaging analysis for AD detection, clinical deployment remains limited due to chal-lenges in model interpretability and usability. Explainable AI (XAI) frameworks such as XRAI offer potential to bridge this gap by providing clinically meaningful visualizations of model decision-making. Methods: This study developed a comprehensive, clinically deployable AI system for AD severity classification using 2D brain MRI data. Three deep learning architectures MobileNet-V3 Large, EfficientNet-B4, and ResNet-50 were trained on an augmented Kaggle dataset (33,984 images across four AD severity classes). The models were evaluated on both augmented and original datasets, with integrated XRAI explainability providing region-based attribution maps. A web-based clinical interface was built using Gradio to deliver real-time predictions and visual explanations. Results: MobileNet-V3 achieved the highest accuracy (99.18% on the augmented test set; 99.47% on the original dataset), while using the fewest parameters (4.2M), confirming its effi-ciency and suitability for clinical use. XRAI visualizations aligned with known neuroana-tomical patterns of AD progression, enhancing clinical interpretability. The web interface delivered sub-20 second inference with high classification confidence across all AD sever-ity levels, successfully supporting real-world diagnostic workflows. Conclusion: This re-search presents the first systematic integration of XRAI into AD severity classification us-ing MRI and deep learning. The MobileNet-V3-based system offers high accuracy, com-putational efficiency, and interpretability through a user-friendly clinical interface. These contributions demonstrate a practical pathway toward real-world adoption of explainable AI for early and accurate Alzheimer’s disease detection.

## Discovered sources

- **PDF**: Open access (gold, CC BY). Downloaded to `paper.pdf` from Europe PMC render endpoint (https://europepmc.org/articles/PMC12564920?pdf=render). PMID 41153232, PMCID PMC12564920. Unpaywall best OA location was the MDPI PDF (https://www.mdpi.com/2075-4418/15/20/2559/pdf), but MDPI and PMC direct PDF endpoints returned 403/HTML to curl.
- **Code**: None found. No code/software repository is cited and there is no Code Availability statement, despite use of PyTorch 2.5.1, TIMM 1.0.15, the Saliency library XRAI module, and Gradio. Web search surfaced no author repo. (A matching bioRxiv preprint exists: doi 10.1101/2025.08.16.670652, no code link.)
- **Data**: One external dataset, cited as ref [12] — Kaggle "Augmented Alzheimer MRI Dataset" by uraninjo (https://www.kaggle.com/datasets/uraninjo/augmented-alzheimer-mri-dataset), open access. T1/T2 axial 2D brain MRI slices in 4 dementia severity classes; 33,984 augmented + 6,400 original images. Verified via paper citation and live Kaggle page. Paper's Data Availability Statement: "Data contained within the article."
- **Clinical trials**: None. Retrospective analysis of a public dataset; IRB and informed consent statements are "Not applicable"; no NCT/PROSPERO registration.
