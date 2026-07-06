# VeraBIND Tau Assay Protocol — Concrete Parameters

Verbatim protocol parameters from Methods, "VeraBIND™ Tau assay" (PDF p.9–11). These are the concrete, runnable-protocol values underlying the conceptual method description in `logic/solution/method.md`; equipment/reagent part numbers are included so the wet-lab protocol is reproducible.

## Plasma input volume
- **Value**: 110 µL of freshly thawed 2–8°C EDTA plasma
- **Rationale**: Standard input volume for the assay's sample-conditioning step.
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, PDF p.9

## Sample dilution/conditioning
- **Value**: 110 µL plasma added to 550 µL of 2–8°C assay-specific sample diluent; incubated 30 min at 2–8°C with gentle mixing
- **Rationale**: Irreversibly inactivates endogenous plasma phosphatases prior to capture.
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, PDF p.9

## Pre-analytical clean-bead step
- **Value**: 600 µL diluted/conditioned plasma + 100 µL custom VeraBIND clean beads; incubated 30 min at 37°C, 1,000 rpm; magnetic separation 15 min; 700 µL bead-free supernatant recovered
- **Rationale**: Removes plasma-matrix interferents before pTau capture.
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, PDF p.9–10

## Capture-bead reaction (pTau purification)
- **Value**: 700 µL cleaned supernatant + 100 µL custom VeraBIND capture beads; incubated 30 min at 37°C, 1,000 rpm; washed magnetically 4× with 500 µL AD wash buffer
- **Rationale**: Selective capture/purification of hyperphosphorylated tau (pTau) by the pool of monoclonal antibody-coated capture beads.
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, PDF p.10

## Normal-tau binding reaction
- **Value**: Capture beads buffer-exchanged into 120 µL normal tau binding buffer; 100 µL recombinant V5-tagged full-length normal Tau 1-441 added; incubated static (no mixing) overnight at 2–8°C; then washed magnetically 4× with 500 µL normal tau wash buffer after warming to 37°C for 30 min
- **Rationale**: Facilitates ionic/hydrophobic binding of PA pTau to recombinant normal tau, mimicking the brain's binding environment; overnight static incubation allows seeding/templating to occur.
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, PDF p.10

## Detection reaction
- **Value**: 100 µL detection buffer + freshly thawed TruBlock Ultra, incubated 5 min; then 100 µL freshly diluted anti-V5 AP Conjugate, incubated static 30 min at 37°C; washed magnetically 4× with 500 µL normal tau wash buffer; resuspended in 100 µL normal tau wash buffer and transferred to a Corning® 96-well white round-bottom polystyrene NBS Microplate (Part No. 3605)
- **Rationale**: Anti-tag AP-conjugated antibody binds only the tag on Recombinant Normal Tau-441 that was captured by PA pTau, providing a signal proportional to seeding activity.
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, PDF p.10–11

## Luminescence readout
- **Value**: 100 µL substrate added, mixed 60 s at 1,000 rpm, incubated 60 min at 30°C static; luminescence read on a GloMax® Discover Microplate Reader (RLU units)
- **Rationale**: Chemiluminescent substrate converted by the AP conjugate generates a luminescent signal directly proportional to bound Recombinant Normal Tau-441 (i.e., to PA pTau captured from plasma).
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, PDF p.11

## Test result Score cutoff
- **Value**: Score ≥ 1.0 = positive; Score < 1.0 = negative. Score = [Unknown RLU] / [(Standard RLU) × (Correction Factor)]
- **Rationale**: Dichotomizes the semi-quantitative RLU-ratio readout into a binary clinical call, normalized against a per-run Standard and lot-specific correction factor.
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, PDF p.11

## Assay Negative/Positive Control cutoffs
- **Value**: Negative Control (pooled tau-PET-negative or age 18–32 healthy-donor EDTA plasma) Score < 0.93; Positive Control (pooled tau-PET-positive EDTA plasma) Score > 1.20
- **Rationale**: Internal quality-control bounds verifying assay-run validity.
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, PDF p.11

## Key reagent/equipment identifiers
- **Value**: K2-EDTA blood tubes: Sarstedt 7.5 mL S-monovette, Part No. 01.1605.008. PP micro tube: Sarstedt Part No. 72.694.306. Deep-well plate: Stellar Scientific Part No. DWP-WB-3866. Detection microplate: Corning Part No. 3605. Plate heater/shaker: Qinstruments BioShake iQ with thermal adapter Part No. 1808-0506. Plate magnet: Alpaqua Magnum FLX® (Solid-Core™). Reader: GloMax® Discover Microplate Reader. Capture-bead antibody reagents: supplied by ADx Neurosciences NV (A Fujirebio Company).
- **Rationale**: Reproducibility identifiers for the wet-lab protocol.
- **Search range**: Not applicable
- **Sensitivity**: Not specified in paper
- **Source**: Methods, PDF p.9–11
