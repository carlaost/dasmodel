export const meta = {
  name: 'breakthrough-corpus-eval',
  description: 'Blind expert panel over all recent AD papers + the never-run 4-2-1 metric design tournament',
  phases: [
    { title: 'Expert panel', detail: '3 blind domain-expert judges rate breakthrough-ness per paper' },
    { title: 'Design tournament', detail: '4 clean-room proposers -> Fable judge -> 2 refine -> 1 winner' },
  ],
}

const ARALIB = '/Users/carlaostmann/code/dasmodel/research/ara-library'
const CORPUS = '/Users/carlaostmann/code/dasmodel/research/metrics/v5-breakthrough/corpus'
const SHAPES = '/Users/carlaostmann/code/dasmodel/research/metrics/v5-breakthrough/tournament'
const SLUGS = typeof args === 'string' ? JSON.parse(args) : args

// ---- schemas -------------------------------------------------------------
const JUDGE_SCHEMA = {
  type: 'object',
  required: ['breakthrough_score', 'tier', 'confidence', 'content_available', 'rationale'],
  properties: {
    breakthrough_score: { type: 'integer', minimum: 0, maximum: 100,
      description: 'How field-reshaping is this work? 0=no contribution, 100=landmark that redefines the field' },
    tier: { type: 'string', enum: ['landmark', 'significant', 'solid', 'incremental', 'non_contribution'] },
    confidence: { type: 'number', minimum: 0, maximum: 1 },
    content_available: { type: 'boolean', description: 'false if only a title was available to judge' },
    rationale: { type: 'string', description: 'one to two sentences, <=320 chars' },
  },
}
const PROPOSAL_SCHEMA = {
  type: 'object',
  required: ['name', 'one_liner', 'signals', 'goodhart_defense', 'recency_handling', 'weaknesses'],
  properties: {
    name: { type: 'string' },
    one_liner: { type: 'string' },
    signals: { type: 'array', items: { type: 'object', required: ['name', 'measures', 'computable_from', 'formula_sketch'],
      properties: { name: { type: 'string' }, measures: { type: 'string' },
        computable_from: { type: 'string', description: 'which GRO L8 sidecar / graph field' },
        formula_sketch: { type: 'string' } } } },
    goodhart_defense: { type: 'string', description: 'how it stops a heavily-cited annual review (facts-and-figures) scoring as a breakthrough' },
    recency_handling: { type: 'string', description: 'how it degrades gracefully on brand-new papers with empty downstream graphs' },
    weaknesses: { type: 'string' },
  },
}
const STAGE1_SCHEMA = {
  type: 'object', required: ['winners', 'reasoning'],
  properties: {
    winners: { type: 'array', minItems: 2, maxItems: 2, items: { type: 'string', description: 'proposal name' } },
    reasoning: { type: 'string' },
    scores: { type: 'array', items: { type: 'object', required: ['name', 'score'],
      properties: { name: { type: 'string' }, score: { type: 'number' }, note: { type: 'string' } } } },
  },
}
const FINAL_SCHEMA = {
  type: 'object', required: ['winner', 'qualification', 'final_metric_spec'],
  properties: {
    winner: { type: 'string' },
    qualification: { type: 'string', description: 'the honest ceiling / where it still fails' },
    final_metric_spec: { type: 'string', description: 'the adopted breakthrough metric: signals, weights, computability verdict' },
  },
}

// ---- prompts -------------------------------------------------------------
const PERSONAS = [
  { key: 'trialist', desc: 'a senior clinical Alzheimer\'s-disease researcher and trialist (you have run phase-3 anti-amyloid trials and read the biomarker literature). You judge whether a paper changes clinical practice, diagnosis, or therapeutic direction.' },
  { key: 'neuroscientist', desc: 'a molecular / systems neuroscientist studying AD mechanisms (single-cell, spatial transcriptomics, microglia, tau/amyloid biology). You judge mechanistic novelty and whether it opens genuinely new biology.' },
  { key: 'metascientist', desc: 'a metascience / research-impact analyst. You are hard-nosed about distinguishing a genuine discovery from a well-cited non-discovery (an annual statistics report, a burden-of-disease update, a review, an incremental ML benchmark). Field-reshaping potential is what you score.' },
]

function judgePrompt(slug, persona) {
  return `You are ${persona}

Rate how much of a scientific BREAKTHROUGH the following Alzheimer's-disease paper is — its potential to reshape the field — on a 0-100 scale.

Read ONLY this file for the paper's content: ${ARALIB}/${slug}/PAPER.md
Use only its YAML frontmatter (title, year, venue, abstract, claims_summary). It is fine to also read logic/claims.md in the same paper directory for detail. Do NOT open the gro/ sidecars, any *.json in the metrics folder, or any file with "significance"/"score" in it — you must stay blind to any computed metric. If PAPER.md has no abstract/claims (title only), judge from the title and set content_available=false with low confidence.

Anchor your scale:
- 90-100 landmark: redefines diagnosis/therapy/mechanism (e.g. a first pivotal disease-modifying trial, a first-in-field molecular discovery).
- 65-89 significant: a real new finding/method that others will build on.
- 40-64 solid: a competent contribution, limited reach.
- 15-39 incremental: derivative, a benchmark tweak, a routine update.
- 0-14 non-contribution: an annual statistics/facts report, a burden-of-disease re-estimate, a generic review — cited but not a discovery.

Be skeptical: a heavily-cited annual "facts and figures" report or a global-burden re-estimate is NOT a breakthrough. Return your rating.`
}

