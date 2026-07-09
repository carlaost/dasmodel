# Breakthrough metric vs blind expert panel — recent corpus


**Headline: Spearman = -0.118, Pearson = -0.066** over 55 recent AD papers.
The current GRO significance signal has ~zero (slightly negative) correlation with blind expert judgement.

- Panel: 3 blind domain-expert judges/paper (trialist, neuroscientist, metascientist), 0-100 breakthrough score.
- Metric: significance = 0.40*contribution + 0.40*delta + 0.20*anchor, from GRO L8 sidecars.
- Caveats: 55/66 papers joined (session limit cut 11 tail papers); only 11/51 sota_anchors were genuinely re-resolved (rest still compiler_estimated=0.20); this is the OLD formula the design tournament was meant to replace.

## The failure is systematic (Goodhart)
- Metric ranks annual **facts-and-figures reports** and review/pipeline papers at the TOP (sig 0.62-0.69); experts rate them 4-8/100.
- Metric ranks genuine **single-cell / spatial / molecular discoveries** LOW (sig 0.17-0.29); experts rate them 63-75/100.
- Lone agreement: **aki26** (molecular resilience) sig 0.80 & expert 70 — the one paper whose anchor was re-resolved to a sparse neighborhood. Weak signal that real anchors help.

| expert | sig | anchor | contrib | delta | paper |
|---|---|---|---|---|---|
| 75 | 0.286 | 0.20 | 0.511 | 0.105 | liu25i-single-cell-multiregion-epigenomic-re |
| 73 | 0.281 | 0.20 | 0.498 | 0.105 | ols25-microglial-mechanisms-drive-amyloid-cl |
| 70 | 0.797 | 1.00 | 0.592 | 0.900 | aki26-molecular-signatures-of-resilience-to- |
| 69 | 0.260 | 0.05 | 0.625 | 0.000 | han26-tau-pathological-activity-in-plasma-be |
| 69 | 0.231 | 0.05 | 0.553 | 0.000 | ard25-response-of-spatially-defined-microgli |
| 65 | 0.280 | 0.20 | 0.495 | 0.105 | ji25-alzheimer-s-disease-patient-brain-extra |
| 63 | 0.170 | 0.05 | 0.294 | 0.105 | sal26-plasma-emtbr-tau243-and-p-tau217 |
| 60 | 0.294 | 0.20 | 0.530 | 0.105 | huu25-apoe-e4-alzheimer-s-risk-converges |
| 58 | 0.289 | 0.20 | 0.516 | 0.105 | ave25-uncovering-plaque-glia-niches-in-human |
| 57 | 0.286 | 0.20 | 0.511 | 0.105 | gon25b-stereo-seq-of-the-prefrontal-cortex |
| 54 | 0.386 | 0.20 | 0.516 | 0.350 | gau25-single-nucleus-and-spatial-transcripto |
| 53 | 0.421 | 1.00 | 0.449 | 0.105 | ada26-adult-human-ex-vivo-brain-slices |
| 51 | 0.226 | 0.20 | 0.115 | 0.350 | kes25-the-alzheimer-s-disease-diagnosis-and |
| 49 | 0.265 | 0.20 | 0.493 | 0.070 | val25-blood-biomarkers-of-alzheimer-s-diseas |
| 49 | 0.350 | 0.60 | 0.470 | 0.105 | sal25-trailblazer-alz-4-a-phase-3 |
| 48 | 0.320 | 0.05 | 0.424 | 0.350 | the25-blood-phosphorylated-tau-for-the-diagn |
| 44 | 0.242 | 0.20 | 0.401 | 0.105 | bec25-a-neuroimmune-cerebral-assembloid-mode |
| 37 | 0.340 | 0.60 | 0.446 | 0.105 | tit26-automated-high-throughput-quantificati |
| 36 | 0.618 | 0.20 | 0.446 | 1.000 | jes26-efficacy-and-safety-of-donanemab-in |
| 36 | 0.384 | 0.20 | 0.511 | 0.350 | smi25-contribution-of-modifiable-midlife-and |
| 34 | 0.534 | 1.00 | 0.485 | 0.350 | aku25b-effects-of-medicare-predictors-in-hea |
| 30 | 0.487 | 0.60 | 0.567 | 0.350 | sim26-multi-modal-graph-neural-network-with |
| 29 | 0.213 | 0.05 | 0.508 | 0.000 | che26-diagnostic-performance-of-plasma-p-tau |
| 27 | 0.277 | 0.60 | 0.287 | 0.105 | pal25-alzheimer-s-association-clinical-pract |
| 25 | 0.184 | 0.05 | 0.329 | 0.105 | div25-the-microcirculation-the-blood-brain-b |
| 24 | 0.288 | 1.00 | 0.116 | 0.105 | ali26-privacy-preserving-multimodal-fusion-f |
| 24 | 0.374 | 1.00 | 0.329 | 0.105 | che25e-apoe4-reprograms-microglial-lipid-met |
| 24 | 0.420 | 1.00 | 0.200 | 0.350 | ali25-multimodal-self-supervised-learning-fo |
| 22 | 0.296 | 0.60 | 0.335 | 0.105 | als25-the-role-of-glial-cell-senescence |
| 21 | 0.266 | 0.20 | 0.460 | 0.105 | bor25b-harmonized-prevalence-estimates-of-de |
| 20 | 0.407 | 1.00 | 0.167 | 0.350 | alb26-early-detection-of-alzheimer-s-disease |
| 17 | 0.441 | 1.00 | 0.496 | 0.105 | afi25-vision-and-convolutional-transformers- |
| 17 | 0.318 | 1.00 | 0.191 | 0.105 | aks25-an-explainable-web-based-diagnostic-sy |
| 17 | 0.261 | 0.20 | 0.448 | 0.105 | amo25-regional-differences-in-the-incidence- |
| 16 | 0.207 | 0.20 | 0.312 | 0.105 | iac25-a-practical-overview-of-the-use |
| 14 | 0.160 | 0.05 | 0.304 | 0.070 | kho25-explainable-artificial-intelligence-in |
| 14 | 0.212 | 0.20 | 0.325 | 0.105 | qi25-alzheimer-s-disease-digital-biomarkers- |
| 11 | 0.296 | 0.60 | 0.335 | 0.105 | gie25-geographical-inequalities-in-dementia- |
| 10 | 0.382 | 1.00 | 0.386 | 0.070 | aku25-population-attributable-fractions-asso |
| 10 | 0.184 | 0.05 | 0.329 | 0.105 | raz25-advancements-in-deep-learning-for-earl |
| 10 | 0.370 | 1.00 | 0.321 | 0.105 | sor25-barriers-for-access-and-utilization-of |
| 9 | 0.294 | 0.60 | 0.329 | 0.105 | ahm26-machine-learning-and-deep-learning-for |
| 8 | 0.407 | 1.00 | 0.412 | 0.105 | als26-early-onset-alzheimer-s-disease-mortal |
| 8 | 0.362 | 1.00 | 0.300 | 0.105 | ala26-trends-in-alzheimer-s-disease-mortalit |
| 8 | 0.608 | 0.20 | 0.480 | 0.940 | cum26-alzheimer-s-disease-drug-development-p |
| 7 | 0.488 | 1.00 | 0.370 | 0.350 | ahm26b-trends-and-disparities-in-alzheimer-d |
| 7 | 0.188 | 0.20 | 0.265 | 0.105 | cav25-global-societal-burden-of-alzheimer-s |
| 7 | 0.251 | 0.20 | 0.422 | 0.105 | hao25-trend-analysis-and-future-predictions- |
| 6 | 0.425 | 0.60 | 0.413 | 0.350 | ant26-mapea-project-evolution-of-care-for |
| 6 | 0.189 | 0.20 | 0.303 | 0.070 | guo25c-the-disease-burden-risk-factors-and |
| 6 | 0.336 | 0.20 | 0.390 | 0.350 | wan25c-global-burden-of-alzheimer-s-disease |
| 6 | 0.242 | 0.05 | 0.230 | 0.350 | liu25h-global-burden-of-alzheimer-s-disease |
| 5 | 0.616 | 0.60 | 0.479 | 0.760 | 20226-2026-alzheimer-s-disease-facts-and |
| 5 | 0.326 | 0.20 | 0.365 | 0.350 | ami25-prevalence-deaths-and-disability-adjus |
| 4 | 0.689 | 1.00 | 0.422 | 0.800 | 20225-2025-alzheimer-s-disease-facts-and |
