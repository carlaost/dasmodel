# Claims

All analyses were exploratory and not controlled for multiplicity (§2.5). Numbers are copied
exactly from `paper.pdf` (verified via the EuropePMC/PMC open-access full text, PMC12869028,
CC BY license); source quotes appear under each claim's `**Sources**`.

## C01: Early-start donanemab slows CDR-SB progression versus a weighted ADNI external control at 3 years
- **Statement**: Donanemab treatment slowed disease progression among early-start participants, with an adjusted mean (LS mean) treatment difference of −1.2 points (95% CI, −1.7 to −0.7) in the CDR-SB score between donanemab and the weighted external ADNI control cohort at 3 years (36 months).
- **Status**: supported
- **Falsification criteria**: The 95% CI for the early-start vs ADNI CDR-SB difference at 36 months includes 0, or the point estimate is ≥0 (higher CDR-SB = worse, so a true benefit requires a negative difference).
- **Proof**: [E01]
- **Evidence basis**: Abstract; §3.2 Efficacy; Fig. 2a (36-month difference −1.2 [−1.7, −0.7]; early-start N=417, ADNI cohort ESS=122 at that timepoint).
- **Interpretation**: The difference from ADNI grows monotonically from month 6 (−0.2) to month 36 (−1.2), consistent with an increasing treatment effect over time rather than a fixed offset.
- **Dependencies**: none
- **Tags**: CDR-SB, efficacy, early-start, ADNI-control, 3-year
- **Sources**:
  - −1.2 points (95% CI, −1.7 to −0.7) at 3 years ← `paper.pdf` p4 §3.2 «Donanemab treatment slowed disease progression among early-start participants, with an adjusted mean treatment difference of −1.2 points (95 % CI, −1.7 to −0.7) in the CDR-SB score between donanemab and the weighted external ADNI control cohort at 3 years (Fig. 2a)» [result]
  - Month 36 difference −1.2 (−1.7, −0.7); early-start N=417; ADNI ESS=122 ← `paper.pdf` p5 Fig. 2a «Early start vs ADNI difference (95% CI): ... −1.2 (−1.7, −0.7) ... Early-start group (N): ... 417 ... ADNI cohort (ESS): ... 122» [result]

## C02: Delayed-start donanemab slows CDR-SB progression versus a weighted ADNI external control 76 weeks after initiation
- **Statement**: Donanemab treatment also slowed disease progression among delayed-start participants, with an adjusted mean treatment difference of −0.8 points (95% CI, −1.3 to −0.3) in the CDR-SB score 76 weeks after initiating donanemab versus the weighted external ADNI control cohort.
- **Status**: supported
- **Falsification criteria**: The 95% CI for the delayed-start vs ADNI CDR-SB difference at 76 weeks post-initiation (month 36 on the overall trial timeline) includes 0, or the point estimate is ≥0.
- **Proof**: [E02]
- **Evidence basis**: §3.2 Efficacy; Fig. 2b (36-month difference −0.8 [−1.3, −0.3]; delayed-start N=458, ADNI ESS=139).
- **Interpretation**: The delayed-start effect size at an equivalent 76 weeks of donanemab exposure (−0.8) is smaller than the early-start 3-year effect (−1.2, C01), consistent with a shorter donanemab exposure window and/or greater baseline disease severity in delayed-start participants (O5).
- **Dependencies**: none
- **Tags**: CDR-SB, efficacy, delayed-start, ADNI-control
- **Sources**:
  - −0.8 points (95% CI, −1.3 to −0.3) ← `paper.pdf` p6 §3.2 «Donanemab treatment also slowed disease progression among delayed-start participants, with an adjusted mean treatment difference of −0.8 points (95 % CI, −1.3 to −0.3) in the CDR-SB score 76 weeks after initiating donanemab versus the weighted external ADNI control cohort (Fig. 2b)» [result]
  - Month 36 difference −0.8 (−1.3, −0.3); delayed-start N=458; ADNI ESS=139 ← `paper.pdf` p5 Fig. 2b «Delayed start vs ADNI difference (95% CI): ... −0.8 (−1.3, −0.3) ... Delayed-start group (N): ... 458 ... ADNI cohort (ESS): ... 139» [result]

