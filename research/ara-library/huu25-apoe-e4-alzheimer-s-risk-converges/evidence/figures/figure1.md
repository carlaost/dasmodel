# Figure 1: Experimental design and annotation of entorhinal cortex (ERC) spatial domains (SpDs)
- **Source**: Figure 1, §2.1–2.2
- **Caption**: "A. Schematic depicting cohort composition (n=30 donors) stratified across APOE genotype, sex and ancestry as well as experimental design for generation of single nucleus RNA-seq (snRNA-seq) and spatially-resolved transcriptomics (SRT) data from postmortem human ERC tissue. Created in BioRender. B. Representative SRT tissue sections showing BayesSpace clusters at k=9 from donors with different APOE genotypes (E2+ versus E4+) and ancestries (African, AA and European, EA). C. Violin plot of APOE log-normalized expression (logcounts) across SpDs. D. spatialLIBD spatial registration heatmap of ERC SpDs compared to reference SpDs in the DLPFC. High confidence matches (cor > 0.5, merge ratio = 0.1) are marked with an 'X'. Related to Figure 2, Fig S1–S14, Fig S43, Table S1–S3."
- **Screenshot**: figure1.png
- **Figure type**: mixed
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Panel A (diagram)**: Cohort cross-tabulation grid — Ancestry (EA/AA rows) × APOE_carrier (E2+/E4+ columns): EA/E2+ = 8 (m7,f1); EA/E4+ = 6 (m6,f0); AA/E2+ = 6 (m3,f3); AA/E4+ = 10 (m5,f5). n=30 neurotypical donors. Workflow arrows: ERC tissue blocks → snRNA-seq (Chromium) → Cell Type Populations (tSNE); and → SRT (Visium, H&E sections) → Spatial Domains.
- **Panel B (qualitative spatial samples)**: 8 representative Visium sections (AA row: Br1556, Br5415, Br5460, Br1039; EA row: Br2582, Br6538, Br5517, Br1706), colored by 9 BayesSpace SpDs; E2+ vs E4+ brackets. Shows laminar + WM organization across donors.
- **Panel C (quantitative_plot, violin)**: APOE logcounts across 9 SpDs. Highest APOE expression in L1~Sp9D5 (astrocyte-enriched L1) with median ≈2.9; other domains median ≈1.5–2.5; WM.uf~Sp9D7 among lowest.
- **Panel D (quantitative_plot, heatmap)**: correlation of ERC SpDs (rows) vs DLPFC reference domains (columns). "X" high-confidence matches: Vasc~Sp9D8↔DLPFC L1 region; L1~Sp9D5↔L1; L2.3~Sp9D1, LD~Sp9D2, Inhib~Sp9D9, L5~Sp9D3 to mid layers; L6~Sp9D4↔L6; WM.uf~Sp9D7 & WM~Sp9D6↔DLPFC WM domains.

## Trend summary
Nine transcriptionally distinct ERC SpDs recovered at k=9; APOE expression peaks in the L1/astrocyte domain; ERC WM domains register to DLPFC WM, but mid GM layers do not cleanly register (reduced ERC lamination). Supports concepts "Spatial domain" and "Spatial registration"; underlies C03 annotation.
