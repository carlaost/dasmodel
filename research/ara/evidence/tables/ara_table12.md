# Table 12: RE-Bench task card with extension-evaluation status

**Source**: Table 12, Appendix G.1 (Task selection)
**Caption**: "RE-Bench task card with extension-evaluation status. Score formula is transcribed verbatim from metr-re-bench/ai_rd_<task>/ai_rd_<task>.py; ℓ denotes validation loss, t wall-clock time, n_solved the count of correctly solved problems, ε_ℓ/ε_p loss/parameter prediction errors. Dir.: score orientation. Start: score of the unmodified starter codebase. Ref.: best score reported in the original RE-Bench evaluation. Claude-4 MALT: count of Claude-4 (Opus + Sonnet) runs in the METR MALT corpus, broken down as O⟨Opus⟩/S⟨Sonnet⟩. † rust_codecontests also has a 10-run claude-3-7-sonnet supplement that uses the same scoring scaffold. ‡ only Claude-3.5/3.7 and OpenAI runs. § no MALT corpus published."
**Screenshot**: ara_table12.png
**Extraction type**: raw_table

| Task | Score formula | Dir. | Start | Ref. | Hardware | Claude-4 MALT | Used |
|------|---------------|------|-------|------|----------|---------------|------|
| triton_cumsum | log(t_ms) | ↓ | 1.56 | 0.47 | 1×H100 | 22 (O13/S9) | yes |
| restricted_mlm | log(ℓ−1.5) | ↓ | 1.81 | 1.13 | 2×H100 80 GB | 22 (O11/S11) | yes |
| fix_embedding | log(ℓ_val−1.5) | ↓ | 2.20 | 0.26 | 1×GPU | 19 (O10/S9) | yes |
| nanogpt_chat_rl | avg. pairwise win-rate | ↑ | 0.54 | 0.85 | 1×GPU + judge | 18 (O12/S6) | yes |
| rust_codecontests | n_solved/165 | ↑ | 0.00 | 0.13 | CPU + LLM API | 12 (O6/S6) + 10† | yes |
| small_scaling_law | 1−(ε_ℓ+ε_p) | ↑ | 0.24 | 0.84 | 1×GPU | 0‡ | no |
| optimize_llm_foundry | log(t_s) | ↓ | 5.60 | 4.54 | 4×H100 | 0§ | no |