## C03: Participants who met treatment course completion criteria by 52 weeks show similar CDR-SB efficacy to the overall early-start group
- **Statement**: Among early-start participants who met treatment course completion criteria by 52 weeks of the placebo-controlled period, the adjusted mean CDR-SB treatment difference versus the weighted ADNI cohort was −1.3 points (95% CI, −1.9 to −0.7) at 3 years, similar to the overall early-start effect of −1.2 (C01).
- **Status**: supported
- **Falsification criteria**: The 95% CI for this subgroup's 36-month difference includes 0, or diverges materially in direction/magnitude from the overall early-start estimate.
- **Proof**: [E03]
- **Evidence basis**: §3.2 Efficacy ("similar efficacy results were observed for participants who met treatment course completion criteria by 52 weeks"); Fig. 2c (36-month difference −1.3 [−1.9, −0.7]; N=198, ADNI ESS=122).
- **Interpretation**: Benefit is not confined to participants who remained on donanemab longest — it is also present, at a comparable magnitude, in those who completed dosing earliest (52 weeks), supporting durability after early treatment completion.
- **Dependencies**: C01
- **Tags**: CDR-SB, efficacy, treatment-course-completion, 52-week-subset
- **Sources**:
  - Similar efficacy for 52-week completers ← `paper.pdf` p6 §3.2 «Similar efficacy results were observed for participants who met treatment course completion criteria by 52 weeks of the placebo-controlled period (Fig. 2c)» [result]
  - Month 36 difference −1.3 (−1.9, −0.7); early-start N=198; ADNI ESS=122 ← `paper.pdf` p5 Fig. 2c «Early start vs ADNI difference (95% CI): ... −1.3 (−1.9, −0.7) ... Early-start group^a (N): ... 198 ... ADNI cohort (ESS): ... 122» [result]

## C04: Early-start participants have a 27% lower risk of progressing to the next CDR-Global disease stage than delayed-start participants
- **Statement**: In a comparison of the early- versus delayed-start groups using the CDR-G score, early-start participants showed a 27% reduced risk of progressing to the next clinical stage of disease versus delayed-start participants over 154 weeks (hazard ratio = 0.73 [95% CI, 0.62–0.86]; p<0.001).
- **Status**: supported
- **Falsification criteria**: The hazard ratio 95% CI includes 1.0, or p≥0.05.
- **Proof**: [E04]
- **Evidence basis**: §3.2 Efficacy; Fig. 3 (HR=0.73 [0.62–0.86], p<0.001; cumulative progression curves showing early-start below delayed-start throughout the LTE period).
- **Interpretation**: The paper explicitly frames this CDR-G hazard-ratio result as "the best evidence of clinical meaningfulness from the available LTE data" (§4), because any CDR-G increase denotes a discrete disease-stage transition rather than a continuous-scale point difference.
- **Dependencies**: none
- **Tags**: CDR-G, progression, hazard-ratio, early-vs-delayed-start
- **Sources**:
  - 27% reduced risk; HR=0.73 [0.62, 0.86]; p<0.001 ← `paper.pdf` p6 §3.2 «In a comparison of the early- versus delayed-start groups using the CDR-G score (Fig. 3), early-start participants showed a 27 % reduced risk of progressing to the next clinical stage of the disease versus delayed-start participants (hazard ratio=0.73 [95 % CI, 0.62–0.86]; p < 0.001)» [result]
  - Hazard ratio (95% CI) 0.73 (0.62-0.86); p<0.001 ← `paper.pdf` p5 Fig. 3 «Hazard ratio (95 % CI)^a 0.73 (0.62-0.86); p<0.001» [result]
  - "best evidence of clinical meaningfulness from the available LTE data" ← `paper.pdf` p8 §4 «This difference provides the best evidence of clinical meaningfulness from the available LTE data» [result]

## C05: Early-start donanemab treatment shows a superior cumulative (AUC) CDR-SB benefit over the LTE period
- **Statement**: In a supporting area-under-the-curve (AUC) analysis of the early-start group versus the ADNI cohort on change in the CDR-SB score, a superior cumulative benefit of donanemab treatment was shown among early-start participants during the LTE period, with an average treatment difference of 0.97 points across 78 weeks (p<0.001).
- **Status**: supported
- **Falsification criteria**: The AUC-based average treatment difference over the 78-week LTE window is ≤0 or p≥0.05.
- **Proof**: [E05]
- **Evidence basis**: §3.2 Efficacy (Fig. S6, referenced but not included in the provided PDF — main-text summary number used here).
- **Interpretation**: The AUC framing captures cumulative (not just endpoint) benefit and corroborates the endpoint-based CDR-SB result (C01) with an independent summary statistic.
- **Dependencies**: C01
- **Tags**: CDR-SB, AUC, cumulative-benefit, early-start
- **Sources**:
  - Average treatment difference 0.97 points across 78 weeks, p<0.001 ← `paper.pdf` p6 §3.2 «a superior cumulative benefit of donanemab treatment was shown among early-start participants during the LTE period (Fig. S6), with an average treatment difference of 0.97 points across 78 weeks (p < 0.001)» [result]

