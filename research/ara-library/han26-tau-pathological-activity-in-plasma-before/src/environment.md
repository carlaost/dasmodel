# Environment

- **Language/runtime**: R, version 2022.07.2 (Statistical analysis, PDF p.15: "Statistical analyses were performed using R (2022.07.2)"). No other code/software artifacts (e.g., analysis scripts, notebooks) were released or provided with the paper.
- **Framework**: Not specified in paper beyond base R (no named packages for ROC/DeLong/McNemar/regression are cited in the text).
- **Hardware (wet-lab assay)**:
  - VeraBIND Tau: Qinstruments BioShake iQ plate heater/shaker (with plate-specific thermal adapter, Part No. 1808-0506); Alpaqua Magnum FLX® plate magnet (Solid-Core™ Technology); GloMax® Discover Microplate Reader (luminescence readout).
  - Amyloid-PET: Philips Gemini PET ([18F]Flutemetamol) or Philips Vereos digital PET ([11C]PiB), Philips Healthcare, Amsterdam.
  - Tau-PET: Philips Vereos digital PET-CT ([18F]MK6240).
  - MRI: GE Healthcare SignaTM Premier 3T scanner, 48-channel phased-array head coil, 1×1×1mm resolution.
- **Hardware (compute)**: Not specified in paper (no CPU/GPU details; this is a clinical/statistical analysis, not a compute-intensive modeling study).
- **Imaging software**: PNEURO v4.1 (PMOD LLC Technologies, Zurich) for semi-quantitative PET/Centiloid processing; PetSurfer (a FreeSurfer toolset) for PET-MRI integration and SUVr extraction; Desikan-Killiany cortical atlas for regional parcellation.
- **Data sources**:
  - Clinical cohort: 145 participants recruited at the Memory Clinic of Cliniques Universitaires Saint-Luc (Brussels, Belgium) and via an academic volunteer registry (June 2019–April 2025). Not a public dataset; access via the corresponding author (Data Availability, PDF p.27).
  - Radiotracers: [18F]MK6240 (Lantheus Inc., investigational; synthesized at KU Leuven), [18F]Flutemetamol (VizamylTM, GE Healthcare), [11C]PiB.
  - Assay reagents: VeraBIND™ capture beads and related reagents supplied by ADx Neurosciences NV (A Fujirebio Company, Gent, Belgium); Lumipulse® G pTau217 Plasma RUO assay and CSF Aβ42 assay (Fujirebio); SIMOA pTau-181 Advantage V2.1 (REF 104111), pTau-231 Advantage (REF 102292), Neurology Plex 3A (REF 101995) kits (Quanterix).
- **Key dependencies**: VeraBIND Tau assay performed at Veravas, Inc. (Oakdale, MN) and Access Genetics & OralDNA Labs (Eden Prairie, MN); underlying VeraBIND™ purification technology described in patent PCT/US24/50852 (Soldo, Iqbal, Bergmann & Ansari, filed Oct. 10, 2024).
- **Protocols**: Ethical approval UCLouvain #UCL-2016-121 (13/05/2019; Eudra-CT 2018-003473-94), Declaration of Helsinki compliance, written informed consent. Full VeraBIND Tau wet-lab protocol parameters are captured in `src/configs/assay_protocol.md`.
- **Random seeds**: Not specified in paper (analytical/clinical statistics, not a stochastic simulation or ML training run).
- **Code availability**: No code repository, script, or notebook was released with this preprint. `src/` accordingly contains only this environment file and the assay's concrete protocol parameters (`src/configs/assay_protocol.md`) — no `src/execution/` stub is created, per the ARA rule against re-encoding a prose-only/wet-lab method as fabricated code (the assay's mechanism is instead captured faithfully in `logic/solution/method.md`, mirroring Figure 1).
- **Gap note**: The Methods text twice references material not present in the supplied 48-page PDF: "see Supplemental Material for the APOE genotyping method" (PDF p.7) and "Detailed equipment and supplies to run the assay are provided in the Supplementary Methods section" (PDF p.9). No supplementary/appendix pages were included in the provided input (the PDF's 48 pages run from the title page through Figure 5 and its caption, with no further sections). The APOE genotyping method and the full equipment/supplies list are therefore "Not available from provided input" — flagged here rather than guessed at.
