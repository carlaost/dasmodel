export const meta = {
  name: 'historical-fulltext-typing-claude',
  description: 'Claude types contributions from FULL TEXT for the historical corpus (dual-model half A)',
  phases: [{ title: 'Type-FT', detail: 'one Claude agent per paper reads full text and types contributions' }],
}
const items = typeof args === 'string' ? JSON.parse(args) : args
const SCHEMA = { type:'object', additionalProperties:false, required:['contributions'],
  properties:{ contributions:{ type:'array', items:{ type:'object', additionalProperties:false,
    required:['type','confidence'],
    properties:{ type:{type:'string', enum:['new_paradigm','new_method','new_finding','refutation','synthesis','incremental_improvement','replication']},
                 confidence:{type:'number', minimum:0, maximum:1} } } } } }
const NOVW={new_paradigm:1.0,new_method:0.8,new_finding:0.7,refutation:0.6,synthesis:0.35,incremental_improvement:0.15,replication:0.1}
phase('Type-FT')
const res = await parallel(items.map(it => () =>
  agent(`Read the full text at ${it.path} (a research paper). List each DISTINCT scientific contribution it makes and classify each with a novelty TYPE from this closed taxonomy plus a confidence in [0,1]:
new_paradigm > new_method > new_finding > refutation > synthesis > incremental_improvement > replication.
Judge ONLY from the paper's own text, at its publication time — NO hindsight about later impact; do not reward quantity. Output only the JSON object.`,
    {label:`ftype:${it.slug}`, phase:'Type-FT', schema:SCHEMA, agentType:'general-purpose', effort:'low'})
    .then(o => { const cs=(o&&o.contributions)||[]
      if(!cs.length) return {slug:it.slug, metric:null, n:0}
      const wc=cs.map(c=>(NOVW[c.type]||0.1)*(c.confidence||0.3))
      const peak=Math.max(...wc)
      const cw=cs.reduce((s,c)=>s+(NOVW[c.type]||0.1)*(c.confidence||0.3),0)/(cs.reduce((s,c)=>s+(c.confidence||0.3),0)||1)
      return {slug:it.slug, metric:Math.max(peak,cw), peak, cwmean:cw, n:cs.length} })
))
const out={}; for(const r of res){ if(r) out[r.slug]=r }
return out
