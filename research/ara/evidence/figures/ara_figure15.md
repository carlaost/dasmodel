# Figure 15: restricted_mlm on Sonnet 4.5 — paper vs ARA

- **Source**: Figure 15, Appendix G.6 (Case study: restricted_mlm)
- **Caption**: "restricted_mlm on Sonnet 4.5: paper vs. ARA score-vs-time (left) and score-vs-cost (right). Faint markers are raw scoring attempts ..."
- **Screenshot**: ara_figure15.png
- **Figure type**: quantitative_plot
- **Extraction method**: digitized_estimate (endpoints confirmed by §7.4 text)
- **Reading confidence**: high
- **Plot kind**: line (best-so-far) + scatter, two panels (vs wall-clock min; vs cumulative API cost USD)
- **Axes**: Y = log(ℓ_val − 1.5), lower is better (↓); X-left = wall-clock minutes (0–500); X-right = cumulative API cost USD (0–80). Dotted grey lines: untrained baseline 1.84, RE-Bench reference 1.13. Series: paper (Sonnet 4.5) blue, ARA (Sonnet 4.5) orange.

| Series | Best final score (log ℓ_val−1.5) |
|--------|----------------------------------|
| ARA (Sonnet 4.5) | ≈0.73 (text: 0.73) |
| paper (Sonnet 4.5) | ≈1.03 (text: 1.03) |
| RE-Bench reference | 1.13 |
| untrained baseline | 1.84 |

## Trend summary
On Sonnet 4.5 the ARA agent (≈0.73) clearly beats the paper agent (≈1.03), and both beat the reference 1.13 (lower better) — inverting the Sonnet 4.6 result where the paper agent won. A weaker base lacks bandwidth to commit deeply to a single architecture, so the heuristic-named ranked alternatives in the trace give the ARA agent a productive playbook.
