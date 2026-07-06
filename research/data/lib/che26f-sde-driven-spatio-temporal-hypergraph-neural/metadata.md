# SDE-Driven Spatio-Temporal Hypergraph Neural Networks for Irregular Longitudinal fMRI Connectome Modeling in Alzheimer's Disease

- **Cite key**: Che26f
- **Authors**: Ruiying Chen; Yutong Wang; Houliang Zhou; Wei Liang; Yong Chen; Lifang He
- **Year**: 2026  (2026-03-20)
- **Journal**: 
- **DOI**: 
- **URL**: https://arxiv.org/abs/2603.20452
- **Citations**: 0 (0.0/yr)

## Abstract

Longitudinal neuroimaging is essential for modeling disease progression in Alzheimer's disease (AD), yet irregular sampling and missing visits pose substantial challenges for learning reliable temporal representations. To address this challenge, we propose SDE-HGNN, a stochastic differential equation (SDE)-driven spatio-temporal hypergraph neural network for irregular longitudinal fMRI connectome modeling. The framework first employs an SDE-based reconstruction module to recover continuous latent trajectories from irregular observations. Based on these reconstructed representations, dynamic hypergraphs are constructed to capture higher-order interactions among brain regions over time. To further model temporal evolution, hypergraph convolution parameters evolve through SDE-controlled recurrent dynamics conditioned on inter-scan intervals, enabling disease-stage-adaptive connectivity modeling. We also incorporate a sparsity-based importance learning mechanism to identify salient brain regions and discriminative connectivity patterns. Extensive experiments on the OASIS-3 and ADNI cohorts demonstrate consistent improvements over state-of-the-art graph and hypergraph baselines in AD progression prediction. The source code is available at https://anonymous.4open.science/r/SDE-HGNN-017F.
