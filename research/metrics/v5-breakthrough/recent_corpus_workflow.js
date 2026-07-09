export const meta = {
  name: 'breakthrough-recent-corpus',
  description: 'Recency-controlled breakthrough experiment: GRO-compile the L8 shape over 67 recent (2025-26) Alzheimer ARAs, get a blind informed-agent full-read breakthrough rating per paper + a 2nd reader on a subset, compute the metric, and correlate metric vs informed rating',
  phases: [
    { title: 'GRO-Extend', detail: 'emit L8 significance sidecars over the 47 ARAs lacking them' },
    { title: 'Informed-Read', detail: 'blind informed-agent full-read breakthrough rating per paper + 2nd reader subset' },
    { title: 'Compute+Correlate', detail: 'metric vs informed rating; does significance predict breakthrough on recent work' },
  ],
}

const ROOT = '/Users/carlaostmann/code/dasmodel'
const LIB = `${ROOT}/research/ara-library`
const CORP = `${ROOT}/research/metrics/v5-breakthrough/corpus`
const SHAPE = `${ROOT}/research/metrics/v5-breakthrough/tournament/shapes/12_breakthrough.md`

const ALL = ["20225-2025-alzheimer-s-disease-facts-and","20226-2026-alzheimer-s-disease-facts-and","ada26-adult-human-ex-vivo-brain-slices","afi25-vision-and-convolutional-transformers-for-alzheimer","ahm26-machine-learning-and-deep-learning-for","ahm26b-trends-and-disparities-in-alzheimer-disease","aki26-molecular-signatures-of-resilience-to-alzheimer","aks25-an-explainable-web-based-diagnostic-system","aku25-population-attributable-fractions-associated-with-alzheimer","aku25b-effects-of-medicare-predictors-in-health","ala26-trends-in-alzheimer-s-disease-mortality","alb26-early-detection-of-alzheimer-s-disease","ali25-multimodal-self-supervised-learning-for-early","ali26-privacy-preserving-multimodal-fusion-for-alzheimer","als25-the-role-of-glial-cell-senescence","als26-early-onset-alzheimer-s-disease-mortality","ami25-prevalence-deaths-and-disability-adjusted-life","amo25-regional-differences-in-the-incidence-of","ant26-mapea-project-evolution-of-care-for","ard25-response-of-spatially-defined-microglia-states","ave25-uncovering-plaque-glia-niches-in-human","bec25-a-neuroimmune-cerebral-assembloid-model-to","bor25b-harmonized-prevalence-estimates-of-dementia-in","cav25-global-societal-burden-of-alzheimer-s","che25e-apoe4-reprograms-microglial-lipid-metabolism-in","che25h-global-burden-of-alzheimer-disease-and","che26-diagnostic-performance-of-plasma-p-tau217","cum26-alzheimer-s-disease-drug-development-pipeline","div25-the-microcirculation-the-blood-brain-barrier","gau25-single-nucleus-and-spatial-transcriptomic-profiling","gie25-geographical-inequalities-in-dementia-diagnosis-and","gon25b-stereo-seq-of-the-prefrontal-cortex","guo25c-the-disease-burden-risk-factors-and","han26-tau-pathological-activity-in-plasma-before","hao25-trend-analysis-and-future-predictions-of","huu25-apoe-e4-alzheimer-s-risk-converges","iac25-a-practical-overview-of-the-use","jes26-efficacy-and-safety-of-donanemab-in","ji25-alzheimer-s-disease-patient-brain-extracts","kes25-the-alzheimer-s-disease-diagnosis-and","kho25-explainable-artificial-intelligence-in-neuroimaging-of","liu25h-global-burden-of-alzheimer-s-disease","liu25i-single-cell-multiregion-epigenomic-rewiring-in","ols25-microglial-mechanisms-drive-amyloid-clearance-in","pal25-alzheimer-s-association-clinical-practice-guideline","qi25-alzheimer-s-disease-digital-biomarkers-multidimensional","raz25-advancements-in-deep-learning-for-early","sal25-trailblazer-alz-4-a-phase-3","sal26-plasma-emtbr-tau243-and-p-tau217","sim26-multi-modal-graph-neural-network-with","smi25-contribution-of-modifiable-midlife-and-late","sor25-barriers-for-access-and-utilization-of","the25-blood-phosphorylated-tau-for-the-diagnosis","tit26-automated-high-throughput-quantification-of-plasma","val25-blood-biomarkers-of-alzheimer-s-disease","wan25c-global-burden-of-alzheimer-s-disease","wee25-early-intervention-anti-a-immunotherapy-attenuates","woj25-immunoassay-detection-of-multiphosphorylated-tau-proteoforms","wu25-a-2025-update-on-treatment-strategies","xu25-epidemiological-and-sociodemographic-transitions-in-the","xu25d-global-incidence-trends-and-projections-of","yu25-global-mortality-prevalence-and-disability-adjusted","zha25-assessing-and-projecting-the-global-impacts","zha25h-a-review-of-multimodal-fusion-based","zho25-microglia-networks-within-the-tapestry-of","zhu25b-global-burden-of-alzheimer-s-disease","zim25-donanemab-in-early-symptomatic-alzheimer-s"]

