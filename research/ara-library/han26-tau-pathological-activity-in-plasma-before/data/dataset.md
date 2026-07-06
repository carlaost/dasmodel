# Dataset

## Provenance
- **Source**: Prospectively recruited clinical cohort, not a public/released dataset. 76 patients from the Memory Clinic of the Cliniques Universitaires Saint-Luc (Brussels, Belgium) + 69 volunteers drawn from a registry established in another academic study (Methods, PDF p.7).
- **Recruitment window**: June 2019 – April 2025.
- **Access**: Not publicly released. "Request for data for replication studies or meta-analyses can be sent to ... bernard.hanseeuw@uclouvain.be" (Data Availability, PDF p.27).

## Size
- **Total N**: 145 individuals, age >45 (79 CU / 66 CI).
- **Longitudinal subsample**: 88 participants (58 CU / 30 CI), 207 total blood samples, 2–5 timepoints per participant (median 3.0, IQR 2.0–3.0).
- **Missing data** (per-variable, entire sample n=145): episodic memory z-score n=139; entorhinal/inferior-temporal SUVr n=141; plasma pTau181 n=142; plasma pTau231 n=118; ROC analyses further exclude pTau181 (missing=3), pTau231 (missing=27), Aβ42/Aβ40 (missing=6) relative to n=145.

## Licensing / Ethics / Consent
- Ethical Committee approval: UCLouvain #UCL-2016-121 (13 May 2019); Eudra-CT number 2018-003473-94.
- Conducted per the Declaration of Helsinki.
- Written informed consent obtained from all participants (Methods, PDF p.8).

## Variables Collected
- **Demographics**: age at tau-PET, sex, education (years), APOE ε4 carriership.
- **Clinical classification**: CU vs. CI (via 4-domain neuropsychological z-score battery, cutoff z<-1.5), MCI vs. dementia subtype within CI.
- **Amyloid status**: amyloid-PET Centiloid ([18F]Flutemetamol or [11C]PiB, n=101) or CSF Aβ42 (lumbar puncture, n=44); A+ = Centiloid≥20 or CSF Aβ42≤544 pg/mL.
- **Tau-PET**: [18F]MK6240 visual Braak-like stage (0–6); regional SUVr (entorhinal, inferior temporal).
- **Plasma biomarkers**: VeraBIND Tau Score (RLU ratio), pTau217 (pg/mL, Lumipulse), pTau181 (pg/mL, SIMOA), pTau231 (pg/mL, SIMOA), Aβ42/Aβ40 ratio (SIMOA).
- **Cognition**: MMSE (/30), episodic memory z-score, and 3 other domain z-scores (language, executive, visuospatial — collected but not all individually reported as outcome variables in Results).

## Cohort Characteristics (Table 1 summary; see `evidence/tables/table1.md` for full transcription)
- All (N=145): age 70.3±8.4y; 44.8% male; 16.3±3.5 years education; 53.8% APOE ε4+; 50.3% A+; MMSE 26.8±3.6; VeraBIND Tau 1.00±0.23 RLU.
- CU (N=79) vs. CI (N=66): CI patients were significantly older-trending (p=0.07, not significant), less educated (p=0.02), more often A+ (78.8% vs. 26.6%, p<0.001), had lower MMSE (24.3 vs. 28.9, p<0.001), lower episodic memory z-scores, higher tau-PET burden, and higher plasma pTau181/231/217 and VeraBIND Tau levels (all p<0.001).

## Note on Sample Composition
The CU volunteer subsample was deliberately enriched for APOE ε4 carriers to match the CI patient subsample's carriership frequency (Methods, PDF p.7); this is a designed, non-representative sampling choice intended to increase statistical power for detecting preclinical AD biomarker positivity, and is listed by the authors as a generalizability limitation (see `logic/solution/constraints.md`).
