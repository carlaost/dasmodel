# Claims — TRAILBLAZER-ALZ 4

Falsifiable efficacy/safety claims. `Proof` references experiment IDs in experiments.md; exact numbers live in `evidence/`. Load-bearing numbers carry `**Sources**` entries with verbatim quotes from the source PDF.

## C01: Donanemab superior on 6-month AP clearance — overall population (co-primary)
- **Statement**: In the overall population, a significantly higher proportion of donanemab- than aducanumab-treated participants reached amyloid plaque clearance (< 24.1 CL) at 6 months: 37.9% (25/66) vs 1.6% (1/64), P < 0.001.
- **Status**: supported
- **Falsification criteria**: If the between-arm difference in 6-month clearance proportion in the overall population were non-significant (P ≥ 0.05) or favored aducanumab.
- **Proof**: [E01]
- **Evidence basis**: Figure 2A; §3.2 — donanemab 37.9% (25/66) vs aducanumab 1.6% (1/64), P<0.001.
- **Interpretation**: One of two co-primary endpoints; establishes early-clearance superiority.
- **Dependencies**: none
- **Tags**: co-primary, amyloid-clearance, 6-month, overall
- **Sources**:
  - 37.9% (25/66) donanemab, 6-mo overall ← paper.pdf p4 §3.2 «37.9% (25 of 66) of donanemab-treated participants versus 1.6% (1 of 64) of aducanumab-treated participants reached AP clearance at 6 months (P < 0.001; Figure 2A)» [result]
  - 1.6% (1/64) aducanumab ← same line above [result]

## C02: Donanemab superior on 6-month AP clearance — low–medium tau subpopulation (co-primary)
- **Statement**: In the low–medium tau subpopulation, a significantly higher proportion of donanemab- than aducanumab-treated participants reached AP clearance (< 24.1 CL) at 6 months: 38.5% (10/26) vs 3.8% (1/26), P = 0.008.
- **Status**: supported
- **Falsification criteria**: If the 6-month clearance difference in the low–medium tau subpopulation were non-significant (P ≥ 0.05) or favored aducanumab.
- **Proof**: [E01]
- **Evidence basis**: Figure 2B; §3.2 — donanemab 38.5% (10/26) vs aducanumab 3.8% (1/26), P=0.008.
- **Interpretation**: Second co-primary endpoint; both co-primary endpoints met permitted gated secondary testing.
- **Dependencies**: none
- **Tags**: co-primary, amyloid-clearance, 6-month, low-medium-tau
- **Sources**:
  - 38.5% (10/26) donanemab, 6-mo low–med tau ← paper.pdf p4 §3.2 «38.5% (10 of 26) of donanemab-treated participants versus 3.8% (1 of 26) of aducanumab-treated participants reached AP clearance at 6 months (P = 0.008; Figure 2B)» [result]
  - 3.8% (1/26) aducanumab ← same line above [result]

## C03: Donanemab superior on AP clearance at 12 and 18 months
- **Statement**: Donanemab-treated participants reached AP clearance more often than aducanumab-treated participants at 12 months (overall 70.0% [42/60] vs 24.6% [15/61], P<0.001) and 18 months (overall 76.8% [43/56] vs 43.1% [25/58], P<0.001); the advantage also held in the low–medium tau subpopulation (12 mo 76.0% vs 18.5%, P<0.001; 18 mo 72.0% vs 43.5%, P=0.022).
- **Status**: supported
- **Falsification criteria**: If clearance proportions at 12 or 18 months did not significantly favor donanemab in the overall population.
- **Proof**: [E02]
- **Evidence basis**: Figure 3A, 3B; §3.3.1.
- **Interpretation**: Superiority persists and remains significant through 18 months; overall-population differences narrow somewhat by 18 months as aducanumab catches up (43.1%).
- **Dependencies**: C01
- **Tags**: secondary, amyloid-clearance, 12-month, 18-month
- **Sources**:
  - 70.0% (42/60) vs 24.6% (15/61), 12-mo overall ← paper.pdf p4–5 §3.3.1 «70.0% (42 of 60) of donanemab-treated participants and 24.6% (15 of 61) of aducanumab-treated participants reached AP clearance (P < 0.001) in the overall population» [result]
  - 76.8% (43/56) vs 43.1% (25/58), 18-mo overall ← paper.pdf p5 §3.3.1 «76.8% (43 of 56) of donanemab-treated participants versus 43.1% (25 of 58) of aducanumab-treated participants reached AP clearance(P<0.001;Figure3B)» [result]
  - low–med tau 76.0% vs 18.5% (P<0.001) and 72.0% vs 43.5% (P=0.022) ← paper.pdf p5 §3.3.1 «76.0% (19 of 25) and 72.0% (18 of 25) of donanemab-treated participants versus 18.5% (5 of 27) and 43.5% (10 of 23) of aducanumab-treated participants reached AP clearance at 12 months (P < 0.001) and 18 months (P = 0.022)» [result]

