# Figure 7: KCNIP4 upregulation in resilient L4 neurons
- **Source**: Figure 7, §"Increased KCNIP4 expression is associated with resilience in AD"
- **Caption**: "a Violin plots showing KCNIP4 gene expression across major cell types (left) and excitatory neuronal subtypes from BA9 and BA17 (right). b Violin plots showing KCNIP4 expression across AD disease groups in Ex2 and Ex5 neurons from BA9 and BA17. Log-normalized expression levels of KCNIP4 are shown. c Immunostaining for KCNIP4, EYA4, and NeuN in cryosections from low, intermediate, and high pathology stages illustrating increased expression of KCNIP4 in L4 EYA4+ neurons in BA17. d Quantification of KCNIP4 protein expression levels in L4 EYA4+ neurons, L4 EYA4− neurons, and L2/3 neurons from BA17 across disease stages (n = 6 donors per disease group). Data are shown as median ± IQR; whiskers represent minimum and maximum values. One-way ANOVA with two-sided Tukey's test… (*p < 0.05; ***p < 0.001; ****p < 0.0001; exact p-values in the Source Data file). Scale bars: 200 µm (low mag); 30 µm (high mag)."
- **Screenshot**: figure7.png
- **Figure type**: mixed (violin plots + IHC micrographs + boxplot quantification)
- **Extraction method**: visual_description + exact_from_labels (significance tiers, n) — no printed per-value labels
- **Reading confidence**: high (significance/labels); medium (violin/box levels read `≈`)

## Panel a (violin plots)
- Left: KCNIP4 expression by major cell type — highest in excitatory neurons and OPCs; also microglia; low in astrocytes/vascular. (Log-normalized; y ~0–7.)
- Right: KCNIP4 across Ex1–Ex18 in BA9 and BA17 — expressed in most excitatory subtypes except Ex14 (L5/6 NP).

## Panel b (violin plots — KCNIP4 by disease group, Ex2/3 vs Ex5)
- Ex5: KCNIP4 estimated mean expression increases Low→High (consistent with resilience) in both BA9 and BA17.
- Ex2/3 (vulnerable): flat/decreasing pattern. (Levels read `≈` from violins.)

## Panel c (IHC micrographs)
DAPI / NeuN / EYA4 / KCNIP4 / merge in BA17 L4 across low, intermediate, high pathology; KCNIP4 visibly increased in EYA4+ L4 cells at intermediate/high.

## Panel d (boxplot quantification, n=6 donors/group; ANOVA + Tukey)
| Comparison | Result (significance tier) |
|-----------|-----------------------------|
| L4 EYA4+ neurons: Int vs Low | * (higher at intermediate) |
| L4 EYA4+ neurons: High vs Low / Int vs High | ns |
| L2/3 neurons: Int vs Low | * (lower); High vs Low *** (lower) |
| L2/3 neurons: Int vs High | ns |
| KCNIP4 intensity all stages: L4 EYA4+ vs L4 EYA4− | **** |
| KCNIP4 intensity all stages: L4 EYA4+ vs L2/3 | **** |
| L4 EYA4− vs L2/3 | ns |

(Exact p-values in Source Data; only significance tiers shown here.)

## Trend summary
KCNIP4 (RNA and protein) is elevated in resilient L4 EYA4+ neurons — peaking at intermediate stage —
and reduced in vulnerable L2/3 neurons, mirroring the transcriptomic divergence. Supports C05, C06.
