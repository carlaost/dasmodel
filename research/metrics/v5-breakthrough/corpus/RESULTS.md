# Breakthrough metric — corpus + graph-signal results

## Corpus (corrected)
- Source: `all-papers.csv` — **539 Alzheimer papers, 526 with DOI, all 2025–2026** (a recent snapshot).
- Citation graph built via OpenAlex (`build_citation_graph.py`): **521/526 resolved, 309 intra-corpus
  citation edges**, largest connected component **216 papers** (real lineage — they cite each other).
- Lineage backbone = the shared landmark ancestors the corpus cites (`ancestors.json`): Lecanemab (cited
  by 72 corpus papers), Donanemab (61), NIA-AA framework (46), DAM microglia (33), p-tau217 (24), Braak
  staging, single-cell AD atlas, etc.

## Labelled set
- **POSITIVES** = 5 landmark-ancestor breakthroughs (all confirmed open-access → GRO-compilable):
  lecanemab (2022), donanemab (2023), p-tau217 (2020), DAM microglia (2017), NIA-AA framework (2018).
- **NEGATIVES** = derivative-cluster corpus papers (already compiled ARAs): the GBD "global burden of AD"
  cluster (wan25c, zhu25b, yu25, ami25, xu25d, liu25h, guo25c, hao25), the DL-detection cluster (raz25,
  kho25, zha25h, ali26, aks25, afi25), and the annual "facts and figures" reports (20225/20226).

## Graph signals (v1, `compute_breakthrough_v1.py`) — 2 of 3 tier-separated signals
Computed over the real citation graph. Means:

| Signal | POSITIVE | NEGATIVE | Discriminates |
|---|---|---|---|
| Uptake (in-corpus citations) | 47.2 | 3.25 | ✅ strong |
| Uptake / year (age-normalized) | 10.35 | 3.25 | ✅ yes |
| CD-index (disruption) | −0.446 | −0.333 | ❌ no |

### Findings
1. **Uptake discriminates known breakthroughs from derivative work (~15×), and survives age-normalization.**
2. **CD-index / disruption does NOT track breakthrough here** — the landmarks are *consolidating* (donanemab
   CD −0.84: its citers also cite the trials it builds on), consistent with the metascience result that many
   landmark works consolidate rather than disrupt. Naive "disruption = breakthrough" fails on this data.
3. **Goodhart hole:** the one negative with high uptake (16) is the annual *facts-and-figures* review — a
   heavily-cited non-discovery. Raw uptake alone would misclassify it → motivates the **third signal
   (significance, from GRO L8 contributions/deltas)** to separate a cited review from a cited breakthrough.

### Caveat
Positives are 2017–23, negatives 2025–26 → raw uptake is age-confounded; CD-index and uptake/year are the
fairer contrasts, and the significance signal (age-independent) is needed to close the review-vs-discovery gap.

## Next: significance signal
GRO-compile the extended shape (incl. L8 `contributions`/`delta_ledger`/`sota_anchor`) over the labelled set,
compute the significance signal, integrate the 3-signal composite, and re-test positives vs negatives.
