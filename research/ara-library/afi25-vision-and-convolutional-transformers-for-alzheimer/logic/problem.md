# Problem Specification

## Observations

### O1: AD is a large and escalating public-health and economic burden
- **Statement**: Prevalence rises sharply with age (~3% at 65–74, ~19% at 75–84, ~47% in those over 84); >55 million people live with dementia worldwide, projected to reach 139 million by mid-century; global annual dementia-care cost is ~US$1.3 trillion, projected to reach ~US$2.8 trillion by 2030.
- **Evidence**: §1 Introduction (page 1–2), citing [1–7].
- **Implication**: Earlier and more accurate diagnosis is a paramount objective, motivating advanced computational diagnostic tools.

### O2: Conventional AD diagnosis has intrinsic limitations
- **Statement**: Clinical evaluation + neuroimaging (sMRI, PET) + fluid biomarkers (CSF/blood) + genetics suffer from inter-observer variability, need for specialized equipment/expertise, and difficulty integrating heterogeneous modalities.
- **Evidence**: §1 (page 2), citing [9–17].
- **Implication**: A multimodal, automated approach is needed for holistic assessment.

### O3: Transformers (ViT/CViT) have emerged as powerful alternatives to CNNs
- **Statement**: ViTs use self-attention to capture both local and global dependencies; recognizing ViTs' data-hunger and computational cost, hybrid CViTs combine CNN local feature extraction with transformer global context.
- **Evidence**: §1, §4.4 (pages 2, 15–18).
- **Implication**: A focused synthesis of ViT/CViT applications in AD is warranted.

### O4: Prior reviews leave a conspicuous gap
- **Statement**: Existing surveys concentrate on pre-transformer (CNN/RNN) methods or evaluate models in isolation, with little emphasis on multimodal integration, algorithmic reproducibility, and implementation frameworks. Table 1 contrasts 8 prior reviews; none cover the full scope (ViTs + CViTs + fusion strategies + reproducibility + frameworks) that this review addresses.
- **Evidence**: §2 Related work (pages 3–5), Table 1.
- **Implication**: A systematic review dedicated to ViT/CViT in multimodal AD analysis is missing.

### O5: The reviewed literature reports very high but inconsistently validated accuracies
- **Statement**: Many reviewed studies report accuracies exceeding 95–99% on benchmark datasets, frequently without external validation on independent cohorts.
- **Evidence**: §7.3.3, §10.1, §12.1.3 (e.g. "accuracies exceeding 99% [195, 196]"); Tables 4, 5.
- **Implication**: High benchmark accuracy may not reflect clinical readiness ("accuracy paradox"); bias risk must be assessed.

## Gaps

### G1: No comprehensive, critical synthesis of ViT/CViT for AD + MCI progression
- **Statement**: A consolidated critical analysis of ViT and CViT models for AD classification AND MCI-to-AD progression prediction is absent from the literature.
- **Caused by**: O3, O4.
- **Existing attempts**: 8 prior reviews (Table 1) focused on earlier DL or partial scope.
- **Why they fail**: They predate or only touch upon transformer architectures and omit fusion/reproducibility/framework analysis.

### G2: MCI-to-AD progression prediction is underexplored
- **Statement**: The clinically vital prognostic task (pMCI vs sMCI) receives far less attention than AD-stage classification.
- **Caused by**: dataset/label availability; benchmark-centric incentives (O5).
- **Existing attempts**: Only a handful of the 68 studies address progression solely (e.g. [131], [166], [207]).
- **Why they fail**: Progression prediction is harder and less rewarded on leaderboard-style accuracy.

### G3: Multimodal fusion is underutilized and vaguely described
- **Statement**: A large portion of works still uses single-modality inputs; when multimodal, methods often default to simpler late fusion and omit alignment/normalization details.
- **Caused by**: data heterogeneity, missing multimodal datasets, reporting culture.
- **Existing attempts**: A minority employ deep intermediate/attention-based fusion.
- **Why they fail**: Lack of methodological transparency creates reproducibility risk.

### G4: Pervasive reproducibility gap and dataset bias
- **Statement**: Only ~15% of studies share code; the field over-relies on ADNI (demographically and technically homogeneous), and external validation is rare.
- **Caused by**: absence of code/data-sharing norms, benchmark-centric evaluation.
- **Existing attempts**: A small "Category 3" group performs rigorous external validation.
- **Why they fail**: Systemic incentives and infrastructure gaps persist.

### G5: LVM "largeness" is not truly harnessed
- **Statement**: Current AD work uses pretrained ViT/Swin backbones as feature extractors via transfer learning, not as true generalist multimodal foundation models with zero-shot reasoning.
- **Caused by**: small homogeneous datasets, supervised fine-tuning paradigm.
- **Existing attempts**: Transfer learning and domain-specific SSL (e.g. DINO).
- **Why they fail**: A conceptual/methodological gap remains between generalist medical AI and specialized fine-tuning-heavy AD work.

## Key Insight
- **Insight**: A rigorous, PRISMA-guided synthesis structured by four purpose-built taxonomies (architecture integration, fusion level, data modality, diagnostic objective) can simultaneously (a) reveal the decisive architectural shift from pure ViTs to hybrid CViTs, and (b) expose the practical, often-overlooked dimensions — reproducibility, frameworks, dataset bias, external-validation deficits, and the accuracy paradox — that separate high-performance modeling from clinical applicability.
- **Derived from**: O3, O4, O5.
- **Enables**: A uniquely holistic and practical assessment that maps current gaps to concrete future-research pathways and a conceptual next-generation LVM.

## Assumptions
- A1: Peer-reviewed journal publications (2021–2025) in five major databases adequately represent the field (conference papers, preprints, book chapters excluded).
- A2: Two independent reviewers with consensus adjudication adequately control selection bias.
- A3: Performance metrics as reported by primary studies are taken at face value for tabulation (the review does not re-run experiments), while critically annotating validation weaknesses.
- A4: The chosen taxonomies (fusion levels [47], integration patterns) are appropriate organizing frameworks for the field.
