# Concepts

## Plasma phosphorylated tau (p-tau)
- **Notation**: p-tau (site-specific: p-tau217, p-tau181, p-tau231)
- **Definition**: Tau protein phosphorylated at a specific residue, measurable in blood (plasma or serum), serving as a scalable blood-based biomarker (BBM) of Alzheimer's disease pathology. The phosphorylation site defines the isoform (threonine 217, 181, or 231).
- **Boundary conditions**: Diagnostic utility depends on isoform, analytical platform, sample matrix, and disease stage; validated against CSF or PET reference standards.
- **Related concepts**: p-tau217, p-tau181, p-tau231, AT(N) framework, blood-based biomarker

## p-tau217
- **Notation**: p217 (nodes: p217_MS, p217_Ratio, p217_ALZpath, p217_Lumi, p217_IA, p217_Lilly, p217_Serum, p217_AutoIA)
- **Definition**: Tau phosphorylated at threonine 217. In this NMA it is the top-performing isoform for detecting amyloid-beta pathology, staging tau pathology, and predicting cognitive decline. Reflects a cellular response to amyloid plaques with a larger dynamic range than p-tau181.
- **Boundary conditions**: Performance is highest when measured by mass spectrometry or as an automated p-tau217/Abeta42 ratio.
- **Related concepts**: p-tau, mass spectrometry, p-tau217/Abeta42 ratio, automated immunoassay

## p-tau181
- **Notation**: p181 (node: p181_IA — used as the reference comparator)
- **Definition**: Tau phosphorylated at threonine 181; the original scalable plasma p-tau marker. Serves as the common reference comparator (baseline) in the network geometry.
- **Boundary conditions**: The paper argues standard p-tau181 immunoassay is effectively obsolete for high-precision AD diagnostics (P-score < 0.20 across outcomes).
- **Related concepts**: p-tau217, reference comparator, immunoassay

## p-tau231
- **Notation**: p231 (node: p231_UGOT)
- **Definition**: Tau phosphorylated at threonine 231; hypothesized to rise earliest in the AD continuum, possibly triggered by soluble Abeta aggregates before significant plaque deposition.
- **Boundary conditions**: Advantageous mainly in the preclinical (asymptomatic) subgroup for early amyloidosis; ranks low across the full continuum.
- **Related concepts**: relay hypothesis, preclinical AD, early amyloidosis

## Network meta-analysis (NMA)
- **Notation**: NMA
- **Definition**: A meta-analytic method comparing multiple interventions/tests simultaneously by combining direct (head-to-head) and indirect evidence within a connected network of comparisons, referenced to a common comparator. Here a random-effects frequentist NMA (netmeta) compares biomarker+platform nodes.
- **Boundary conditions**: Requires a connected network; assumes transitivity/consistency across the evidence base; between-study heterogeneity captured by I2.
- **Related concepts**: network geometry, P-score, mean difference, direct/indirect evidence

## P-score (SUCRA analog)
- **Notation**: P-score in [0, 1]
- **Definition**: A frequentist ranking metric (analogous to SUCRA in Bayesian NMA) giving the probability that a treatment/test is better than a competing one, averaged over all competitors. Higher values indicate a higher probability of being the best diagnostic marker.
- **Boundary conditions**: Ranks relative performance within a specific outcome/network; not an absolute accuracy value.
- **Related concepts**: SUCRA, NMA, ranking, network geometry

## Network geometry
- **Notation**: —
- **Definition**: The graph of the evidence network in which nodes are biomarker+platform combinations (node size ∝ total participants) and edges are direct head-to-head comparisons (edge thickness ∝ number of comparisons). Nodes are categorized by epitope (e.g., 217 vs. 181) and platform (MS vs. AutoIA).
- **Boundary conditions**: Distinct networks are built per outcome (e.g., 8 nodes for Abeta detection, 6 nodes for Tau-PET recognition).
- **Related concepts**: NMA, direct/indirect evidence, Figure 2

## Mean difference (MD) in AUC
- **Notation**: MD (with 95% CI)
- **Definition**: The primary effect size in this NMA — the difference in Area Under the Curve between a given biomarker node and the p181_IA reference, estimated by a random-effects model. A CI not crossing 0 indicates a significant difference.
- **Boundary conditions**: AUCs extracted from studies; where CIs were unreported they were calculated from SE or estimated from sample size and p-values.
- **Related concepts**: AUC, forest plot, reference comparator

## Area Under the Curve (AUC)
- **Notation**: AUC
- **Definition**: The area under the receiver-operating-characteristic curve, summarizing a biomarker's ability to discriminate a positive from negative reference-standard status; the primary diagnostic-accuracy metric extracted from each study.
- **Boundary conditions**: Interpreted relative to CSF or PET reference standards; combined across studies via NMA rather than reported as absolute pooled AUCs in the main text.
- **Related concepts**: sensitivity, specificity, diagnostic test accuracy

## p-tau217/Abeta42 ratio
- **Notation**: p217_Ratio (also "ratio-based" / "ratio effect")
- **Definition**: A composite metric dividing p-tau217 by Abeta42 (or non-phospho-tau). Normalizes for inter-individual differences in protein clearance and constitutive tau levels, mitigating confounders such as chronic kidney disease.
- **Boundary conditions**: Provides a significant incremental AUC gain (MD = 0.025; I2 = 0%) over single-analyte assays on automated platforms.
- **Related concepts**: ratio effect, single-analyte assay, automated immunoassay

## Analytical platform (MS vs. immunoassay)
- **Notation**: MS (IP-MS); IA (Simoa, MSD, Lumipulse, ALZpath, Fujirebio, Lilly); AutoIA
- **Definition**: The measurement technology for quantifying plasma p-tau. Immunoprecipitation mass spectrometry (IP-MS) is the specificity benchmark; ultrasensitive and fully automated immunoassays (e.g., Simoa, Lumipulse) offer greater clinical accessibility. AutoIA = automated immunoassay.
- **Boundary conditions**: MS is highest-precision but lowest-throughput; automated IAs bridge the gap for routine use.
- **Related concepts**: IP-MS, Simoa, Lumipulse, network geometry

## Sample matrix (plasma vs. serum)
- **Notation**: plasma; serum (node: p217_Serum)
- **Definition**: The blood fraction analyzed. Plasma requires rapid processing; serum is the standard matrix in routine hospital chemistry. The NMA tests whether serum is a viable substitute.
- **Boundary conditions**: Serum p-tau217 is comparable to plasma (P-score = 0.568) where rapid plasma processing is unavailable.
- **Related concepts**: matrix efficiency, clinical implementation, p-tau217

## AT(N) framework
- **Notation**: AT(N)
- **Definition**: A biological research framework defining Alzheimer's disease by objective biomarkers of Amyloid (A), Tau (T), and Neurodegeneration (N), reflecting the shift from a clinical-syndrome to a biological-construct definition of AD.
- **Boundary conditions**: Underlies the choice of amyloid-/tau-PET and CSF reference standards for validating BBMs.
- **Related concepts**: amyloid-beta, tau pathology, reference standard