function proposerPrompt(i) {
  return `You are clean-room metric designer #${i}. Design a BREAKTHROUGH-NESS metric for scientific papers, computed from the GRO substrate.

Read these to ground your design (and nothing about other proposers' work):
- The data shape you can compute over: ${SHAPES}/shapes/12_breakthrough.md
- The proposer brief + constraints: ${SHAPES}/PROPOSER_BRIEF.md and ${SHAPES}/CRITIQUE_BRIEF.md (if present)
- What the current signals actually produced on the real 66-paper recent corpus: ${CORPUS}/corpus_scored.md  (READ THIS — it shows the failure you must fix)
- Example L8 sidecars a paper carries: pick any dir under ${ARALIB}/*/gro/ (contributions.yaml, delta_ledger.yaml, sota_anchor.yaml, external_quantities.yaml, temporal.yaml) and the graph fields (uptake_per_year, cd_index).

THE PROBLEM TO SOLVE (from corpus_scored.md): the current significance signal ranks the annual "2025 Alzheimer's facts and figures" REPORT as the #1 most-significant paper, above real donanemab trials and molecular discoveries. That is a Goodhart failure. Design a metric (a SET of signals, never one number) that:
  1. Separates a genuine discovery from a heavily-cited non-discovery (annual report / burden re-estimate / review).
  2. Is computable from the GRO L8 shape + citation graph — say exactly which fields feed each signal.
  3. Degrades gracefully on brand-new papers (empty downstream graph) — a young paper is PENALIZED-not-skipped, and you must distinguish "not-yet-a-breakthrough" from "failed-to-become-one".
Return your proposal.`
}

function stage1Prompt(proposals) {
  return `You are the Fable judge for a breakthrough-metric design tournament. Four clean-room proposers submitted metric designs (JSON below). Pick the TWO strongest to advance.

Judge on: (a) does it actually kill the "annual facts-and-figures report ranks #1" Goodhart hole; (b) is every signal genuinely computable from the named GRO L8 / graph fields (no hand-waving); (c) forward-looking honesty — does it separate not-yet from failed, and degrade gracefully on new papers; (d) is it a SET spanning distinct signals, not one repackaged number.

PROPOSALS:
${JSON.stringify(proposals, null, 2)}

Name the two winners (by their exact "name") and explain.`
}

function refinePrompt(winnerName, proposals) {
  return `You are the designer of the "${winnerName}" breakthrough metric, advancing to round 2. Here are ALL four round-1 proposals so you can graft the best ideas from the others into yours:
${JSON.stringify(proposals, null, 2)}

Revise "${winnerName}" into its strongest form. Keep it computable from the GRO L8 shape + citation graph, keep it a SET of signals, and make the Goodhart defense (annual report must not rank as a breakthrough) and the new-paper recency handling airtight. Return the improved proposal.`
}

function finalPrompt(improved) {
  return `You are the Fable judge naming the WINNER of the breakthrough-metric design tournament. Two refined designs (JSON below). Pick one, state the honest ceiling (where it still fails), and write the final adopted metric spec: the signals, their weights, which GRO field computes each, and a one-line computability verdict (which signals are deterministic once the graph exists vs irreducibly judged).

REFINED DESIGNS:
${JSON.stringify(improved, null, 2)}`
}

// ---- run -----------------------------------------------------------------
phase('Expert panel')
log(`Expert panel: ${SLUGS.length} recent papers x ${PERSONAS.length} blind judges`)
const expert = await parallel(SLUGS.map(slug => () =>
  parallel(PERSONAS.map(p => () =>
    agent(judgePrompt(slug, p.desc), { label: `judge:${p.key}:${slug.slice(0, 10)}`, phase: 'Expert panel', schema: JUDGE_SCHEMA, effort: 'low' })
      .then(v => (v ? { persona: p.key, ...v } : null))
  )).then(votes => ({ slug, votes: votes.filter(Boolean) }))
))

phase('Design tournament')
log('Design tournament: 4 clean-room proposers')
const proposals = (await parallel([1, 2, 3, 4].map(i => () =>
  agent(proposerPrompt(i), { label: `propose#${i}`, phase: 'Design tournament', schema: PROPOSAL_SCHEMA })
))).filter(Boolean)

let tournament = { proposals, stage1: null, improved: [], final: null }
if (proposals.length >= 2) {
  const stage1 = await agent(stage1Prompt(proposals), { label: 'judge:stage1', phase: 'Design tournament', schema: STAGE1_SCHEMA })
  tournament.stage1 = stage1
  const winnerNames = (stage1?.winners || []).filter(n => proposals.some(p => p.name === n)).slice(0, 2)
  const improved = (await parallel(winnerNames.map(w => () =>
    agent(refinePrompt(w, proposals), { label: `refine:${w.slice(0, 14)}`, phase: 'Design tournament', schema: PROPOSAL_SCHEMA })
  ))).filter(Boolean)
  tournament.improved = improved
  if (improved.length >= 1) {
    tournament.final = await agent(finalPrompt(improved), { label: 'judge:final', phase: 'Design tournament', schema: FINAL_SCHEMA })
  }
}

return { expert, tournament, n_papers: SLUGS.length }
