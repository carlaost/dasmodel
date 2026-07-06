# Evidence Index

Raw evidence for the *desciencemodel* project ARA. Objects are namespaced by source:
`ara_*` = ARA paper (Liu et al., 2026); `mo_*` = multi-omics paper (Otte et al., 2025). Each file has
a co-located rendered `.png` screenshot of the source region. The oshima implementation has no
numbered tables/figures — its evidence is the captured source under `src/execution/` (see
`src/artifacts.md`).

> **Claim-ID authority.** This index and `logic/claims.md` use the unified project claim numbering
> (C01–C15). Individual evidence files may still carry the *per-source provisional* claim tags from
> extraction; where they differ, this index and `claims.md` are authoritative. The unified mapping:
> ARA-paper claims = C01–C09; oshima claims = C10–C12 (code-grounded, no table/figure evidence);
> multi-omics claims = C13–C15.

## Tables
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/ara_table1.md](tables/ara_table1.md) | ARA Table 1 | — (concept) | Research event types & structured payloads (Live Research Manager taxonomy) |
| [tables/ara_table2.md](tables/ara_table2.md) | ARA Table 2 | C01–C06 (setup) | PaperBench vs RE-Bench benchmark characteristics |
| [tables/ara_table3.md](tables/ara_table3.md) | ARA Table 3 | C01, C02 | Understanding/QA accuracy + token usage over 450 outcomes |
| [tables/ara_table4.md](tables/ara_table4.md) | ARA Table 4 | C08 | Rigor-Auditor mutation-benchmark detection rates |
| [tables/ara_table5.md](tables/ara_table5.md) | ARA Table 5 | C09 | Dimensional coverage: PDF / GitHub / Tracker / ARA |
| [tables/ara_table6.md](tables/ara_table6.md) | ARA Table 6 | C04 | Taxonomy of reproduction-critical information |
| [tables/ara_table7.md](tables/ara_table7.md) | ARA Table 7 | C01, C03 (setup) | Test corpus: 23 PaperBench papers (15 for reproduction) |
| [tables/ara_table8.md](tables/ara_table8.md) | ARA Table 8 | C04 | Reproduction info gap by category (45.4% fully specified) |
| [tables/ara_table9.md](tables/ara_table9.md) | ARA Table 9 | C04 | Gap-type distribution (missing hyperparameters 26.2%) |
| [tables/ara_table10.md](tables/ara_table10.md) | ARA Table 10 | C05 | Below-reference exploration cost (90.2% cost / 59.2% tokens / 113×) |
| [tables/ara_table11.md](tables/ara_table11.md) | ARA Table 11 | C03 | Per-paper reproduction success by difficulty (64.4 vs 57.4) |
| [tables/ara_table12.md](tables/ara_table12.md) | ARA Table 12 | C06, C07 (setup) | RE-Bench extension task card (scores, MALT counts) |
| [tables/ara_table13.md](tables/ara_table13.md) | ARA Table 13 | — (exploration) | Extension harness failure modes & fixes |
| [tables/ara_table14.md](tables/ara_table14.md) | ARA Table 14 | C08 | Per-paper × per-injection L2 detection (orphan blind spot) |

## Figures
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/ara_figure1.md](figures/ara_figure1.md) | ARA Figure 1 | C09 | PDF (lossy) vs ARA (lossless) — problem framing |
| [figures/ara_figure2.md](figures/ara_figure2.md) | ARA Figure 2 | C05 | Storytelling Tax: branching vs linear narrative |
| [figures/ara_figure3.md](figures/ara_figure3.md) | ARA Figure 3 | C04 | Reproduction information gap (mirrors Tables 8/9) |
| [figures/ara_figure4.md](figures/ara_figure4.md) | ARA Figure 4 | — (architecture) | ARA directory structure |
| [figures/ara_figure5.md](figures/ara_figure5.md) | ARA Figure 5 | C09 | Cross-layer forensic bindings of a real ARA |
| [figures/ara_figure6.md](figures/ara_figure6.md) | ARA Figure 6 | — (concept) | Live Research Manager session-boundary pipeline |
| [figures/ara_figure7.md](figures/ara_figure7.md) | ARA Figure 7 | — (concept) | ARA Compiler four-stage pipeline |
| [figures/ara_figure8.md](figures/ara_figure8.md) | ARA Figure 8 | C08 | ARA Seal three levels (+ human review) |
| [figures/ara_figure9.md](figures/ara_figure9.md) | ARA Figure 9 | — (concept) | Three-stage review pipeline |
| [figures/ara_figure10.md](figures/ara_figure10.md) | ARA Figure 10 | — (concept) | (Human+AI)² research network |
| [figures/ara_figure11.md](figures/ara_figure11.md) | ARA Figure 11 | C03 | Reproduction success by difficulty (grouped bar) |
| [figures/ara_figure12.md](figures/ara_figure12.md) | ARA Figure 12 | C06, C07 | Extension trajectories ×5 (Sonnet 4.6) |
| [figures/ara_figure13.md](figures/ara_figure13.md) | ARA Figure 13 | C03 | Per-paper ARA−baseline reproduction delta heatmap |
| [figures/ara_figure14.md](figures/ara_figure14.md) | ARA Figure 14 | C07 | triton_cumsum extension, Sonnet 4.5 (ARA 0.27 vs paper 0.64) |
| [figures/ara_figure15.md](figures/ara_figure15.md) | ARA Figure 15 | C07 | restricted_mlm extension, Sonnet 4.5 (ARA 0.73 vs paper 1.03) |
| [figures/mo_figure1.md](figures/mo_figure1.md) | Otte Figure 1 | C13 | Processed cholesterol-biosynthesis reaction interaction network |
| [figures/mo_figure2.md](figures/mo_figure2.md) | Otte Figure 2 | C13 | Embedding model: two-tower Linear→tanh→dot-product network |
| [figures/mo_figure3.md](figures/mo_figure3.md) | Otte Figure 3 | C13 | Objective schematic: one-hot → embedding → predicted context |
| [figures/mo_figure4.md](figures/mo_figure4.md) | Otte Figure 4 (a–d) | C13, C14, C15 | t-SNE clusters; omics intermixing; nearest-neighbor; bimodal dot products |

## Reading-confidence notes
- ARA Figures 12/14/15 axis readings are marked `≈` / `digitized_estimate`, with endpoints
  corroborated by §7.4 text.
- Multi-omics Figure 4 panel d histogram values are `≈` (digitized_estimate); panels a–c read
  structurally (no fabricated points).
- ARA Figure 8 contains a 4th "Human Review" card though the text names only Seal Levels L1–L3 —
  flagged in the figure file.
