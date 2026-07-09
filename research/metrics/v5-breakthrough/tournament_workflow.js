export const meta = {
  name: 'breakthrough-metric-redesign-tournament',
  description: '4-2-1 design tournament: redesign the breakthrough metric to align with the blind expert panel, emitting a concrete formula over available GRO features',
  phases: [
    { title: 'Design tournament', detail: '4 clean-room proposers -> Fable judge -> 2 refine -> 1 winner + formula' },
  ],
}

const V5 = '/Users/carlaostmann/code/dasmodel/research/metrics/v5-breakthrough'
const CORPUS = V5 + '/corpus'
const ARALIB = '/Users/carlaostmann/code/dasmodel/research/ara-library'

// Per-paper fields available in corpus_scored.json that a formula may use:
const FIELDS = [
  'contribution', 'contrib_peak', 'contrib_wmean', 'n_contribs', 'n_puffery',
  'delta', 'delta_max', 'frac_quant_verified', 'n_deltas',
  'anchor', 'anchor_mean_overlap', 'anchor_max_overlap', 'anchor_n',
  'uptake_per_year', 'cd_index', 'year',
].join(', ')

const PROPOSAL_SCHEMA = {
  type: 'object',
  required: ['name', 'rationale', 'formula', 'fields_used', 'goodhart_defense', 'recency_handling'],
  properties: {
    name: { type: 'string' },
    rationale: { type: 'string', description: 'why this design tracks expert breakthrough judgement' },
    formula: { type: 'string', description: 'a single Python expression over a dict r with the named fields (e.g. "0.5*r[\'contrib_peak\'] + 0.3*(1-r[\'anchor_mean_overlap\'] or 0) - 0.2*r[\'n_puffery\']"). Must be pure arithmetic; guard None with (x or 0).' },
    fields_used: { type: 'array', items: { type: 'string' } },
    goodhart_defense: { type: 'string', description: 'why an annual facts-and-figures report / burden re-estimate scores LOW under this formula' },
    recency_handling: { type: 'string' },
  },
}
const STAGE1_SCHEMA = {
  type: 'object', required: ['winners', 'reasoning'],
  properties: {
    winners: { type: 'array', minItems: 2, maxItems: 2, items: { type: 'string' } },
    reasoning: { type: 'string' },
  },
}
const FINAL_SCHEMA = {
  type: 'object',
  required: ['winner', 'formula', 'weights_explained', 'computability_verdict', 'qualification'],
  properties: {
    winner: { type: 'string' },
    formula: { type: 'string', description: 'the final adopted Python expression over dict r (pure arithmetic, None-guarded)' },
    weights_explained: { type: 'string' },
    computability_verdict: { type: 'string', description: 'which terms are deterministic-once-resolved vs irreducibly judged' },
    qualification: { type: 'string', description: 'the honest ceiling: overfitting risk (validated in-sample on n=55), sparse-graph limits' },
  },
}

const GROUNDING = `Ground your design by reading:
- Available per-paper features (your formula palette) + current scores: ${CORPUS}/corpus_scored.json  (fields: ${FIELDS})
- THE FAILURE YOU MUST FIX: ${CORPUS}/metric_vs_expert.json — the current significance metric vs the blind 3-judge expert panel over 55 recent papers. Spearman is ~ -0.10 (near zero / slightly negative). The metric ranks annual "facts and figures" reports, burden re-estimates, and the drug-pipeline review NEAR THE TOP; the expert panel floors them (~4-9/100) and puts real molecular/clinical discoveries (ols25, liu25i, aki26, han26) on top.
- The data shape: ${V5}/tournament/shapes/12_breakthrough.md and brief ${V5}/tournament/PROPOSER_BRIEF.md
- An example resolved anchor (sparse=novel): ${ARALIB}/aki26-molecular-signatures-of-resilience-to-alzheimer/gro/sota_anchor.yaml`

function proposerPrompt(i) {
  return `You are clean-room breakthrough-metric designer #${i}. Redesign the breakthrough-ness metric so it ALIGNS with expert judgement, expressed as a concrete formula over the available GRO features.

${GROUNDING}

Your job: propose a formula (a single Python arithmetic expression over a dict r whose keys are: ${FIELDS}) that would rank the 55 papers close to the expert panel — i.e. push comprehensive reports/reviews DOWN and genuine discoveries UP. Diagnose WHY the current significance (0.4*contribution + 0.4*delta + 0.2*anchor) fails: reports rack up many typed contributions and quantified deltas (high contribution+delta) despite zero novelty. Candidate fixes to consider: use contrib_peak (best single contribution) not breadth; penalize breadth/padding (n_contribs, n_puffery); use LOW anchor_mean_overlap as the novelty signal (sparse prior art = novel; dense = incremental); down-weight delta breadth. Guard None with (x or 0). Keep it interpretable — a few terms, not a kitchen sink. Return your proposal.`
}
function stage1Prompt(props) {
  return `You are the Fable judge. Four proposers submitted breakthrough-metric formulas (JSON). Pick the TWO most likely to (a) rank genuine discoveries above comprehensive reports, (b) generalize rather than overfit n=55, (c) stay interpretable and computable from the named fields.\n\n${JSON.stringify(props, null, 2)}\n\nName two winners (exact names) and explain.`
}
function refinePrompt(name, props) {
  return `You designed "${name}", advancing to round 2. Here are all four round-1 proposals — graft the best ideas in:\n${JSON.stringify(props, null, 2)}\n\nRevise "${name}" into its strongest, still-interpretable form. Keep the formula a pure None-guarded arithmetic expression over: ${FIELDS}. Return the improved proposal.`
}
function finalPrompt(improved) {
  return `You are the Fable judge naming the WINNER. Two refined breakthrough-metric formulas (JSON):\n${JSON.stringify(improved, null, 2)}\n\nPick one. Return the final adopted formula (pure None-guarded Python arithmetic over dict r with fields: ${FIELDS}), explain the weights, give a computability verdict (which terms are deterministic-once-anchors-resolved vs irreducibly judged), and state the honest ceiling (it is validated IN-SAMPLE on 55 papers with partial anchor resolution — overfitting risk, no held-out set).`
}

phase('Design tournament')
log('Redesign tournament: 4 clean-room proposers targeting the expert panel')
const proposals = (await parallel([1, 2, 3, 4].map(i => () =>
  agent(proposerPrompt(i), { label: `propose#${i}`, phase: 'Design tournament', schema: PROPOSAL_SCHEMA })
))).filter(Boolean)

let out = { proposals, stage1: null, improved: [], final: null }
if (proposals.length >= 2) {
  const stage1 = await agent(stage1Prompt(proposals), { label: 'judge:stage1', phase: 'Design tournament', schema: STAGE1_SCHEMA })
  out.stage1 = stage1
  const winners = (stage1?.winners || []).filter(n => proposals.some(p => p.name === n)).slice(0, 2)
  const improved = (await parallel(winners.map(w => () =>
    agent(refinePrompt(w, proposals), { label: `refine:${w.slice(0, 14)}`, phase: 'Design tournament', schema: PROPOSAL_SCHEMA })
  ))).filter(Boolean)
  out.improved = improved
  if (improved.length >= 1) {
    out.final = await agent(finalPrompt(improved), { label: 'judge:final', phase: 'Design tournament', schema: FINAL_SCHEMA })
  }
}
return out
