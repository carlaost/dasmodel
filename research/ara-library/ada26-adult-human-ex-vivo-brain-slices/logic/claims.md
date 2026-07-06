# Claims

> Grounding: abstract-only. Each `Statement` is phrased at the level the **abstract** asserts;
> `Status` is `author-asserted` because the full-text evidence (figures, statistics, methods) could
> not be retrieved. Load-bearing numbers/enumerations are grounded in the verified analysis repo
> (`[input]` = value defined in code/config). No quantitative *results* are claimed here — those
> would require the unavailable full text and live (where filable) in `evidence/`.

## C01: Adult human organotypic slice cultures preserve architecture and mature cell identity over weeks
- **Statement**: Organotypic brain slice cultures prepared from adult human neurosurgical resection
  tissue preserve tissue architecture and mature cell identities over a culture window of weeks.
- **Status**: author-asserted (full text unavailable to verify quantitatively)
- **Falsification criteria**: If cultured slices lost mature cell-type marker expression, showed
  disrupted laminar/tissue architecture, or dedifferentiated within the culture window, the claim
  fails.
- **Proof**: [E01]
- **Evidence basis**: Abstract states cultures "preserve tissue architecture and mature cell
  identities over weeks." The snRNA-seq script defines and groups by eight mature CNS cell types
  via canonical markers, consistent with resolved mature identities.
- **Interpretation**: "Preservation over weeks" is the authors' summary; the exact number of weeks
  and the quantitative fidelity metrics are Not available from provided input (no full text).
- **Dependencies**: none
- **Tags**: platform, organotypic culture, cell identity
- **Sources**:
  - 8 mature cell types with canonical markers ← `src/execution/sNucRNAseq_plots.R:37` «Astrocytes = c("SLC1A2","SLC1A3","ALDH1L1","SLC4A4","AQP4","CD44","GFAP"),» (first of the 8-entry `Molecular_markers` list: Astrocytes, Endothelial, Ex.neurons, In.neurons, Microglia, Oligos, OPCs, Perivascular_cells) [input]
  - "preserve tissue architecture and mature cell identities over weeks" ← metadata.md abstract «Cultures preserve tissue architecture and mature cell identities over weeks» [input]

## C02: Cultures elicit stimulus-specific transcriptional programs to diverse stressors
- **Statement**: The slice cultures mount stimulus-specific transcriptional programs in response to
  diverse stressors; the perturbation panel comprises Control, BLM, H₂O₂, LPS, and TNFα.
- **Status**: author-asserted (full text unavailable to verify quantitatively)
- **Falsification criteria**: If transcriptional responses to the different stressors were
  indistinguishable (no stimulus-specific separation), the claim fails.
