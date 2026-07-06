# Problem Specification

## Observations

### O1: Single-site p-tau is an established but incomplete AD biomarker
- **Statement**: CSF and plasma tau phosphorylated at single sites (p-tau181, p-tau205, p-tau212, p-tau217, p-tau231) discriminate AD from controls and other neurodegenerative diseases with high accuracy, with p-tau217 and p-tau231 possibly outperforming p-tau181 as early-AD markers.
- **Evidence**: Introduction + Discussion; refs 6–11, 7,10,12–20,31,32.
- **Implication**: Site-specific phosphorylation carries diagnostic signal, but only one site at a time has been measured in fluids.

### O2: Tau carries >50 phosphorylation sites and multiple concurrent PTMs
- **Statement**: Diverse tau post-translational modifications (PTMs), including more than 50 phosphorylation sites, have been identified; their physiological/pathological roles are not fully understood.
- **Evidence**: Introduction; refs 24–26.
- **Implication**: The full information content of tau phosphorylation is not captured by single-site assays.

### O3: Doubly/triply phosphorylated tau peptides are enriched in AD brain and body fluids
- **Statement**: Post-mortem mass-spectrometry studies show significantly elevated doubly- and triply-phosphorylated peptides in both soluble and insoluble fractions of AD brain tissue; peptides carrying multiple phosphorylations within the 181–231 sequence are frequently identified; indirect immunoprecipitation evidence (Ashton et al.) shows doubly phosphorylated species in CSF.
- **Evidence**: Discussion; refs 34, 24,26,33, 18.
- **Implication**: Multiphosphorylated tau proteoforms exist in fluids and could be measured directly.

### O4: Tau phosphorylation follows site-specific trajectories along disease progression
- **Statement**: A pattern of CSF tau staging has been proposed with site-specific phosphorylation changes following distinct trajectories over time (e.g., p-tau217 increase precedes p-tau181; both temporally associated with amyloid pathology).
- **Evidence**: Introduction/Discussion; ref 29 (Barthélemy et al.).
- **Implication**: Concurrent multi-site phosphorylation may serve as an enhanced proxy for disease stage.

## Gaps

### G1: Multiphosphorylated tau has never been measured directly as a fluid biomarker
- **Statement**: The diagnostic and prognostic value of tau simultaneously phosphorylated at two different sites, and its added value versus single-site p-tau, is unexplored in body fluids.
- **Caused by**: O1, O2, O4.
- **Existing attempts**: Mass spectrometry (destructive, brain tissue; indirect immunoprecipitation in fluids, ref 18).
- **Why they fail**: No immunoassay existed that requires two concurrent phosphorylations to produce a signal; single-site assays cannot report co-occurrence of phosphorylations on the same molecule.

### G2: CSF-vs-plasma processing of tau proteoforms is poorly understood
- **Statement**: Whether tau proteoforms are processed identically in CSF and plasma, and whether a fluid marker's diagnostic behavior transfers between matrices, is unknown.
- **Caused by**: O3 (fragment/truncation patterns differ between compartments).
- **Existing attempts**: Studies of single-site markers report matrix differences but not for doubly phosphorylated species.
- **Why they fail**: No assay for doubly phosphorylated tau existed to compare matrices.

## Key Insight
- **Insight**: A sandwich immunoassay whose **capture** and **detector** antibodies each target a *different* phosphorylation site will only generate signal when a single tau molecule carries *both* phosphorylations simultaneously — turning a pair of single-site antibodies into a direct, specific readout of a doubly phosphorylated proteoform.
- **Derived from**: O2, O3 (multiphosphorylated species exist) + the sandwich-assay geometry.
- **Enables**: Two Simoa assays — C231D181 (capture p-tau231 / detect p-tau181) and C231D217 (capture p-tau231 / detect p-tau217) — measuring p-tau181&231 and p-tau217&231 in CSF and plasma.

## Assumptions
- A1: Capture and detector antibodies retain their single-site specificity when used together, so signal reflects genuine double phosphorylation (supported by the single-site-peptide-mix control returning blank signal).
- A2: A+/T+ CSF profile (NIA-AA A/T/N framework) is a valid ground-truth definition of the AD continuum against which biomarker accuracy is measured.
- A3: In-house University of Perugia cohorts (discovery + validation) are representative enough to estimate diagnostic performance, acknowledged as small especially for pre-AD.
- A4: Calibrator-based concentrations from custom synthetic peptides (not absolutely quantified) give relative but not definitive absolute concentrations.
