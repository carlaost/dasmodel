# Open Challenges and Future Directions

Grounded in "Open Challenges" (PDF p.645-646), "Future Directions" (p.646-647), and Figures 4 and 8.

## Open challenges
1. **Dataset dependence remains strong.** Overreliance on a few public benchmarks (especially ADNI)
   reduces confidence in real-world generalization (Alsubaie et al., 2024).
2. **Class imbalance and task inconsistency remain widespread.** The literature mixes easier and
   harder tasks and reports different diagnostic categories/evaluation protocols, making direct
   comparison unreliable (Qiu et al., 2022).
3. **Clinical translation remains limited.** High experimental performance does not guarantee routine
   usefulness unless models handle missing modalities, scanner variation, uncertainty, and
   heterogeneous populations (Castellano et al., 2024; Qiu et al., 2022).
4. **Interpretability still lacks standardized evaluation.** Many studies claim explainability, but
   few define how explanation quality should be measured or validated with domain experts (Hu et al.,
   2024).

## Future directions (Figure 8 roadmap)
1. **External validation across institutions and scanners** should become routine (Qiu et al., 2022).
2. **Robust multimodal integration** should expand beyond MRI + PET to cognitive scores, blood
   biomarkers, genomics, longitudinal histories, and clinical text, with principled handling of
   missing data (Golovanevsky et al., 2022; Qiu et al., 2022).
3. **Longitudinal and prognostic modeling** deserves greater emphasis because AD is progressive and
   static single-time-point diagnosis captures only part of the clinical problem (Lu et al., 2018).
4. **Rigorous explainability**: evaluate stability, anatomical plausibility, cross-cohort consistency,
   and usefulness to clinicians; architecture-level (self-explainable) explainability is especially
   promising (Hu et al., 2024).
5. **Reproducibility and open benchmarking**: stronger reporting standards, code availability,
   preprocessing transparency, and fair comparison frameworks (Alsubaie et al., 2024).

## Roadmap framing (Figure 8)
The "Next-Generation Alzheimer's Disease Diagnosis Systems" are framed around eight coordinated
directions: External Validation ("multi-center testing"), Longitudinal Modeling ("disease progression
prediction"), Trustworthy AI & Uncertainty Estimation ("reliable and safe decision support"), Robust
Multimodal Fusion ("MRI, PET, biomarkers, cognition"), Clinical Deployment ("workflow integration and
usability"), Missing Modality Handling ("incomplete real-world records"), Reproducibility & Open
Benchmarking ("transparent pipelines and fair comparisons"), and Explainability Evaluation ("stable
and clinically meaningful explanations").