- **Proof**: [E02]
- **Evidence basis**: Abstract ("elicit stimulus-specific transcriptional programs to diverse
  stressors"). The bulk analysis script performs LDA and WGCNA over exactly the five treatment
  conditions and separates programs by treatment.
- **Interpretation**: The abstract asserts stimulus specificity; the degree of separation (LDA
  variance, program-trait correlations) is quantitative and Not available from provided input.
- **Dependencies**: none
- **Tags**: stimulus specificity, bulk RNA-seq, WGCNA, LDA
- **Sources**:
  - 5 treatment conditions (Control, BLM, H2O2, LPS, TNF) ← `src/execution/bulk_treatments_plots.R:20` «treatments <- c("Control", "BLM", "H2O2", "LPS", "TNF")» [input]

## C03: TNFα drives a coordinated multicellular glial response with pro-/anti-inflammatory loops
- **Statement**: TNFα stimulation elicits a coordinated response across the glial compartment —
  microglia, astrocytes, and OPCs — that includes pro- and anti-inflammatory feedback loops among
  these cell types.
- **Status**: author-asserted (full text unavailable to verify quantitatively)
- **Falsification criteria**: If the three glial types responded independently (no coordinated /
  reciprocal signaling) or showed no anti-inflammatory component, the claim fails.
- **Proof**: [E03, E06]
- **Evidence basis**: Abstract ("resolve coordinated glial responses to TNFα … including pro-/anti-
  inflammatory loops among microglia, astrocytes, and OPCs"). The snRNA-seq script computes
  cell-type-specific TNF-vs-control differential expression specifically for microglia, astrocytes,
  and OPCs.
- **Interpretation**: The loop structure is inferred by the authors from DE + cell-cell
  communication analysis; the specific ligand–receptor edges constituting the loops are Not
  available from provided input (see C06 for the MultiNicheNet analysis that would support them).
- **Dependencies**: C01, C02
- **Tags**: TNFα, microglia, astrocytes, OPCs, neuroinflammation
- **Sources**:
  - the three glial types analysed = microglia, astrocytes, OPCs ← `src/execution/sNucRNAseq_plots.R:158` «glia_types <- c("microglia", "astrocytes", "opcs")» [input]
  - candidate shared TNF-response genes ← `src/execution/sNucRNAseq_plots.R:46` «gene_list <-c("NAMPT","SOD2","WTAP","IRAK1","NFKB1","PARP14","TNFAIP2","TNIP1")» [input]

## C04: The slice-derived TNFα glial response is validated in postmortem human brain (and external datasets)
- **Statement**: The coordinated glial TNFα response observed ex vivo is recapitulated in postmortem
  human brain, and the slice-derived TNFα signatures are validated against external datasets.
- **Status**: author-asserted (full text unavailable to verify quantitatively)
- **Falsification criteria**: If the ex-vivo TNFα signatures showed no correspondence with
  postmortem human brain or the external validation datasets, the claim fails.
- **Proof**: [E04]
- **Evidence basis**: Abstract ("validated in postmortem human brains"). Repo README states
  validation "in external datasets (mouse microglia, human iPSC-derived astrocytes, COVID-19
  postmortem brains, and large AD snRNA-seq cohorts)."
- **Interpretation**: The abstract highlights postmortem human brain; the repo enumerates a broader
  set of external datasets. The statistical concordance metrics are Not available from provided
  input.
- **Dependencies**: C03
- **Tags**: external validation, postmortem brain, COVID-19, Alzheimer's disease
- **Sources**:
  - "validated in postmortem human brains" ← metadata.md abstract «resolve coordinated glial responses to TNFα (validated in postmortem human brains)» [input]

## C05: WGCNA of bulk RNA-seq defines shared and stimulus-specific gene programs
- **Statement**: Weighted gene co-expression network analysis (WGCNA) of the bulk RNA-seq defines a
  set of gene programs (Prog.1–Prog.5) that capture shared and stimulus-specific responses, whose
  correlation with each treatment is testable.
- **Status**: author-asserted (full text unavailable to verify quantitatively)
- **Falsification criteria**: If WGCNA yielded no programs whose activity correlated specifically
  with individual treatments, the claim fails.
- **Proof**: [E02]
- **Evidence basis**: The bulk script builds a program-trait correlation heatmap over five programs
  (Prog.1–Prog.5) and five treatments, annotating significance stars; README states WGCNA defines
  "shared and stimulus-specific gene programs and their functional annotation across treatments."
- **Interpretation**: Five programs are the set selected/displayed in the released script; whether
  the full WGCNA produced additional modules is Not available from provided input.
- **Dependencies**: C02
- **Tags**: WGCNA, gene program, bulk RNA-seq, pathway enrichment
- **Sources**:
  - 5 programs Prog.1–Prog.5 ← `src/execution/bulk_treatments_plots.R:55` «selected_rows <- c("Prog.1","Prog.2","Prog.3","Prog.4","Prog.5") » [input]
  - 5 treatment columns ← `src/execution/bulk_treatments_plots.R:54` «selected_cols <- c("Control", "BLM", "H2O2", "LPS", "TNF")» [input]

## C06: MultiNicheNet prioritizes ligand–receptor interactions differing between TNFα and control
- **Statement**: MultiNicheNet-based cell-cell communication analysis, comparing TNFα-treated and
  control slices, prioritizes ligand–receptor interactions that underlie the coordinated glial
  crosstalk.
- **Status**: author-asserted (full text unavailable to verify quantitatively)
- **Falsification criteria**: If no ligand–receptor interactions were differentially prioritized
  between TNFα and control, the claim fails.
- **Proof**: [E06]
- **Evidence basis**: Repo README ("MultiNicheNet-based cell-cell communication analysis comparing
  TNFα-treated and control slices, and prioritization of ligand-receptor interactions").
  Supplementary Table 5 sheet is titled "TNF signaling analysis" / "MultiNicheNet signaling
  network … Prioritization of top ligand–receptor …".
- **Interpretation**: The specific prioritized interactions are contained in Supplementary Table 5
  (bundled xlsx) but were not transcribed here; the abstract's "pro-/anti-inflammatory loops" (C03)
  are the biological interpretation of these edges.
- **Dependencies**: C03
- **Tags**: cell-cell communication, MultiNicheNet, ligand-receptor
- **Sources**:
  - MultiNicheNet TNFα-vs-control comparison + ligand-receptor prioritization ← README.md «MultiNicheNet‑based cell-cell communication analysis comparing TNFα-treated and control slices, and prioritization of ligand-receptor interactions.» [input]
