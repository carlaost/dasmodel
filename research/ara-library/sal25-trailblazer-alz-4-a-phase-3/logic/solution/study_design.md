# Study Design — TRAILBLAZER-ALZ 4

Directional description of the trial design (arms, endpoints, population, analysis flow). NO endpoint results here — exact results live in `evidence/`.

## Overview
- **Type**: Phase 3, randomized, open-label, parallel-group, multicenter, active-comparator superiority trial.
- **Duration**: 76 weeks.
- **Sites**: 31 sites in the United States.
- **Dates**: Initiated September 24, 2021; completed September 19, 2023. (Registration NCT05108922; see `logic/related_work.md` RW01 and `src/environment.md`.)
- **Sponsor/funding**: Eli Lilly and Company.
- **Oversight**: Conducted per Declaration of Helsinki and ICH-GCP; protocol and SAP approved by an independent ethics committee/IRB at each site; written informed consent obtained.

## Arms (randomized 1:1)
- **Donanemab**: intravenous, once every 4 weeks — 700 mg for the first three doses, then 1400 mg thereafter. Participants meeting donanemab dosing-cessation criteria stopped infusions but continued all other assessments.
- **Aducanumab**: intravenous, per the US ADUHELM (aducanumab-avwa) package insert (weight-based dosing).
- **Randomization stratification**: by amyloid level and APOE ε4 status (non-carrier / heterozygous / homozygous).

## Population
- **Inclusion**: age 50–85; early symptomatic AD (MCI or mild dementia); MMSE 20–30; CDR Global Score 0.5 or 1.0; amyloid pathology by florbetapir F18 PET (positive visual scan and ≥37 CL, or negative visual scan and ≥50 CL). Baseline flortaucipir F18 PET performed but not used for eligibility.
- **Key exclusions**: pre-existing ARIA-E; > 4 cerebral microhemorrhages; > 1 area of superficial siderosis; any intracerebral hemorrhage > 1 cm; severe white-matter disease; bleeding disorder or platelet-antiaggregant/anticoagulant use (aspirin ≤ 325 mg/day permitted).
- **Disposition** (Figure 1): 441 assessed → 293 screen-failed → 148 randomized (74/74) → overall analysis populations 71 (donanemab) / 69 (aducanumab); 113 (80.7%) completed.

## Analysis sets
1. **Overall population** — all randomized participants with baseline + ≥1 postbaseline florbetapir PET.
2. **Low–medium tau subpopulation** — overall-population participants with baseline flortaucipir PET meeting low–medium tau criteria.
3. **Safety analysis set** — all participants exposed to study treatment.

## Endpoints
- **Co-primary**: superiority of donanemab vs aducanumab in the proportion reaching AP clearance (< 24.1 CL, florbetapir PET) at 6 months, in (1) the overall population and (2) the low–medium tau subpopulation.
- **Key secondary**: time to AP clearance; mean absolute change from baseline in AP at 6, 12, 18 months (percent change modeled analogously).
- **Additional secondary**: AP clearance proportions at 12 and 18 months.
- **Exploratory**: plasma biomarkers (p-tau217, p-tau181, GFAP, NfL).
- **Safety**: AEs (spontaneously reported), labs, ECG, exams, centrally read MRI, C-SSRS; ARIA-E, ARIA-H, and infusion-related reactions as AEs of special interest.

## Statistical framework
- Co-primary: logistic regression (treatment + APOE ε4 status + baseline amyloid + baseline age).
- Mean change: ANCOVA at 6 months; MMRM at 12/18 months.
- Time to clearance: Kaplan–Meier + 2-sided unstratified log-rank test.
- Biomarkers: MMRM on log-transformed values.
- Multiplicity: gated hierarchy after both co-primary endpoints significant — mean change at 6 mo → 12 mo → time to clearance (at study completion) → mean change at 18 mo. Two-sided α = 0.05. Software: SAS v9.4.
- Planned enrollment ≈ 200 (≈50% low–medium tau), powered ≥98% for co-primary superiority at 6 months (actual randomized 148).

## Blinding note
Open-label for participants and investigators (may affect safety reporting), but MRI schedules were identical across arms and MRI + amyloid PET reads were centrally blinded, protecting the imaging endpoints.