## C04: Donanemab reaches AP clearance faster (shorter median time)
- **Statement**: Median time to achieve AP clearance was shorter with donanemab than aducanumab: 359 days vs 568 days (P < 0.001, log-rank), with more clearance events (51/67 vs 25/65).
- **Status**: supported
- **Falsification criteria**: If the log-rank comparison of time-to-clearance were non-significant, or the donanemab median were ≥ the aducanumab median.
- **Proof**: [E03]
- **Evidence basis**: Figure 3C; §3.3.2 — median 359 vs 568 days, P<0.001; KM events 51 (donanemab) vs 25 (aducanumab).
- **Interpretation**: Key secondary endpoint (time to AP clearance, tested at study completion); ~209-day earlier clearance.
- **Dependencies**: C01
- **Tags**: key-secondary, time-to-clearance, Kaplan-Meier
- **Sources**:
  - median 359 vs 568 days, P<0.001 ← paper.pdf p5 §3.3.2 «The median time to achieve AP clearance was 359 days for donanemab-treated participants versus 568 days for aducanumab-treated participants (P < 0.001; Figure 3C)» [result]
  - events 51/67 (donanemab), 25/65 (aducanumab) ← evidence/figures/figure3.png (Figure 3C on-plot table) «Aducanumab 65 25 568.00 (542.00; -); Donanemab 67 51 359.00 (343.00; 377.00)» [result]

## C05: Donanemab produced greater absolute and percent amyloid lowering at 6, 12, and 18 months
- **Statement**: LS mean absolute (CL) and percent change from baseline in brain amyloid PET favored donanemab over aducanumab at all timepoints in the overall population (e.g., 6-mo percent change −65.17 vs −16.96; 18-mo percent change −86.29 vs −72.84) and in the low–medium tau subpopulation, all P values significant (P ≤ .042).
- **Status**: supported
- **Falsification criteria**: If any timepoint's between-arm difference in mean amyloid change were non-significant in the overall population.
- **Proof**: [E04]
- **Evidence basis**: Table 2 — all 6/12/18-month absolute and percent comparisons P<0.05 favoring donanemab; overall-population 6-mo percent change −65.17 vs −16.96 (P<0.001).
- **Interpretation**: Key secondary endpoint (mean change from baseline), tested in the gated hierarchy; depth of clearance greater with donanemab.
- **Dependencies**: C01
- **Tags**: key-secondary, amyloid-lowering, ANCOVA, MMRM
- **Sources**:
  - 6-mo overall LS mean percent change −65.17 vs −16.96, P<0.001 ← evidence/tables/table2.md (Table 2) «6 | LS mean percent change | −65.17 | −16.96 | <0.001» [result]
  - 18-mo overall LS mean percent change −86.29 vs −72.84, P=.002 ← evidence/tables/table2.md (Table 2) «18 | LS mean percent change | −86.29 | −72.84 | .002» [result]

