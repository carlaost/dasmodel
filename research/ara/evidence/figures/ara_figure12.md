# Figure 12: Extension trajectories on five RE-Bench tasks (Claude Sonnet 4.6)

- **Source**: Figure 12, §7.4 (Extension from ARA)
- **Caption**: "Extension trajectories on five RE-Bench tasks under Claude Sonnet 4.6. One task per column: top row is score-vs-wall-clock-time, bottom row is score-vs-cumulative-cost; the y-axis is shared down each column. Faint markers are individual scoring attempts, solid lines are the best-so-far envelope, and stars mark the best attempt; dotted grey lines mark each task's RE-Bench reference. Arrows in the column titles indicate metric direction. Across all five tasks the ARA agent reaches a useful first move earlier than the paper agent, and ends with the better best score on rust_codecontests, nanogpt_chat_rl, and fix_embedding; on triton_cumsum and restricted_mlm the paper agent later overtakes ..."
- **Screenshot**: ara_figure12.png
- **Figure type**: quantitative_plot
- **Extraction method**: digitized_estimate
- **Reading confidence**: medium
- **Plot kind**: line (best-so-far envelope) + scatter (raw attempts), 5 columns × 2 rows
- **Axes**: X (top row) = wall-clock minutes (0–500, linear); X (bottom row) = cumulative API cost USD (0–~80, linear). Y = per-task score (different metric/scale per column, see direction arrows). Series: paper (Sonnet 4.6) vs ARA (Sonnet 4.6); dotted line = RE-Bench reference.

Per-column task, direction, and reference (reference values from Table 12). Higher-is-better ↑ / lower-is-better ↓.

| Task | Dir. | Ref. | Outcome (who ends ahead) |
|------|------|------|--------------------------|
| triton_cumsum | ↓ (log t_ms) | 0.47 | paper agent ends ahead (int8 redesign at t≈47.7 min) |
| rust_codecontests | ↑ (n_solved/165) | 0.13 | ARA agent ends ahead (commits to hand-coded Rust lib at t≈9 min via H12) |
| nanogpt_chat_rl | ↑ (win-rate) | 0.85 | ARA agent ends ahead (H08 pre-names degenerate-output filter) |
| fix_embedding | ↓ (log ℓ_val−1.5) | 0.26 | ARA agent ends ahead (H11/H13 mark a documented dead end) |
| restricted_mlm | ↓ (log ℓ−1.5) | 1.13 | paper agent ends ahead (single ConvMLMDilated tune, 8 h) |

## Trend summary
On all five tasks the ARA agent reaches a useful first scoring move earlier (e.g., triton_cumsum: ARA scores ≈0.47 at t≈11 min vs paper's first score at t≈37 min; rust: ARA commits at t≈9 min vs paper t≈395 min). The early ARA lead converts to a final win on 3/5 tasks; on triton_cumsum and restricted_mlm the more capable Sonnet 4.6 paper agent overtakes via moves the trace never names. Net: trace-preservation accelerates the first move universally but can constrain a high-capability agent from out-of-box exploration.
