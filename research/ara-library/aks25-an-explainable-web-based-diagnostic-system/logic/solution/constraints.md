# Constraints, Assumptions & Limitations

> Grounding: abstract-only. The provided PDF is a different paper (see PAPER.md), so limitations
> stated in the paper's own Discussion/Limitations section were NOT available. Items below are
> derived from the abstract and the verified dataset record; the compile's own grounding
> limitation is stated explicitly.

## Boundary conditions
- **Modality**: 2D brain MRI slices only (T1/T2 axial, per `sources.yaml`) — not 3D volumes, not multimodal (no PET/CSF/clinical data).
- **Task**: Four-class AD severity classification (NonDemented, VeryMildDemented, MildDemented, ModerateDemented).
- **Data source**: A single public Kaggle dataset (uraninjo). No external clinical cohort was used.
- **Deployment**: Web-based Gradio interface with sub-20-second inference target.

## Assumptions
- A1: 2D slices carry enough signal for four-class severity classification.
- A2: Performance on the augmented dataset transfers to the original (non-augmented) data and to clinical use.
- A3: XRAI attribution overlapping known AD neuroanatomy indicates clinically trustworthy decisions.
- A4: Sub-20-second inference is adequate for real-world diagnostic workflows.

## Known limitations
- **L1 (compile-level, grounding)**: This ARA is abstract-only. The provided `paper.pdf` contained a different article (Afifi et al., Brain Informatics 2026, DOI 10.1186/s40708-025-00286-7), so no verified full text of Aks25 was available. Method details, quantitative results tables, figures, ablations, and the authors' own stated limitations could not be captured. Downstream agents must not treat absent detail as evidence of absence.
- **L2 (dataset provenance)**: The Kaggle dataset is pre-augmented by a third party (uraninjo); augmentation procedure and the relationship between augmented and original images are outside the paper's control. Class balance across the four severity classes is not available from provided input.
- **L3 (generalization)**: Only a single public dataset was used; external multi-site validation is not evidenced in the abstract. Reported ≥99% accuracy on the same data family risks optimistic estimates relative to independent clinical data.
- **L4 (explainability evaluation)**: XRAI alignment with AD neuroanatomy is described qualitatively in the abstract; no quantitative overlap metric or reader study is evidenced from the provided input.
- **L5 (reproducibility)**: No code repository or code-availability statement exists (per `sources.yaml`), despite the implementation using PyTorch 2.5.1, TIMM 1.0.15, the Saliency XRAI module, and Gradio. Exact hyperparameters, seeds, train/val/test splits, and hardware are not available from provided input.
