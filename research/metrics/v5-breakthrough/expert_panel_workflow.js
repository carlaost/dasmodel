export const meta = {
  name: 'breakthrough-expert-panel',
  description: 'Blind 3-judge domain-expert panel rating breakthrough-ness of every recent AD paper (the ground truth to validate the metric against)',
  phases: [
    { title: 'Expert panel', detail: '3 blind domain-expert judges per paper' },
  ],
}

const ARALIB = '/Users/carlaostmann/code/dasmodel/research/ara-library'
const SLUGS = typeof args === 'string' ? JSON.parse(args) : args

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

const PERSONAS = [
  { key: 'trialist', desc: "a senior clinical Alzheimer's-disease researcher and trialist (you have run phase-3 anti-amyloid trials and read the biomarker literature). You judge whether a paper changes clinical practice, diagnosis, or therapeutic direction." },
  { key: 'neuroscientist', desc: 'a molecular / systems neuroscientist studying AD mechanisms (single-cell, spatial transcriptomics, microglia, tau/amyloid biology). You judge mechanistic novelty and whether it opens genuinely new biology.' },
  { key: 'metascientist', desc: 'a metascience / research-impact analyst. You are hard-nosed about distinguishing a genuine discovery from a well-cited non-discovery (an annual statistics report, a burden-of-disease update, a review, an incremental ML benchmark). Field-reshaping potential is what you score.' },
]

function judgePrompt(slug, persona) {
  return `You are ${persona}

Rate how much of a scientific BREAKTHROUGH the following Alzheimer's-disease paper is — its potential to reshape the field — on a 0-100 scale.

Read ONLY this file for the paper's content: ${ARALIB}/${slug}/PAPER.md
Use only its YAML frontmatter (title, year, venue, abstract, claims_summary). You may also read logic/claims.md in the same paper directory for detail. Do NOT open the gro/ sidecars, any *.json in the metrics folder, or any file with "significance"/"score"/"anchor" in it — you must stay blind to any computed metric. If PAPER.md has no abstract/claims (title only), judge from the title and set content_available=false with low confidence.

Anchor your scale:
- 90-100 landmark: redefines diagnosis/therapy/mechanism (a first pivotal disease-modifying trial, a first-in-field molecular discovery).
- 65-89 significant: a real new finding/method others will build on.
- 40-64 solid: a competent contribution, limited reach.
- 15-39 incremental: derivative, a benchmark tweak, a routine update.
- 0-14 non-contribution: an annual statistics/facts report, a burden-of-disease re-estimate, a generic review — cited but not a discovery.

Be skeptical: a heavily-cited annual "facts and figures" report or a global-burden re-estimate is NOT a breakthrough. Return your rating.`
}

phase('Expert panel')
log(`Expert panel: ${SLUGS.length} recent papers x ${PERSONAS.length} blind judges`)
const expert = await parallel(SLUGS.map(slug => () =>
  parallel(PERSONAS.map(p => () =>
    agent(judgePrompt(slug, p.desc), { label: `judge:${p.key}:${slug.slice(0, 10)}`, phase: 'Expert panel', schema: JUDGE_SCHEMA, effort: 'low' })
      .then(v => (v ? { persona: p.key, ...v } : null))
  )).then(votes => ({ slug, votes: votes.filter(Boolean) }))
))

return { expert, n_papers: SLUGS.length }
