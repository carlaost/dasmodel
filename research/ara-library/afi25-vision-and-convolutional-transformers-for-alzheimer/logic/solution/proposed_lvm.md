# Conceptual Proposal — Next-Generation LVM for AD Assessment

The review's forward-looking design contribution (§11.3, Fig. 43). This is a *conceptual* architecture
(a diagram + prescriptive description), not an implemented or evaluated model — no code, weights, or
results exist. Mirrored from the Fig. 43 diagram; reflected here as the review's proposed method.

## Motivation
Current AD work uses pretrained ViT/Swin backbones as fine-tuned feature extractors (transfer
learning or domain-specific SSL), not as true generalist foundation models — leaving the "largeness"
of LVMs unharnessed (gap G5). The proposal aims for holistic, interpretable, predictive assessment.

## Proposed components (Fig. 43)
1. **Backbone**: a vision-language model (e.g. adapted from PaLI [286] or Flamingo [287]) so unstructured text (clinical notes, radiology reports) can be integrated alongside images.
2. **Hierarchical pretraining**:
   - Stage 1 — general foundational pretraining on massive general-domain image–text data (e.g. LAION-5B [288]).
   - Stage 2 — medical domain-specific pretraining on aggregated medical corpora (e.g. PubMedVision [274], GMAI-VL-5.5M [273]) via contrastive image–text alignment.
3. **Modality-specific input encoding/tokenization**:
   - Neuroimaging (3D sMRI, 3D PET): 3D-native ViT encoders or factorized spatio-temporal attention modeling inter-slice dependencies (building on ViT-TST [134]).
   - Tabular/textual (cognitive scores, demographics, APOE/PRS): projected into a shared embedding space as "non-image" tokens [49]; unstructured notes via the inherent language encoder.
4. **Advanced multimodal fusion transformer**:
   - Joint token-sequence processing: concatenate tokens from all modalities with modality-type + positional embeddings (AD-Transformer style [49]).
   - Hierarchical cross-modal attention: interleaved self-attention (within-modality) and cross-attention (across modalities), as in MCAD [155].
5. **Multi-task + RL fine-tuning**:
   - Supervised fine-tuning (SFT) on multiple simultaneous tasks (classification, prognosis, abnormality segmentation) with a multi-task loss (HAMMF-style [154]).
   - Reinforcement Learning with Clinical Feedback (RLCF), e.g. PPO [289], with an expert-designed reward that scores diagnostic accuracy, penalizes clinically-irrelevant hallucinations, and rewards localization to pathologically-relevant regions (Abnormal-Aware Rewarding, cf. UMed-LVLM [275]).

## Guiding synthesis (§11.2)
The proposal is framed as a shift from a data-centric to a methodology-centric paradigm, built on a
"synergistic triad": (a) high-quality curated multimodal data, (b) advanced training objectives
(e.g. RLCF) enforcing clinical reasoning/interpretability, and (c) true deep multimodal fusion.
Rigorous benchmark studies (Jeong et al. [276]) suggest plain Domain-Adaptive Pretraining (DAPT)
yields only marginal gains, motivating this more holistic approach.

## Status
Not implemented; not evaluated. No numbers are associated with this proposal (it is design-only).
