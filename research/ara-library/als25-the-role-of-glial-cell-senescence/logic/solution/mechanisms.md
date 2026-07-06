# Synthesized Mechanistic Model: Glial Senescence → Alzheimer's Disease

*Grounding: full-text. This is the review's core "method" — the mechanistic framework it assembles.
Structure mirrors Figures 1 and 2 and §1.1–§1.3. No original data; all steps are attributed to
cited primary studies within the review.*

## Overview

The review builds a causal loop in which aging/pathology stressors drive glial senescence, whose
SASP and functional deficits produce chronic neuroinflammation, impaired Aβ/tau clearance,
demyelination, and neurodegeneration — which in turn amplify the stressors, reinforcing senescence
through positive feedback. Figure 1 depicts the general senescence program; Figure 2 depicts its
AD-specific consequences.

## Stage 1 — Triggers of senescence (upstream)

Stressors that initiate cellular senescence (Figure 1; §1 Introduction):
- Mitochondrial dysfunction → increased ROS → oxidative stress
- Telomere shortening / erosion → replicative senescence
- Oncogene activation
- DNA damage (double-strand breaks, telomeric alterations)
- Oxidative stress

These converge on the **DNA damage response (DDR)**: persistent/irreparable damage keeps DDR
chronically active, enforcing permanent cell-cycle arrest via **p53 → p21WAF1/CIP1** and/or via
**p16INK4A** upregulation. **GATA4** provides a parallel, ATR/ATM-dependent but p53/p16-independent
route to NF-κB and SASP.

## Stage 2 — The senescent phenotype (state)

A senescent glial cell exhibits (Tables 1, 2):
- Permanent growth arrest (↑ p16INK4A, ↑ p21WAF1/CIP1, ↑ p53, ↓ Ki-67)
- DNA-damage / chromatin markers (↑ γH2AX, ↑ SAHF, ↓ Lamin B1, HMGB1 release)
- Metabolic shift (↑ SA-β-gal, ↑ oxidative stress, ↑ lipofuscin, altered lipid/iron metabolism)
- Resistance to apoptosis (↑ BCL-2 / BCL-xL dependence)
- **SASP** secretion (IL-1β, IL-6, IL-8, TNF-α, INF-γ, MMPs, NOS2, PAI-1, HMGB1, RAGE-related, TGF-β)

## Stage 3 — Cell-type-specific consequences in AD (Figure 2)

### Astrocytes (§1.2.1)
- Lose glutamate/ion homeostasis and synaptic support → excitotoxicity, reduced synaptic vesicle pool, reduced neurotrophic factors (IGF-1, NGF).
- Reduced Aβ-uptake receptors (LRP1, SR-B1) → impaired Aβ degradation; reactive astrocytes show ↑ β-/γ-secretase (may add to amyloid load).
- Aβ and tau induce astrocyte senescence; >75% of GFAP+ astrocytes in AD are TauO- and p16INK4A-reactive (Gaikwad 2021).

### Microglia (§1.2.2)
- Pathology-driven rapid proliferation around plaques → **replicative senescence**; senescent microglia = disease-associated microglia (DAM) / plaque-associated microglia (PAM).
- Reduced phagocytosis of Aβ and tau → prolonged activation → chronic neuroinflammation.
- Aβ and tau induce microglial senescence (↑ p16/p21, SASP, γH2AX; ↓ Lamin B1).

### Oligodendrocytes / OPCs (§1.2.3)
- Senescent OPCs lose differentiation capacity → **remyelination failure**; mature-oligodendrocyte myelin loss → impaired axonal conduction and memory.
- SASP from senescent microglia/astrocytes (and astrocyte-released HMGB1) further induces OPC senescence.
- Post-mitotic mature oligodendrocytes senesce via division-independent routes (ROS from high myelin metabolic demand, limited antioxidant defense, chronic inflammation, NF-κB).

## Stage 4 — Feedback loops (self-reinforcement)

- **SASP → neighboring-cell senescence** (inflammaging): senescent glia propagate senescence to nearby cells (Schafer 2020).
- **Aβ/tau ⇄ senescence**: Aβ and tau induce senescence; senescent glia fail to clear Aβ/tau and can seed Aβ, accelerating aggregation (Frost & Li 2017; Parhizkar 2019).
- **Mitochondrial dysfunction ⇄ senescence**: ROS drives DNA damage → senescence; senescence impairs mitochondrial function → more ROS (Miwa 2022).
- **Chronic neuroinflammation ⇄ glial senescence**: neuroinflammation promotes senescence, which sustains neuroinflammation.

Net output: cognitive decline and neuronal loss — the hallmarks of AD.

## Method status
This is a **synthesized narrative model**, not a formally specified algorithm. It is supported by
convergent primary evidence (marker studies, in vitro induction, clearance/rescue experiments) but
retains open mechanistic gaps (see `constraints.md` and `problem.md` G1–G4).
