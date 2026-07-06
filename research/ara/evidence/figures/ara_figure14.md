# Figure 14: triton_cumsum on Sonnet 4.5 — paper vs ARA

- **Source**: Figure 14, Appendix G.6 / G.6.1 (Case study: triton_cumsum)
- **Caption**: "triton_cumsum on Sonnet 4.5: paper vs. ARA score-vs-time (left) and score-vs-cost (right). Faint markers are raw scoring attempts ..."
- **Screenshot**: ara_figure14.png
- **Figure type**: quantitative_plot
- **Extraction method**: digitized_estimate (endpoints confirmed by §7.4 text)
- **Reading confidence**: high
- **Plot kind**: line (best-so-far) + scatter, two panels (vs wall-clock min; vs cumulative API cost USD)
- **Axes**: Y = log(t_ms), lower is better (↓); X-left = wall-clock minutes (0–500); X-right = cumulative API cost USD (0–80). Dotted grey = RE-Bench reference 0.47. Series: paper (Sonnet 4.5) blue, ARA (Sonnet 4.5) orange.

| Series | Best final score (log t_ms) |
|--------|------------------------------|
| ARA (Sonnet 4.5) | ≈0.27 (text: 0.27) |
| paper (Sonnet 4.5) | ≈0.64 (text: 0.64) |
| RE-Bench reference | 0.47 |

## Trend summary
On the weaker Sonnet 4.5 base the comparison INVERTS relative to Sonnet 4.6: the ARA agent (≈0.27) beats the paper agent (≈0.64) and both beat the reference 0.47 (lower better). Both 4.5 agents leave the official 3-pass kernel structure intact and only tune autotune configs; the ARA agent's trace-cited conservative grid (NUM_STAGES ∈ {4,8}, heuristic H01) wins.
