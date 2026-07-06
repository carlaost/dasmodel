# Figure 5: Transcriptome signatures of AD progression in neocortex
- **Source**: Figure 5, §"Differential gene and pathway expression in vulnerable vs resilient neocortex in AD"
- **Caption**: "a 'High-confidence' DE genes were identified using a linear mixed model and either bootstrap, pseudobulk, or hdWGCNA. 'Early' and 'late' DE genes correspond to intermediate vs. low and high vs. intermediate AD pathology… b Bar plots show total numbers of DE genes, upregulated genes, and downregulated genes, identified by a linear mixed model. Downregulation predominates, though early-stage BA17 shows high upregulation… c Heatmap of high-confidence DE genes in BA9 and BA17 excitatory clusters. DE gene counts increase with pathology progression and from BA9 to BA17. SLC17A7 ISH staining shows layer distribution… d UpSet plots show intersecting high-confidence DE genes across regions and stages for six excitatory neuronal subtypes… Genes highlighted in red are differentially expressed in all four conditions. e Heatmap of 54 high-confidence DE genes shared across brain regions and disease stages… f Hierarchical heatmap of functional enrichment… top 50 enriched pathways. g Heatmap of enriched pathways within each excitatory neuronal subtype…"
- **Screenshot**: figure5.png
- **Figure type**: mixed (quantitative bar/UpSet + heatmaps + qualitative ISH)
- **Extraction method**: exact_from_labels (text-stated totals + legible UpSet counts) + visual_description
- **Reading confidence**: medium (dense multi-panel)

## Panel a (diagram)
Workflow: high-confidence DE = LMM ∩ (Bootstrap / Pseudobulk / hdWGCNA); "Early" = Int vs Low, "Late" = High vs Int → Disease Progression Signatures.

## Panel b (bar plots — DE gene counts, LMM)
Directional: downregulation predominates overall; early-stage BA17 shows high upregulation; nuclei counts per cluster provided. Exact per-cluster counts not individually printed (bar heights `≈`).

## Panel d (UpSet plots) — legible intersection totals per subtype
Rows = 4 conditions (BA9 Early, BA9 Late, BA17 Early, BA17 Late); red = shared across all 4.
| Subtype | Selected condition totals (BA9 E / BA9 L / BA17 E / BA17 L) | Red genes (shared all 4) |
|---------|-----------------------------------------------------------|--------------------------|
| Ex1 | 53 / 189 / 54 / 90 | KCND2, KCNQ5, STXBP5L |
| Ex2 | 133 / 103 / 74 / 159 | NALF1, SNTG1, SYN3, TAFA1 |
| Ex3 | 168 / 157 / (…) | ROBO2 |
| Ex5 | 34 / 128 / 89 / (…) | KCNIP4 |
| Ex12 | 32 / 226 / 15 / 77 | (…) |
| Ex16 | 51 / 33 / 82 / (…) | (…) |
(Counts read from the UpSet totals: treat as `≈`; some obscured values left as "…".)

## Panel e (heatmap — 54 shared high-confidence DE genes)
Genes incl. KCNH7, KCNQ5, DLG2, KCNIP4, CDH12, NALF1, RGS6, SNAP91, CSMD1, ADGRB3, CNTNAP2, CACNA1B, NRG3, FGF14, CACNA1C, SYN3, AUTS2, MAGI2, RIMS2, SLC8A1, NRXN1, GRM5, SLC24A2, GRIN2A, COPG2 (…). Pattern: greater changes in BA9 than BA17; BA9 downregulation increases with progression; BA17 upregulation shifts to downregulation with progression. COPG2, SLC24A2 upregulated early in both.

## Panels f,g (functional enrichment heatmaps)
Top-50 pathways incl. synaptic signaling, modulation of chemical synaptic transmission, regulation of synapse organization, cell-cell adhesion, regulation of membrane potential, calcium/sodium/potassium ion transport, intracellular calcium ion homeostasis, glutamate receptor signaling, synaptic vesicle clustering, action potential, brain development. Pattern (g): downregulation in most BA9 subtypes (early & late) and BA17 L2/3 (Ex1–3) late; upregulation early in BA17; Ex5 (BA9 & BA17 early) shares enriched pathways with upregulation.

## Key text-stated quantities
| Quantity | Value |
|----------|-------|
| High-confidence DE genes | 986 |
| Shared across all 4 conditions | 54 |
| Ex5 common BA9/BA17 early | 19 |
| Ex5 common BA9/BA17 late | 9 |
| Parallel (min-500-gene) | 962 (460 overlap, 35 shared all 4) |

## Trend summary
DE-gene burden rises with pathology and is higher in BA9 than BA17; Ex5 is distinctive in early
upregulation; convergent pathways center on synapse/ion/calcium/excitability. Supports C03, C04.