## C06: Earlier donanemab initiation saves more time on CDR-SB progression than delayed initiation
- **Statement**: At 3 years, early-start donanemab treatment saved approximately 6.9 months versus the ADNI cohort as measured by the CDR-SB score. At the end of the LTE, 1.5 years after starting donanemab, delayed-start treatment saved approximately 5.6 months on CDR-SB progression — an absolute difference in time savings of 1.3 months favoring earlier treatment.
- **Status**: supported
- **Falsification criteria**: The early-start time-saved estimate is ≤ the delayed-start time-saved estimate, or either time-saved estimate is ≤0.
- **Proof**: [E06]
- **Evidence basis**: §3.2 Efficacy; §4 Discussion.
- **Interpretation**: The paper cautions that the 1.3-month absolute gap likely understates the true benefit of earlier treatment, because the rate of disease progression is generally higher at later disease stages — a factor not accounted for in the time-saved calculation.
- **Dependencies**: C01, C02
- **Tags**: time-saved, CDR-SB, early-vs-delayed-start
- **Sources**:
  - Early-start 6.9 months at 3 years; delayed-start 5.6 months at end of LTE (1.5 years after starting donanemab) ← `paper.pdf` p6 §3.2 «At 3 years, early-start donanemab treatment saved approximately 6.9 months versus the ADNI cohort as measured by the CDR-SB score. At the end of the LTE and 1.5 years after starting donanemab, delayed-start treatment saved approximately 5.6 months on CDR-SB progression» [result]
  - Absolute difference in time savings 1.3 months; progression rate generally higher at later stages (not accounted for) ← `paper.pdf` p8 §4 «although the absolute difference in time savings observed between early- and delayed-start donanemab is 1.3 months, the rate of disease progression is generally higher at later stages, which is not accounted for in our calculation» [result]

## C07: Donanemab produces robust and similarly sized amyloid plaque reduction regardless of early- or delayed-start timing
- **Statement**: Early-start participants achieved an LS mean (SE) reduction in amyloid plaque of 86.96 (0.92) CL at 76 weeks. Delayed-start participants achieved a similar reduction of 86.01 (0.89) CL at 154 weeks (76 weeks after initiating donanemab).
- **Status**: supported
- **Falsification criteria**: The two LS mean CL reductions differ by an amount inconsistent with "similar" (e.g., non-overlapping given their SEs by a wide margin), or either reduction is not significantly different from 0.
- **Proof**: [E07]
- **Evidence basis**: §3.3 Amyloid PET; Fig. 4a.
- **Interpretation**: Because both groups reach nearly identical CL reduction at an equivalent 76 weeks of donanemab exposure, the paper argues the biologic amyloid-lowering effect of donanemab is consistent regardless of when treatment starts or background disease progression at initiation.
- **Dependencies**: none
- **Tags**: amyloid, centiloids, early-vs-delayed-start, biomarker
- **Sources**:
  - 86.96 (0.92) CL at 76 weeks (early-start); 86.01 (0.89) CL at 154 weeks / 76 weeks post-initiation (delayed-start) ← `paper.pdf` p6 §3.3 «Early-start participants achieved an LS mean (standard error) reduction in amyloid plaque of 86.96 (0.92) CL at 76 weeks. Delayed-start participants achieved a similar reduction (86.01 [0.89] CL) at 154 weeks, 76 weeks after initiating donanemab (Fig. 4a)» [result]

