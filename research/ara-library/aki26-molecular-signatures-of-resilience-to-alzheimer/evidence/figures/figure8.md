# Figure 8: AAV-mediated delivery of Kcnip4 in excitatory neurons reduces hyperexcitability in vitro and in a humanized mouse model of AD
- **Source**: Figure 8, §"Increased KCNIP4 expression is associated with resilience in AD" (in vitro/in vivo)
- **Caption**: "a In vitro approach to evaluate AAV-mediated Kcnip4 overexpression on neural activity… using calcium imaging. b Representative neuronal Ca2+ transients (ΔF/F₀) at DIV 14 for each condition. c Quantification of Ca2+ transient frequency… (4 wells per condition, 2 fields per well, 3 GFP-positive neurons per field). d In vivo approach… in AppSAA and WT mice… e Western blot… KCNIP4 levels… two doses of Kcnip4 AAV (n = 3 per group). f Representative images… quantification of transduction efficiency in SSC. g−i… cortical amyloid beta, GFAP, and IBA1 immunostaining in AppSAA mice treated with Kcnip4 AAV or control AAV (6−7 mice per group). j… GFP and c-Fos. k Percentage of c-Fos-positive cells in all cortical neurons across study groups. l−o Quantification of c-Fos in GFP+ vs GFP− neurons… (5−7 mice per group). p… GFP and Arc. q Mean Arc staining intensity in all cortical neurons… r−u, Quantification of Arc… in GFP+ vs GFP− neurons… Data shown as median ± IQR. Two-sided t-test / one-way ANOVA + Tukey (*p<0.05; **p<0.01, ***p<0.001, ****p<0.0001)."
- **Screenshot**: figure8.png
- **Figure type**: mixed (vector schematics + Ca2+ traces + Western blot + IHC micrographs + violin/box quantification)
- **Extraction method**: visual_description + exact_from_labels (significance tiers, doses, n) — no printed per-value labels
- **Reading confidence**: high (design/significance); medium (violin levels read `≈`)

## Panel a (diagram)
AAV constructs: Kcnip4 AAV = PHP.eB-CaMKIIa-Kcnip4-P2A-EGFP; Ctrl = PHP.eB-CaMKIIa-EGFP; jRGECO1a AAV = PHP.eB-Syn-jRGECO1a. Timeline: DIV0 → DIV7 AAV transduction → DIV12 Aβ1–42 oligomers (200 nM) → DIV14 calcium imaging.

## Panels b,c (calcium imaging — Ca2+ transient frequency, DIV14)
Conditions: Ctrl AAV, Kcnip4 AAV, Ctrl AAV + Aβ1–42, Kcnip4 AAV + Aβ1–42.
| Comparison | Result |
|-----------|--------|
| Ctrl AAV vs Kcnip4 AAV | * (Kcnip4 lower) |
| Ctrl AAV vs Ctrl AAV+Aβ | *** (Aβ raises) |
| Ctrl AAV+Aβ vs Kcnip4 AAV+Aβ | **** (Kcnip4 lowers under Aβ) |
| Kcnip4 AAV vs Kcnip4 AAV+Aβ | **** |
Kcnip4 reduces transient frequency basally and under Aβ (traces visibly sparser). (Approx. values `≈`; y-axis "Ca2+ transient frequency", events/min.)

## Panel e (Western blot, n=3/group)
KCNIP4 (36 kDa) vs GAPDH (22 kDa label as shown); Ctrl AAV 1e11 vs Kcnip4 AAV 5e10 vs Kcnip4 AAV 1e11 vg. Higher dose (1e11) → significant KCNIP4 increase (* vs control); 5e10 ns.

## Panel f (transduction efficiency, SSC)
~10% GFP+ neurons in SSC across the four groups (all pairwise ns).

## Panels g–i (pathology, 6–7 mice/group)
| Marker | Kcnip4 AAV vs Ctrl AAV (AppSAA) |
|--------|-------------------------------|
| Amyloid-β (anti-human) stained area | ns |
| GFAP stained area | ns |
| IBA1 stained area | * (decreased; reduced microgliosis) |

## Panels j–o (c-Fos, 5–7 mice/group)
- k (all neurons): Ctrl AAV WT vs Ctrl AAV AppSAA ** ; Ctrl AAV AppSAA vs Kcnip4 AAV AppSAA ** / *** (AppSAA elevation reversed by Kcnip4).
- l Ctrl AAV WT (GFP+ vs GFP−): ns; m Kcnip4 AAV WT: ns; n Ctrl AAV AppSAA: ns; **o Kcnip4 AAV AppSAA: * (GFP+ lower than GFP−).**

## Panels p–u (Arc, 5–7 mice/group)
- q (all neurons): Ctrl AAV WT vs Kcnip4 AAV WT * ; WT vs AppSAA **** ; Ctrl AAV AppSAA vs Kcnip4 AAV AppSAA **** ; (AppSAA elevation reversed).
- r Ctrl AAV WT: ns; s Kcnip4 AAV WT: ns; t Ctrl AAV AppSAA: ns; **u Kcnip4 AAV AppSAA: * (GFP+ lower Arc than GFP−).**

## Trend summary
Kcnip4 overexpression lowers neuronal hyperactivity (Ca2+ in vitro; c-Fos/Arc in vivo, specifically
in transduced GFP+ AppSAA neurons) and modestly reduces microgliosis, without altering amyloid
burden or astrogliosis. Supports C07, C08; the amyloid/GFAP null results ground dead-end N19.