## C06: Plasma biomarker differences favor donanemab early but are not significant at 18 months (NfL never significant)
- **Statement**: At 18 months, donanemab showed numerically greater decreases than aducanumab in plasma p-tau217 (−33.2% vs −25.7%), p-tau181 (−18.0% vs −14.3%), and GFAP (−20.0% vs −13.7%), but the adjusted mean differences were NOT statistically significant at 18 months (p-tau217 P=0.098; p-tau181 P=0.372; GFAP P=0.171); the differences were significant at 6 months for all three. NfL increased from baseline in both arms (donanemab +8.9% vs aducanumab +14.0%) with no significant treatment effect at any timepoint.
- **Status**: supported
- **Falsification criteria**: If the 18-month adjusted mean differences for p-tau217/p-tau181/GFAP were reported as statistically significant, or if a significant NfL treatment effect had been observed.
- **Proof**: [E05]
- **Evidence basis**: Figure 4A–D; §3.3.3; §4.
- **Interpretation**: Consistent directional biomarker changes; loss of 18-month significance attributed by authors to higher variability/lower power of plasma biomarkers and residual pathology after clearance.
- **Dependencies**: C05
- **Tags**: exploratory-biomarker, p-tau, GFAP, NfL, MMRM
- **Sources**:
  - p-tau217 18-mo −33.2% vs −25.7%; diff at 18mo P=0.098 ← paper.pdf p5 §3.3.3 «plasma phosphorylated tau (p-tau)217 levels at 18 months were 33.2% lower with donanemab treatment compared to 25.7% lower with aducanumab treatment... −0.046 (95% CI, −0.100 to 0.009; P = 0.098) at 18 months» [result]
  - NfL +8.9% vs +14.0%, no significant effect ← paper.pdf p5–6 §3.3.3 «plasma levels of NfL at 18 months were 8.9% higher with donanemab treatment compared to 14.0% higher with aducanumab treatment versus baseline» and §4 «No significant treatment effect on NfL was observed» [result]

## C07: Faster/deeper amyloid clearance did not increase ARIA frequency or risk
- **Statement**: Despite greater and faster amyloid clearance with donanemab, ARIA incidence was not increased relative to aducanumab; ARIA-E TEAE incidence was numerically lower with donanemab (23.9% vs 34.8%), ARIA-H lower (22.5% vs 33.3%), and time-to-first-ARIA-E did not differ significantly between arms (P = 0.438).
- **Status**: supported
- **Falsification criteria**: If donanemab (the faster/deeper clearer) had shown significantly higher ARIA-E incidence or significantly earlier time-to-ARIA-E than aducanumab.
- **Proof**: [E06]
- **Evidence basis**: Table 3 (ARIA-E 23.9% vs 34.8%; ARIA-H 22.5% vs 33.3%); Figure 5 (P=0.438); §3.4, §4.
- **Interpretation**: Authors conclude the amount and rapidity of amyloid clearance do not necessarily correspond to increased ARIA occurrence.
- **Dependencies**: C03, C04
- **Tags**: safety, ARIA, class-effect
- **Sources**:
  - ARIA-E TEAE 23.9% (donanemab) vs 34.8% (aducanumab) ← evidence/tables/table3.md (Table 3) «ARIA-E ᵃ | 17 (23.9) | 24 (34.8)» [result]
  - time-to-first-ARIA-E P=.438 ← evidence/figures/figure5.png (Figure 5 on-plot) «Aducanumab 69 23 ; Donanemab 71 17 .438» [result]

## C08: No deaths; overall safety/tolerability consistent with prior reports
- **Statement**: There were no deaths in the study; TEAEs occurred in 83.1% (donanemab) and 87.0% (aducanumab); ≥1 SAE in 18.3% vs 11.6%; ARIA-E events were mostly mild-to-moderate radiographic severity (88.2% donanemab, 82.6% aducanumab); infusion-related reactions were higher with donanemab (8.5% vs 2.9%) and superficial siderosis higher with aducanumab (10.1% vs 0%).
- **Status**: supported
- **Falsification criteria**: If any deaths occurred, or if TEAE/SAE/ARIA severity profiles diverged materially from those reported.
- **Proof**: [E06]
- **Evidence basis**: Table 3; §3.4; Figure 1 (disposition).
- **Interpretation**: Tolerability broadly comparable; distinct AE signatures (donanemab: infusion reactions; aducanumab: superficial siderosis).
- **Dependencies**: none
- **Tags**: safety, tolerability, adverse-events
- **Sources**:
  - no deaths ← paper.pdf p6 §3.4 «There were no deaths in this study.» [result]
  - TEAEs 83.1% vs 87.0% ← evidence/tables/table3.md (Table 3) «TEAEs | 59 (83.1) | 60 (87.0)» [result]
  - ARIA-E mostly mild-moderate 88.2% / 82.6% ← paper.pdf p6 §3.4 «Events of ARIA-E with donanemab and aducanumab were mostly of mild to moderate radiographic severity (88.2% and 82.6% of ARIA-E events, respectively)» [result]