## C08: More than 75% of donanemab-treated participants achieve amyloid clearance (<24.1 CL) by 76 weeks after initiation, in both early- and delayed-start groups
- **Statement**: After initiating donanemab treatment, amyloid clearance (<24.1 CL) was achieved by a similar percentage of early- and delayed-start participants at week 24 (29.7% [n=226/761] and 33.2% [n=196/591], respectively), week 52 (66.1% [n=443/670] and 66.7% [n=345/517], respectively), and week 76 (76.4% [n=469/614] and 76.5% [n=345/451], respectively). An additional 56.8% of early-start participants who continued donanemab treatment in the LTE achieved amyloid clearance by the end of the LTE.
- **Status**: supported
- **Falsification criteria**: Clearance percentages diverge substantially between early- and delayed-start groups at a matched post-initiation timepoint, or clearance does not increase monotonically from week 24 to week 76.
- **Proof**: [E07]
- **Evidence basis**: §3.3 Amyloid PET; Fig. 4b (bar chart: 29.7/33.2, 66.1/66.7, 76.4/76.5 at weeks 24/52/76 post-initiation for early-/delayed-start respectively).
- **Interpretation**: The near-identical clearance trajectories reinforce C07 — the biologic amyloid response to donanemab does not depend on whether the participant is in the early- or delayed-start group.
- **Dependencies**: C07
- **Tags**: amyloid-clearance, centiloids, biomarker, early-vs-delayed-start
- **Sources**:
  - Week 24: 29.7% (226/761) / 33.2% (196/591); week 52: 66.1% (443/670) / 66.7% (345/517); week 76: 76.4% (469/614) / 76.5% (345/451) ← `paper.pdf` p6 §3.3 «amyloid clearance (<24.1 CL) was achieved by a similar percentage of early- and delayed-start participants at week 24 (29.7 % [n = 226/761] and 33.2 % [n = 196/591], respectively), week 52 (66.1 % [n = 443/670] and 66.7 % [n = 345/517], respectively), and week 76 (76.4 % [n = 469/614] and 76.5 % [n = 345/451], respectively) (Fig. 4b)» [result]
  - Additional 56.8% of early-start LTE-continuers achieved clearance by end of LTE ← `paper.pdf` p6 §3.3 «Additional early-start participants (56.8 %) who continued donanemab treatment in the LTE period achieved amyloid clearance (<24.1 CL) assessed by an amyloid PET scan at the end of the LTE» [result]

## C09: The proportion of participants meeting amyloid-based treatment course completion criteria in the LTE mirrors the placebo-controlled period rates
- **Statement**: For early-start participants who continued donanemab treatment in the LTE, 29.9% (n=44/147) met treatment course completion criteria at 102 weeks, 45.6% (n=62/136) at 130 weeks, and 55.6% (n=70/126) at 154 weeks. For delayed-start participants who received donanemab in the LTE, 17.6% (n=105/595) met criteria at 102 weeks (24 weeks after starting donanemab), 51.3% (n=267/520) at 130 weeks (52 weeks after starting), and 70.7% (n=319/451) at 154 weeks (76 weeks after starting) — values similar to the placebo-controlled-period completion rates at 24, 52, and 76 weeks (17.1%, 46.6%, and 69.2%, respectively).
- **Status**: supported
- **Falsification criteria**: The LTE completion-criteria rates at matched post-initiation timepoints diverge substantially from the placebo-controlled-period rates (17.1%/46.6%/69.2%).
- **Proof**: [E09]
- **Evidence basis**: §3.3 Amyloid PET.
- **Interpretation**: Consistency of completion timing across the placebo-controlled period and the LTE (in both early- and delayed-start groups) indicates the amyloid-lowering kinetics of donanemab are stable and reproducible across different points in the trial and disease timeline.
- **Dependencies**: C08
- **Tags**: treatment-course-completion, amyloid, consistency
- **Sources**:
  - Early-start continuers: 29.9% (44/147) at 102wk, 45.6% (62/136) at 130wk, 55.6% (70/126) at 154wk ← `paper.pdf` p6 §3.3 «29.9 % (n = 44/147) met treatment course completion criteria at 102 weeks, 45.6 % (n = 62/136) at 130 weeks, and 55.6 % (n = 70/126) at 154 weeks» [result]
  - Delayed-start: 17.6% (105/595) at 102wk, 51.3% (267/520) at 130wk, 70.7% (319/451) at 154wk; PC-period rates 17.1%/46.6%/69.2% ← `paper.pdf` p6 §3.3 «17.6 % (n = 105/595) met treatment course completion criteria at 102 weeks ... 51.3 % (n = 267/520) at 130 weeks ... and 70.7 % (n = 319/451) at 154 weeks ... similar to the percentage of donanemab-treated participants in the placebo-controlled period who met treatment course completion criteria at 24 weeks (17.1 %), 52 weeks (46.6 %), and 76 weeks (69.2 %)» [result]

