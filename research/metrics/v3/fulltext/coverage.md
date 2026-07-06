# Full-text coverage report (P4)

Produced in response to critique P4 (`research/metrics/v3/critiques/cycle1.md`): the metrics
judges currently check claims against `research/data/lib/<slug>/metadata.md`, which is
abstract + metadata, not the source paper. This report is the acquisition pass: pull real full
text where it exists, and be honest about where it doesn't. No text was fabricated or padded —
rows marked `abstract_only` have no file in this directory.

## Method

For each of the 12 ARAs, in priority order:

1. **local_pdf** — if `research/data/lib/<slug>/paper.pdf` already existed (per `sources.yaml`
   `pdf.downloaded: true`), extracted with `pdftotext -layout` (Poppler) into
   `research/metrics/v3/fulltext/<slug>.txt`.
2. **pubmed** — else, resolved PMCID (`convert_article_ids` / PMCID already recorded in
   `sources.yaml`) and pulled full text via the live PubMed MCP `get_full_text_article` tool.
3. **biorxiv** — checked for a bioRxiv preprint route; the `bioRxiv` MCP `get_preprint` tool
   returns metadata + abstract + a PDF URL, **not extracted full text**, so it was not usable as
   a fulltext source on its own in this pass (huu25 has a bioRxiv DOI but was resolved via its
   PMC copy instead, since that PMC record carries a machine-readable full text body).
4. **abstract_only** — else, confirmed (via `convert_article_ids`, no PMCID found) that no PMC
   full text exists and the article is paywalled with no accessible OA route; left as-is. No
   file was written for these slugs.

`has_methods_section` / `has_discussion` were checked by grepping each cached file for Methods /
Discussion section markers (numbered headers like `2 METHODS`, `4 DISCUSSION`, or bare
`Methods` / `Discussion` headings — layouts vary because `pdftotext -layout` preserves the
paper's two-column typesetting, so headers appear inline with running header/footer text). For
the two abstract-only rows, the "Methods" seen is a 2–4 sentence structured-abstract stub
(`METHODS\n<one paragraph>`), not a real Methods section, and there is no Discussion at all in a
structured abstract (Background/Objective/Methods/Results/Conclusions) — so both booleans are
`false` there, which is the whole point of the critique: falsifiability/scope/nulls/limitations
live in sections the abstract omits.

## Coverage table

| slug | source | char_count | has_methods_section | has_discussion |
|---|---|---:|:---:|:---:|
| ahm26b | abstract_only | 3122 (metadata.md) | false | false |
| che26 | local_pdf | 57569 | true | true |
| cum26 | local_pdf | 165202 | true | true |
| huu25 | pubmed | 81477 | true | true |
| jes26 | local_pdf | 80022 | true | true |
| kes25 | local_pdf | 146472 | true | true |
| pal25 | local_pdf | 123147 | true | true |
| sal25 | local_pdf | 75624 | true | true |
| sal26 | pubmed | 38681 | true | true |
| the25 | abstract_only | 6440 (metadata.md) | false | false |
| tit26 | local_pdf | 91342 | true | true |
| woj25 | local_pdf | 128544 | true | true |

## Totals

- **Full text acquired: 10 / 12** (83%)
  - `local_pdf`: 8 (che26, cum26, jes26, kes25, pal25, sal25, tit26, woj25) — PDF was already
    cached in `research/data/lib/<slug>/paper.pdf`; extracted, not newly fetched.
  - `pubmed` (live MCP, newly fetched this pass): 2 (huu25 via PMC12667772, sal26 via
    PMC13213595).
- **Abstract-only: 2 / 12** (ahm26b, the25) — both confirmed paywalled with no PMC record
  (`convert_article_ids` returns no PMCID for PMID 41773884 / 40818474) and no other OA PDF
  route (Unpaywall `oa_status: closed` for ahm26b; the25's only OA location is a
  submitted-version landing page at pure.au.dk with no directly downloadable PDF — already
  documented in each slug's `sources.yaml`).
- All 10 full-text files have both a genuine Methods and a genuine Discussion section
  (10/10 true/true); the 2 abstract-only rows have neither (0/2 true/true) by construction of a
  structured abstract.

## Honest assessment (for the caller)

**Acquisition worked better than expected: 10/12 (83%), not the "no source PDF for most ARAs"
state the critique describes.** 8 of those 10 were *already* sitting on disk as `paper.pdf` from
an earlier ingestion pass and simply hadn't been extracted to text — that's the biggest single
finding here: most of the "abstract-only" framing in the critique was stale. Only 2 required a
live external call this session, and both worked on the first try via PubMed's PMC full-text
endpoint (bioRxiv's MCP tool does not itself return extracted full text, only metadata + PDF
URL, so it wasn't the load-bearing tool here despite being named in P4).

**Is re-grounding the judges against full text now possible for enough ARAs to matter? Yes,
for a corpus this size.** 10/12 is a strong majority, and the 2 gaps (ahm26b, the25) are
genuinely unreachable by legitimate means right now (closed OA, no PMC, no author-manuscript
copy) — not a fetch-effort problem, a rights problem. A re-grounding pass should:
- Run all 10 [sem] judges against the cached full text instead of `metadata.md` for those slugs.
- For ahm26b and the25, either exclude them from paper-quality ranking (per P4's own
  recommendation: "abstract-only ARAs barred from paper-quality ranking") or explicitly label
  their scores `unverifiable`/`abstract-bound` rather than `validated`/`source_bound`.
- Re-run the specific over-claims the critique flagged as compiler-transcription errors
  (the25 "all…at moderate certainty", jes26 "amyloid clearance was maintained" vs. the paper's
  "reaccumulates", huu25 "MAPT downregulated") against the newly cached full text — the25 and
  jes26 now both have real full text on disk, so this check is directly actionable, not
  theoretical.
- Note the25 in particular: it was one of the critique's three "validated" judge subjects and is
  one of the two still abstract-only here. Its judge score should not be trusted as
  paper-grounded until/unless a manuscript copy is found (e.g. an author's institutional
  repository beyond the dead pure.au.dk landing page) — flag it explicitly rather than silently
  re-scoring it off metadata.md again.

Net: this pass does not fix P1–P3 (the `validated` mislabeling, the fidelity-vs-paper-rank
conflation, the C16 axiom) — those are scoring-logic problems, not text-availability problems —
but it removes the specific "there is no source PDF" excuse for 10 of 12 ARAs and gives the next
cycle real text to check compiler fidelity against.