const NEED = ["20225-2025-alzheimer-s-disease-facts-and","20226-2026-alzheimer-s-disease-facts-and","ada26-adult-human-ex-vivo-brain-slices","afi25-vision-and-convolutional-transformers-for-alzheimer","ahm26-machine-learning-and-deep-learning-for","ahm26b-trends-and-disparities-in-alzheimer-disease","aku25-population-attributable-fractions-associated-with-alzheimer","aku25b-effects-of-medicare-predictors-in-health","ala26-trends-in-alzheimer-s-disease-mortality","alb26-early-detection-of-alzheimer-s-disease","ali25-multimodal-self-supervised-learning-for-early","als25-the-role-of-glial-cell-senescence","als26-early-onset-alzheimer-s-disease-mortality","amo25-regional-differences-in-the-incidence-of","ant26-mapea-project-evolution-of-care-for","ave25-uncovering-plaque-glia-niches-in-human","bec25-a-neuroimmune-cerebral-assembloid-model-to","bor25b-harmonized-prevalence-estimates-of-dementia-in","cav25-global-societal-burden-of-alzheimer-s","che25e-apoe4-reprograms-microglial-lipid-metabolism-in","che25h-global-burden-of-alzheimer-disease-and","div25-the-microcirculation-the-blood-brain-barrier","gie25-geographical-inequalities-in-dementia-diagnosis-and","gon25b-stereo-seq-of-the-prefrontal-cortex","huu25-apoe-e4-alzheimer-s-risk-converges","iac25-a-practical-overview-of-the-use","ji25-alzheimer-s-disease-patient-brain-extracts","kes25-the-alzheimer-s-disease-diagnosis-and","liu25h-global-burden-of-alzheimer-s-disease","liu25i-single-cell-multiregion-epigenomic-rewiring-in","ols25-microglial-mechanisms-drive-amyloid-clearance-in","pal25-alzheimer-s-association-clinical-practice-guideline","qi25-alzheimer-s-disease-digital-biomarkers-multidimensional","sal25-trailblazer-alz-4-a-phase-3","sal26-plasma-emtbr-tau243-and-p-tau217","sim26-multi-modal-graph-neural-network-with","smi25-contribution-of-modifiable-midlife-and-late","sor25-barriers-for-access-and-utilization-of","the25-blood-phosphorylated-tau-for-the-diagnosis","tit26-automated-high-throughput-quantification-of-plasma","wee25-early-intervention-anti-a-immunotherapy-attenuates","woj25-immunoassay-detection-of-multiphosphorylated-tau-proteoforms","wu25-a-2025-update-on-treatment-strategies","xu25d-global-incidence-trends-and-projections-of","zha25-assessing-and-projecting-the-global-impacts","zha25h-a-review-of-multimodal-fusion-based","zho25-microglia-networks-within-the-tapestry-of"]