## C10: Amyloid re-accumulates slowly after donanemab discontinuation, at a rate comparable to natural disease progression
- **Statement**: Early-start participants who met treatment course completion criteria by 52 weeks maintained a mean (SD) amyloid level of 10.99 (14.41) CL at 154 weeks — below the 24.1 CL amyloid-negativity cutoff. Combining LTE data with three additional donanemab studies (phase 1b NCT02624778; TRAILBLAZER-ALZ phase 2 NCT03367403; TRAILBLAZER-EXT NCT04640077), amyloid plaque reaccumulation was calculated to be 2.4 CL/year.
- **Status**: supported
- **Falsification criteria**: The mean amyloid level of 52-week completers at 154 weeks exceeds the 24.1 CL amyloid-negativity cutoff, or the estimated reaccumulation rate is not "comparable" to independently reported natural accumulation rates ([14],[15]).
- **Proof**: [E08]
- **Evidence basis**: §3.3 Amyloid PET; Fig. 4c; §4 Discussion.
- **Interpretation**: The paper interprets this as reinforcing "previously reported conclusions on slow plaque reaccumulation following donanemab treatment" and as supporting the rationale for limited-duration dosing (§4).
- **Dependencies**: C08
- **Tags**: amyloid-reaccumulation, centiloids, biomarker, exposure-response-model
- **Sources**:
  - Mean (SD) 10.99 (14.41) CL at 154 weeks, below 24.1 CL cutoff ← `paper.pdf` p6 §3.3 «Early-start participants who met treatment course completion criteria by 52 weeks of the placebo-controlled period maintained a mean (SD) amyloid level of 10.99 (14.41) CL at 154 weeks, which is below the 24.1 CL cutoff for amyloid negativity (Fig. 4c)» [result]
  - Reaccumulation rate 2.4 CL/year, from four donanemab studies including this LTE ← `paper.pdf` p6 §3.3 «From data across four donanemab studies (including the results of this LTE), amyloid plaque reaccumulation was calculated to be 2.4 CL/year» [result]
  - "comparable to the natural history of the disease" ← `paper.pdf` p7 §4 «After completing donanemab treatment, the rate of amyloid reaccumulation was comparable to the natural history of the disease [14,15]» [result]

## C11: No new safety signals were observed during the LTE compared to the established donanemab safety profile
- **Statement**: The incidences of death, serious AEs (SAEs), and treatment-emergent AEs (TEAEs) in delayed-start participants dosed in the LTE (placebo→donanemab, N=657) were 1.1%, 19.6%, and 86.5%, respectively; in early-start participants switched to placebo (donanemab→placebo, N=393), 2.0%, 20.4%, and 80.2%; in early-start participants who continued donanemab (donanemab→donanemab, N=157), 1.3%, 13.4%, and 84.7%. Two deaths during the LTE were previously reported: one due to ARIA-E and one due to intracranial hemorrhage following thrombolytic administration where a same-day MRI showed severe ARIA-E.
- **Status**: supported
- **Falsification criteria**: A new, previously uncharacterized AE signal emerges in the LTE safety data that was not part of donanemab's established profile from the placebo-controlled period [2], or the descriptive incidence rates diverge sharply from that established profile.
- **Proof**: [E10]
- **Evidence basis**: Table 1 (full safety overview and AEs of special interest by treatment-sequence group); §3.4 Safety; §4 Discussion.
- **Interpretation**: Event frequencies among early-start participants who continued donanemab in the LTE were generally lower than the frequencies observed for donanemab-treated participants during the placebo-controlled period [2], consistent with declining risk with cumulative exposure/duration off high-frequency early-treatment risk windows.
- **Dependencies**: none
- **Tags**: safety, deaths, SAE, TEAE, ARIA
- **Sources**:
  - Deaths/SAEs/TEAEs: donanemab→placebo 8 (2.0%)/80 (20.4%)/315 (80.2%); donanemab→donanemab 2 (1.3%)/21 (13.4%)/133 (84.7%); placebo→donanemab 7 (1.1%)/129 (19.6%)/568 (86.5%) ← `paper.pdf` p7 Table 1 «Deaths ... 8 (2.0 %) 2 (1.3 %) 7 (1.1 %) ... SAEs ... 80 (20.4 %) 21 (13.4 %) 129 (19.6 %) ... TEAEs ... 315 (80.2 %) 133 (84.7 %) 568 (86.5 %)» [result]
  - Delayed-start (placebo→donanemab) rates 1.1%/19.6%/86.5% narratively; early-start-to-placebo rates 2.0%/20.4%/80.2% ← `paper.pdf` p6-7 §3.4 «The incidences of death, serious AEs, and TEAEs in delayed-start participants who received at least one infusion during the LTE were 1.1 %, 19.6 %, and 86.5 %, respectively» and «The incidences of death, serious AEs, and TEAEs in early-start participants who were switched to placebo infusions ... and received at least one placebo infusion during the LTE were 2.0 %, 20.4 %, and 80.2 %, respectively» [result]
  - Two deaths: ARIA-E and intracranial hemorrhage (post-thrombolytic, same-day MRI showed severe ARIA-E) ← `paper.pdf` p6-7 §3.4 «Two deaths during the LTE period were previously reported [13]; one was due to ARIA-E, and one was due to intracranial hemorrhage. The death due to intracranial hemorrhage occurred following thrombolytic administration in a participant where an MRI scan on the same day showed severe ARIA-E» [result]
  - "no new safety signals were observed during the LTE period compared to the established safety profile of donanemab" ← `paper.pdf` p7 §4 «Importantly, no new safety signals were observed during the LTE period compared to the established safety profile of donanemab» [result]

