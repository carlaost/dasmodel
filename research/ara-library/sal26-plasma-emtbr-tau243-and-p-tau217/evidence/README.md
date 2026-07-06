# Evidence Index

> **Grounding: abstract-only — no evidence objects extracted.**
>
> The full text of this article was unavailable at compile time. It is green open access
> (CC BY-NC-ND; PMID 42189519, PMCID PMC13213595) and readable as HTML on PMC/Europe PMC, but **no
> licit rendered/OA PDF exists** (Unpaywall `url_for_pdf` is null; the PMC and Europe PMC PDF
> endpoints return no file). Because no full text or figure/table source was accessible, **no
> numbered tables or figures could be rendered, transcribed, or screenshotted.**
>
> Consequently, per compiler rules (no fabrication), this ARA files **zero** evidence tables and
> **zero** evidence figures. The `evidence/tables/` and `evidence/figures/` directories are
> intentionally empty. Evidence-completeness for Seal Level 1 is **N/A (abstract-only)**: the source
> the completeness sweep would run over (main text + appendices with numbered objects) was not
> available.

## Tables
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| — (none) | No full text available (abstract-only) | — | No numbered tables could be extracted; none exist in the abstract. |

## Figures
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| — (none) | No full text available (abstract-only) | — | No numbered figures could be extracted; none exist in the abstract. |

## Where the numbers live instead
The only quantitative values available from the provided input are the cohort sizes (872 BioFINDER-2;
156 Knight ADRC), which are grounded in `logic/claims.md` (C01) with verbatim quotes from the
abstract (`metadata.md`). All effect sizes (concordance statistics, model-comparison margins,
association measures) are reported by the abstract only qualitatively ("strong concordance",
"outperformed", "aligned with greater ...") and are marked "Not available from provided input (no
full text)" throughout the cognitive layer.

## To complete the evidence layer later
If a licit full text / OA PDF or the JAMA figures/tables become available, extract each numbered
`Table N` and `Figure N` in order (markdown transcription + `.png` screenshot per compiler §11) and
re-run the coverage + Seal passes.
