# Problem Specification

## Observations

### O1: Donanemab significantly slowed clinical progression during the 76-week placebo-controlled period of TRAILBLAZER-ALZ 2
- **Statement**: In the pivotal phase 3 TRAILBLAZER-ALZ 2 trial, donanemab significantly slowed clinical progression compared with placebo at 76 weeks in participants with early symptomatic AD and amyloid and tau pathology (previously reported in Sims et al. [2]).
- **Evidence**: §1 Introduction (`paper.pdf` p1).
- **Implication**: The 76-week placebo-controlled result establishes short/medium-term efficacy, but does not show whether benefit persists, grows, or fades once treatment is stopped after a limited course.

### O2: TRAILBLAZER-ALZ 2 used a distinctive limited-duration dosing design with amyloid-based treatment course completion criteria
- **Statement**: Participants receiving donanemab were switched to blinded placebo infusions after meeting treatment course completion criteria — an amyloid plaque level of <11 Centiloids (CL) on any single PET scan or <25 CL on two consecutive PET scans — assessed at weeks 24, 52, 76, 102, or 130.
- **Evidence**: §1 Introduction; §2.1 Trial design (`paper.pdf` p1–2).
- **Implication**: Because dosing is capped once amyloid is cleared, a central open question is whether clinical benefit is retained after treatment stops and how quickly amyloid re-accumulates — this cannot be answered from the 76-week placebo-controlled data alone.

### O3: The 78-week long-term extension (LTE) has no internal placebo control
- **Statement**: The LTE of TRAILBLAZER-ALZ 2 does not include an internal placebo control to allow comparison of disease progression in participants without amyloid-targeting treatment; all delayed-start (originally placebo) participants who continue into the LTE are started on donanemab.
- **Evidence**: §2.3 External ADNI control cohort (`paper.pdf` p3).
- **Implication**: Any efficacy estimate over the full 3-year (154-week) observation period requires an external, untreated comparison cohort rather than a randomized concurrent control.

### O4: A majority of early-start participants who enter the LTE stop receiving donanemab and revert to blinded placebo
- **Statement**: Of the 860 participants randomized to donanemab (early-start), 550 (64.0%) received at least one LTE infusion; of these, 393 were switched to placebo (having met treatment course completion criteria) and only 157 continued donanemab in the LTE. The majority (71.5%) of early-start participants who continued into the LTE received only blinded placebo infusions for the entire LTE duration.
- **Evidence**: §3.1 Participants; §4 Discussion (`paper.pdf` p4, p7).
- **Implication**: Long-term "early-start" efficacy in the LTE is overwhelmingly a test of durability of benefit after treatment discontinuation, not of continued active treatment.

### O5: Delayed-start participants entering the LTE have more severe disease than the original study population
- **Statement**: Delayed-start participants who entered the LTE had more severe disease at LTE start than the study population had at the start of the placebo-controlled period; almost half of delayed-start participants would not have met the study's initial MMSE-based eligibility criteria.
- **Evidence**: §4 Discussion (`paper.pdf` p7).
- **Implication**: Early-start vs delayed-start comparisons are confounded by differential disease severity at donanemab initiation, complicating causal interpretation of any observed gap between groups.

## Gaps

### G1: Whether donanemab's clinical benefit persists, and how it evolves, over 3 years of observation including after treatment discontinuation
- **Statement**: It was unknown whether the clinical benefit demonstrated at 76 weeks would continue to grow, plateau, or erode over a longer follow-up window, and specifically whether benefit is retained once dosing stops following amyloid clearance.
- **Caused by**: O1, O2, O4
- **Existing attempts**: The 76-week placebo-controlled analysis (Sims et al. [2]).
- **Why they fail**: A 76-week placebo-controlled window cannot observe post-discontinuation durability or effects beyond 18 months.

### G2: No internal placebo group exists in the LTE to quantify long-term treatment effect
- **Statement**: Without a placebo arm in the LTE, disease-progression benefit at 3 years cannot be measured by direct within-trial comparison.
- **Caused by**: O3
- **Existing attempts**: None within TRAILBLAZER-ALZ 2 itself; other donanemab studies did not provide an internal untreated comparator either.
- **Why they fail**: Ethically, an amyloid-clearing therapy with demonstrated 76-week benefit could not be withheld from all LTE participants; an external comparator was required instead.

### G3: The rate of amyloid reaccumulation after treatment discontinuation, and whether it threatens the durability of clinical benefit, was uncharacterized
- **Statement**: Because dosing is capped once amyloid is cleared, whether plaque reaccumulates quickly (undermining the rationale for limited-duration dosing) or slowly (supporting it) was an open, clinically consequential question.
- **Caused by**: O2
- **Existing attempts**: Amyloid trajectories were reported through 76 weeks in the pivotal trial; no post-discontinuation reaccumulation rate had been established from TRAILBLAZER-ALZ 2 alone.
- **Why they fail**: The pivotal 76-week report ends before enough participants complete a course and are followed long enough off-drug to estimate a reaccumulation slope.

## Key Insight
- **Insight**: By following both early-start (randomized donanemab) and delayed-start (randomized placebo, then donanemab in the LTE) participants for a full 78-week blinded extension (154 weeks total), and comparing CDR-SB trajectories to a propensity-score-weighted external control drawn from the ADNI natural-history cohort, it is possible to estimate whether donanemab's clinical benefit grows over 3 years, whether that benefit is retained after limited-duration dosing ends, and how quickly amyloid re-accumulates once treatment stops — without an internal LTE placebo arm.
- **Derived from**: O1, O2, O3, O4, O5
- **Enables**: Estimation of a 3-year treatment effect (early-start vs weighted ADNI), a shorter delayed-start treatment effect, a between-group progression-risk comparison (early- vs delayed-start via CDR-Global), amyloid reduction/clearance/reaccumulation trajectories after treatment completion, and a continued, descriptive long-term safety profile.

## Assumptions
- A1: The propensity-score-weighted ADNI cohort (matched on age, sex, APOE ε4 status, CDR-SB, ADAS-Cog13, and screening MMSE) is an acceptable proxy for the disease trajectory TRAILBLAZER-ALZ 2 participants would have followed without amyloid-targeting treatment.
- A2: Baseline amyloid CL level, though associated with disease trajectory, could be omitted from the propensity weighting because it was missing for 43% of the eligible ADNI-derived population.
- A3: Any increase in CDR-Global (CDR-G) score at two consecutive study visits represents a clinically meaningful stage transition, appropriate as a hazard-model endpoint for between-group comparison.
- A4: The established minimal-clinically-important-difference (MCID) thresholds for CDR-SB, derived for individual patient-level change, are not appropriate for interpreting between-group differences at a study endpoint (stated explicitly in §4 Discussion, citing [16]).
- A5: Combining LTE reaccumulation data with three earlier donanemab studies (phase 1b, TRAILBLAZER-ALZ phase 2, TRAILBLAZER-EXT) into a single exposure-response model yields a valid overall reaccumulation-rate estimate.