## C12: ARIA risk declines with cumulative donanemab exposure and after treatment discontinuation
- **Statement**: Among all participants exposed to donanemab, most ARIA-E events occurred within the first 24 weeks of treatment; the incidence of ARIA-E was 1.0% or less in each 6-month interval following a participant's last dose of donanemab, and the risk of ARIA-H continued to decrease after the last dose. Frequencies of symptomatic ARIA-E and symptomatic ARIA-H within any single 6-month post-discontinuation interval did not exceed 0.1% and 0.3%, respectively. Among early-start participants who met treatment course completion criteria by 52 weeks, the frequencies of any ARIA, ARIA-E, and ARIA-H after switching to placebo were 20.3%, 2.0%, and 18.3%, respectively, with no ARIA-related serious AEs; the observation-time-adjusted incidence rates (OAIRs) for these participants were similar to participants who received placebo during the placebo-controlled period (1.0 vs 1.5 for ARIA-E; 10.9 vs 10.4 for ARIA-H).
- **Status**: supported
- **Falsification criteria**: ARIA-E/ARIA-H incidence rates increase (rather than plateau/decrease) with time since last donanemab dose, or the OAIRs for 52-week completers diverge substantially from placebo-period rates.
- **Proof**: [E11]
- **Evidence basis**: §3.4 Safety (Fig. S7, Fig. S8, and Table S5 referenced but not included in the provided PDF — main-text summary numbers used here).
- **Interpretation**: The declining post-discontinuation ARIA risk, converging toward placebo-like OAIRs, supports the safety rationale for limited-duration dosing (once amyloid is cleared and dosing stops, treatment-related imaging-abnormality risk falls toward background levels).
- **Dependencies**: none
- **Tags**: safety, ARIA, OAIR, post-discontinuation
- **Sources**:
  - Most ARIA-E events within first 24 weeks; ARIA-E incidence ≤1.0% per 6-month interval post-last-dose; ARIA-H risk continues to decrease ← `paper.pdf` p7 §3.4 «An analysis of the time to the first ARIA-E event among all participants exposed to donanemab (Fig. S7) revealed that most events occurred within the first 24 weeks of treatment. Fig. S8 shows that the incidence of ARIA-E was 1.0 % or less in each 6-month interval following participants' last dose of donanemab and that the risk of ARIA-H continued to decrease after the last dose of donanemab» [result]
  - Symptomatic ARIA-E ≤0.1%, symptomatic ARIA-H ≤0.3% per 6-month post-discontinuation interval ← `paper.pdf` p7 §3.4 «The frequencies of symptomatic ARIA-E and symptomatic ARIA-H within any single 6-month period did not exceed 0.1 % and 0.3 %, respectively, after the last dose of donanemab» [result]
  - 52-week completers: any ARIA 20.3%, ARIA-E 2.0%, ARIA-H 18.3%, no ARIA-related SAEs; OAIR 1.0/10.9 vs placebo-period 1.5/10.4 ← `paper.pdf` p7 §3.4 «the frequencies of any ARIA, ARIA-E, and ARIA-H after switching to placebo were 20.3 %, 2.0 %, and 18.3 %, respectively, with no ARIA-related serious AEs reported (Table S5). Following treatment course completion by 52 weeks, the OAIRs ... for early-start participants were similar to participants who received placebo during the placebo-controlled period (1.0 for ARIA-E and 10.9 for ARIA-H vs 1.5 for ARIA-E and 10.4 for ARIA-H, respectively)» [result]
