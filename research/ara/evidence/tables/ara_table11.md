# Table 11: Per-paper reproduction success rates (%) by difficulty level

**Source**: Table 11, Appendix F.2 (Per-Paper Reproduction Analysis)
**Caption**: "Per-paper reproduction success rates (%) by difficulty level. Easy, medium, and hard columns show the unweighted success rate within each difficulty tier; the final two columns show the difficulty-weighted rate (1:2:3 weighting). Rice per-difficulty values are interpolated from the weighted score and overall rate, as its per-difficulty JSON entry was recorded separately."
**Screenshot**: ara_table11.png
**Extraction type**: raw_table

ARA = ARA agent, Base/BL = PDF+GitHub baseline. Easy/Med./Hard = unweighted per-tier success rate (%). Weighted = difficulty-weighted (1:2:3) success rate (%).

| Paper | ARA Easy | ARA Med. | ARA Hard | BL Easy | BL Med. | BL Hard | Weighted ARA | Weighted Base |
|-------|----------|----------|----------|---------|---------|---------|--------------|---------------|
| adaptive-pruning | 90.9 | 80.0 | 31.7 | 89.8 | 83.0 | 35.0 | 63.5 | 65.8 |
| all-in-one | 90.4 | 92.0 | 61.1 | 91.3 | 87.5 | 42.0 | 72.8 | 60.4 |
| bam | 97.1 | 97.1 | 77.6 | 100.0 | 95.1 | 89.5 | 88.2 | 93.2 |
| bbox | 93.3 | 59.5 | 31.6 | 97.8 | 52.7 | 17.3 | 49.8 | 40.8 |
| fre | 79.3 | 45.4 | 50.9 | 62.2 | 32.6 | 28.6 | 53.2 | 34.4 |
| ftrl | 25.0 | 38.0 | 32.0 | 36.2 | 54.4 | 30.0 | 33.0 | 38.8 |
| mechanistic-und. | 85.7 | 88.3 | 67.1 | 82.5 | 36.7 | 55.0 | 76.2 | 55.0 |
| pinn | 96.2 | 93.8 | 89.8 | 78.8 | 75.0 | 65.9 | 92.2 | 71.0 |
| rice | 72.3 | 72.1 | 65.8 | 74.1 | 73.9 | 68.0 | 69.9 | 71.8 |
| sample-specific-masks | 95.6 | 29.8 | 31.1 | 95.6 | 35.7 | 25.7 | 42.7 | 42.3 |
| self-composing-pol. | 87.5 | 46.5 | 52.3 | 93.3 | 36.0 | 37.2 | 57.3 | 47.8 |
| self-expansion | 34.7 | 37.5 | 39.3 | 20.8 | 65.0 | 47.3 | 38.2 | 48.9 |
| sequential-neural | 95.2 | 68.3 | 51.6 | 69.3 | 53.5 | 39.7 | 64.8 | 49.3 |
| stochastic-interpolants | 97.7 | 100.0 | 74.1 | 95.5 | 100.0 | 72.4 | 86.7 | 85.3 |
| test-time-model-adapt. | 87.8 | 43.5 | 19.8 | 94.4 | 50.0 | 15.9 | 35.1 | 35.0 |
| **Mean** | 85.1 | 68.5 | 54.5 | 80.2 | 62.9 | 46.0 | 64.4 | 57.4 |