const EXTEND_SCHEMA = {
  type: 'object', required: ['slug', 'ok', 'n_contributions', 'n_deltas'],
  properties: { slug: { type: 'string' }, ok: { type: 'boolean' },
    n_contributions: { type: 'integer' }, n_deltas: { type: 'integer' }, note: { type: 'string' } },
}

const RATING_SCHEMA = {
  type: 'object',
  required: ['slug', 'breakthrough_score', 'tier', 'justification'],
  properties: {
    slug: { type: 'string' },
    breakthrough_score: { type: 'integer' },
    tier: { type: 'string', enum: ['landmark', 'notable', 'solid', 'incremental', 'derivative'] },
    dimensions: {
      type: 'object',
      properties: { novelty: { type: 'integer' }, significance: { type: 'integer' },
        rigor: { type: 'integer' }, field_shift_potential: { type: 'integer' } },
    },
    justification: { type: 'string' },
  },
}

const FINAL_SCHEMA = {
  type: 'object',
  required: ['code_file', 'results_file', 'spearman_significance_vs_informed', 'headline'],
  properties: {
    code_file: { type: 'string' }, results_file: { type: 'string' }, n_papers: { type: 'integer' },
    spearman_significance_vs_informed: { type: 'number' },
    spearman_uptake_vs_informed: { type: 'number' },
    interrater_agreement: { type: 'number' }, headline: { type: 'string' },
  },
}

const extendTrack = (async () => {
  phase('GRO-Extend')
  return (await parallel(NEED.map((slug) => () =>
    agent(
      `Add the GRO L8 significance tier to an already-compiled recent (2025-26) Alzheimer's ARA.

ARA dir: ${LIB}/${slug}  (has PAPER.md + logic/; may or may not have gro/).
Spec: ${SHAPE} (sections A + C).

STEPS:
1. Read PAPER.md (front matter: year, doi) + logic/claims.md + logic/related_work.md (+ existing gro/ if present).
2. If gro/ lacks base sidecars, first emit quantities.yaml (Q##), claims_typed.yaml (C##), refs.yaml (R###), entities.yaml, genre.yaml, grounded in the ARA.
3. Emit the L8 files into ${LIB}/${slug}/gro/: contributions.yaml (CT##, double-typed author_framed vs compiler_assessed from the closed taxonomy, realized_in must ref real C##), delta_ledger.yaml (D##, claimed_value=Q##, baseline_value=XQ##), external_quantities.yaml (XQ##), sota_anchor.yaml (precedence_date=pub year), temporal.yaml.
4. HONESTY / penalize-don't-skip: emit only what the paper supports. Derivative/incremental work correctly gets incremental_improvement/replication/synthesis contribution types and qualitative_only/claimed_unresolved/not_claimed delta_status. Do NOT inflate novelty. Ground every number in the source.

Return structured result with real counts. Keep YAML valid.`,
      { phase: 'GRO-Extend', label: `ext:${slug.slice(0, 6)}`, schema: EXTEND_SCHEMA, effort: 'medium' }
    )
  ))).filter(Boolean)
})()

