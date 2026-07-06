# Study Design — Registry Census Methodology

This survey builds on the authors' previous AD pipeline studies (Cummings et al. 2024, 2025). It is
a curated census of ClinicalTrials.gov, not an interventional study. Methodology is drawn from
§2 Methods and §3 Results.

## Data collection pipeline
1. **Source**: ClinicalTrials.gov, the US NIH/NLM clinical-trial registry. US trials with ≥1 US
   site, conducted under an FDA IND, or involving a US-manufactured drug must register within 21 days
   of enrolling the first participant.
2. **Access**: Data accessed via the ClinicalTrials.gov API and transferred to the UNLV Clinical
   Trial Observatory and the Cleveland Clinic Laboratory of Network Medicine databases. Raw JSON is
   retrieved as posted and parsed for >30 key data fields.
3. **Curation**: Automated filtering combining rule-based programming and manual expert curation
   identifies and characterizes trials testing AD pharmacological interventions. Extracted and
   annotated data are stored in a PostgreSQL relational database for querying and analysis.
4. **Index Date**: 1 January 2026 — the fixed snapshot date for the census.

## Fields captured per trial
Test-agent name; trial title; NCT identifier; actual start date; projected primary end date; whether
a biomarker is required for eligibility or serves as a primary/secondary outcome; whether the drug is
repurposed (compared against DrugBank, https://go.drugbank.com/); trial location(s); lead sponsor
(industry vs not).

## Inclusion / exclusion rules
- **Included**: Trials active on the Index Date (recruiting, active-not-recruiting, enrolling by
  invitation, not-yet-recruiting) in Phase 1, Phase 1/2, Phase 2, Phase 2/3, or Phase 3. When a trial
  spans two phases, the higher phase is used. Each novel agent is counted once (in the higher phase
  if assessed in more than one).
- **Excluded**: Phase 0 and Phase 4 trials; trials whose participants have dementia of any cause or
  in which AD is included with other dementias; MCI as a manifestation of a non-AD condition;
  non-pharmacologic approaches (exercise, lifestyle, cognitive-behavior therapy, caregiver
  interventions, supplements, medical foods); trials of devices, gene therapies, or stem-cell
  therapies; biomarker trials with no intervention. Suspended/terminated/completed/withdrawn/unknown
  (no update within 2 years) trials are described but not counted in active summaries.

## Classification rules
- **Therapeutic purpose (DTT vs STT)**: Determined from declared therapeutic intent + trial
  characteristics + literature + sponsor. DTTs split into biologics vs small molecules (<500 Da,
  oral). STTs split into cognition-enhancing vs NPS-targeting (with an "other" bucket, e.g., seizures).
- **CADRO target**: Each agent's principal mechanism is mapped to a Common AD Research Ontology
  category, using ClinicalTrials.gov, the literature, and ALZFORUM. Multi-mechanism agents may be
  classified "multitarget".
- **Repurposing**: An agent is repurposed if approved for another indication or repositioned during
  development, judged against DrugBank.

## Analyses reported
Composition by phase; by therapeutic purpose; by CADRO category (overall and per phase); by
continuum stage; by sponsor (industry vs not); by geography (North America / non-North America /
global; unique-site counts by world region); biomarker use (eligibility vs outcome, by modality);
participant demand (by phase and purpose); repurposing (by phase, modality, sponsor); combination
therapies; drugs scheduled to complete Phase 2/3 trials in 2026; and a 10-year longitudinal
trajectory (trial/agent counts and target-class shares, 2017–2026).

## Global site geography (Index Date 1 January 2026)
Unique active trial sites: 3156 in North America and 3607 in non-North American regions, including
1363 in Western Europe/Israel, 661 in Eastern Europe/Russia, 571 in Asia (excluding Japan), 516 in
Japan, 321 in South America/Mexico, and 175 in South Africa/Australia/New Zealand.
