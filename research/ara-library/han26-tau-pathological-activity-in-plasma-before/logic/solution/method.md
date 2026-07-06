# Method: VeraBIND Tau Assay

This mirrors the structure of Figure 1 (`evidence/figures/figure1.md`), a diagram of the assay's reaction pipeline, plus the narrative protocol description in Methods (PDF p.9–11).

## Principle
The VeraBIND Tau assay is a functional (activity-based), not purely quantitative, immunoassay. Rather than reporting the concentration of tau phosphorylated at a specific residue, it purifies hyperphosphorylated tau (pTau) from plasma and directly tests whether that purified pTau is "pathologically active" — i.e., capable of binding to and templating recombinant normal tau, mimicking the prion-like seeding behavior of pathological tau aggregates in the AD brain (Introduction, PDF p.6–7; concept "PA pTau / Tau Seeding Activity" in `logic/concepts.md`).

## Reaction Pipeline (mirrors Figure 1 diagram)
1. **Conditioned and Cleaned Sample** — EDTA plasma is diluted in assay-specific diluent to irreversibly inactivate endogenous plasma phosphatases, then pre-cleaned with "clean beads" to remove interfering matrix components.
2. **First Reaction (capture)** — A pool of proprietary monoclonal antibody-coated "capture beads" (anti-pTau solid phase) selectively captures and purifies hyperphosphorylated tau (pTau, including PA pTau) from the cleaned plasma. Reagents supplied by ADx Neurosciences NV (a Fujirebio company).
3. **Washing** — Magnetic washing (4×) removes the plasma matrix from the capture beads.
4. **Second Reaction (normal-tau binding)** — Capture beads are buffer-exchanged into a normal-tau binding buffer (mimicking brain pH/ionic/hydrophobic conditions) and incubated overnight (static, 2–8°C) with recombinant, V5-tagged, full-length normal Tau 1-441 ("Recombinant Normal Tau-441"). If the captured pTau is pathologically active, it binds this recombinant normal tau, analogous to pTau-mediated normal-tau aggregation observed in the AD brain.
5. **Washing** — Magnetic washing (4×) removes unbound Recombinant Normal Tau-441.
6. **Third Reaction (tag detection)** — An alkaline-phosphatase (AP)-conjugated anti-V5-tag monoclonal antibody ("Anti-Tag AP Conjugate") binds the tag on any Recombinant Normal Tau-441 that was captured by PA pTau on the beads.
7. **Washing** — Magnetic washing (4×) removes unbound AP Conjugate.
8. **Enzyme Reaction** — A chemiluminescent substrate is added; the AP conjugate catalyzes a reaction generating a light signal.
9. **Luminescence Measurement** — A GloMax® Discover Microplate Reader records the relative luminescence units (RLU), which is directly proportional to the amount of Recombinant Normal Tau-441 bound by PA pTau — i.e., to the amount of pathologically active (seeding-competent) pTau captured from the plasma sample.

## Scoring
The raw RLU signal is converted into a semi-quantitative **test result Score** using a Standard (EDTA plasma known to be either tau-PET-negative or from an apparently healthy 18–32-year-old donor), run in duplicate in each assay:

```
Score = [Unknown signal response (RLU)] / [(Standard test result signal (RLU)) × (Correction Factor)]
```

- Score < 1.0 → negative (PA pTau not detected)
- Score ≥ 1.0 → positive (PA pTau detected)
- Assay Negative Control: pooled tau-PET-negative/young-donor plasma, Score < 0.93
- Assay Positive Control: pooled tau-PET-positive plasma, Score > 1.20

## Design Rationale
The assay's core design choice — testing binding/seeding activity rather than site-specific phosphorylation concentration — directly targets the gap identified in `logic/problem.md` (G1): existing pTau-species immunoassays (pTau181/205/212/217/231) quantify a phosphorylation state that occurs both physiologically (reversibly, e.g., under hypothermia) and pathologically, and therefore cannot specifically distinguish aggregation-competent tau. By requiring the captured pTau to actively template a normal-tau substrate under brain-like binding conditions, VeraBIND Tau aims to functionally recapitulate the prion-like seeding step itself (RW10 in `logic/related_work.md`).

## What This File Does Not Cover
The exact reagent volumes, incubation times/temperatures, and plate/equipment part numbers are concrete protocol parameters, not conceptual method choices; they are captured verbatim in `src/configs/assay_protocol.md` per the ARA schema's separation of method narrative (`logic/solution/`) from concrete implementation parameters (`src/configs/`).