const readTrack = (async () => {
  phase('Informed-Read')
  const primary = await parallel(ALL.map((slug) => () =>
    agent(
      `You are an INFORMED Alzheimer's-disease research reviewer. Read one paper IN FULL and rate how much of a SCIENTIFIC BREAKTHROUGH it is — did it, or is it poised to, change what the field does next?

Read ONLY the paper's own content: ${LIB}/${slug}/PAPER.md (title, abstract, claims_summary) and ${LIB}/${slug}/logic/claims.md, ${LIB}/${slug}/logic/experiments.md, ${LIB}/${slug}/logic/related_work.md if present. Do NOT read the gro/ directory — your judgment must be INDEPENDENT of any metric.

Judge as a domain expert would: is the core finding genuinely novel and important, or a derivative re-analysis (another global-burden/GBD estimate, an incremental ML detection pipeline, an annual statistics report)? Landmark = a lecanemab/donanemab/p-tau217-class advance. Derivative = adds little the field didn't already have.

Return: breakthrough_score 0-100, tier (landmark/notable/solid/incremental/derivative), per-dimension sub-scores (novelty, significance, rigor, field_shift_potential; 0-100 each), one-sentence justification. Be calibrated and discriminating — do NOT cluster in the middle; most papers in any corpus are incremental.`,
      { phase: 'Informed-Read', label: `read:${slug.slice(0, 6)}`, schema: RATING_SCHEMA, effort: 'high' }
    )
  ))
  const subset = ALL.filter((_, i) => i % 4 === 0)
  const second = await parallel(subset.map((slug) => () =>
    agent(
      `You are a SECOND INDEPENDENT informed Alzheimer's reviewer. Blind breakthrough rating. Read ONLY ${LIB}/${slug}/PAPER.md + ${LIB}/${slug}/logic/{claims,experiments,related_work}.md — NOT the gro/ dir. Return breakthrough_score 0-100, tier, per-dimension sub-scores, one-sentence justification. Be calibrated and discriminating.`,
      { phase: 'Informed-Read', label: `read2:${slug.slice(0, 6)}`, schema: RATING_SCHEMA, effort: 'high' }
    )
  ))
  return { primary: primary.filter(Boolean), second: second.filter(Boolean) }
})()

const [extended, reads] = await Promise.all([extendTrack, readTrack])
log(`GRO-extended ${extended.filter(r => r.ok).length}/${NEED.length}; informed reads ${reads.primary.length}/${ALL.length} (+${reads.second.length} 2nd-reader subset)`)

phase('Compute+Correlate')
const primaryJson = JSON.stringify(reads.primary)
const secondJson = JSON.stringify(reads.second)
const final = await agent(
  `Compute the breakthrough metric over the recent corpus and correlate it against the blind informed-agent ground truth. Recency-controlled: ALL papers are 2025-26, so if the metric still tracks the informed rating it is NOT just detecting age.

INPUTS:
- GRO L8 shapes on disk at ${LIB}/<slug>/gro/ for the 67 recent ARAs.
- Real citation graph: ${CORP}/refs_raw.json (id2key + per-paper referenced_works), ${CORP}/works.json (per corpus paper: doi, year, oa_cited_by). Map each ARA to the graph by the DOI in its PAPER.md front matter.
- Reuse/adapt scorers: ${CORP}/compute_significance.py (significance from L8), ${CORP}/compute_breakthrough_v1.py (uptake + CD-index from the graph).
- Informed PRIMARY ratings (ground truth) JSON array of {slug, breakthrough_score, tier, dimensions, justification}:
${primaryJson}
- Informed SECOND-reader subset JSON array:
${secondJson}

STEPS:
1. Write ${CORP}/compute_recent.py: for each of the 67 ARAs compute SIGNIFICANCE from L8, UPTAKE/year + CD-index from the graph (join by DOI; papers absent from the graph get uptake 0, flagged), and the COMPOSITE. Attach the primary informed breakthrough_score.
2. Compute Spearman correlation: significance vs informed, uptake/year vs informed, composite vs informed (across papers with both). Compute inter-rater agreement (Spearman + mean abs diff) between primary and second-reader on the subset.
3. Write ${CORP}/recent_results.json (per-paper: all signals + informed score + tier) and ${CORP}/recent_results.md: correlation table, inter-rater agreement, ranked top/bottom-10 by informed score with metric scores, and an HONEST verdict — does significance predict informed breakthrough judgment on recent work (confound removed)? any mis-rankings? Note uptake is expected weak here (recent = little citation time) — that is the point.
4. Report ONLY what the code prints. Do not fabricate.

Return the structured result.`,
  { phase: 'Compute+Correlate', label: 'compute+correlate', schema: FINAL_SCHEMA, effort: 'high' }
)

return {
  gro_extended: extended.filter(r => r.ok).length,
  informed_reads: reads.primary.length,
  second_reader_subset: reads.second.length,
  result: final,
}
