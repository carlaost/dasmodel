# Alzheimers Disease Progression Prediction Based on Manifold Mapping of Irregularly Sampled Longitudinal Data

- **Cite key**: Hon25
- **Authors**: Xin Hong; Ying Shi; Yinhao Li; Yen-Wei Chen
- **Year**: 2025  (2025-11-25)
- **Journal**: ArXiv
- **DOI**: 10.48550/arXiv.2511.20154
- **URL**: https://doi.org/10.48550/arXiv.2511.20154
- **Citations**: 0 (0.0/yr)

## Abstract

The uncertainty of clinical examinations frequently leads to irregular observation intervals in longitudinal imaging data, posing challenges for modeling disease progression.Most existing imaging-based disease prediction models operate in Euclidean space, which assumes a flat representation of data and fails to fully capture the intrinsic continuity and nonlinear geometric structure of irregularly sampled longitudinal images. To address the challenge of modeling Alzheimers disease (AD) progression from irregularly sampled longitudinal structural Magnetic Resonance Imaging (sMRI) data, we propose a Riemannian manifold mapping, a Time-aware manifold Neural ordinary differential equation, and an Attention-based riemannian Gated recurrent unit (R-TNAG) framework. Our approach first projects features extracted from high-dimensional sMRI into a manifold space to preserve the intrinsic geometry of disease progression. On this representation, a time-aware Neural Ordinary Differential Equation (TNODE) models the continuous evolution of latent states between observations, while an Attention-based Riemannian Gated Recurrent Unit (ARGRU) adaptively integrates historical and current information to handle irregular intervals. This joint design improves temporal consistency and yields robust AD trajectory prediction under irregular sampling.Experimental results demonstrate that the proposed method consistently outperforms state-of-the-art models in both disease status prediction and cognitive score regression. Ablation studies verify the contributions of each module, highlighting their complementary roles in enhancing predictive accuracy. Moreover, the model exhibits stable performance across varying sequence lengths and missing data rates, indicating strong temporal generalizability. Cross-dataset validation further confirms its robustness and applicability in diverse clinical settings.
