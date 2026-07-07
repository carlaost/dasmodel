# Table 1: Sample characteristics of SHARE wave 9 and SHARE-HCAP subsample, weighted

- **Source**: Table 1, paper.pdf p.3 (Methods)
- **Caption**: "Sample characteristics of SHARE wave 9 and SHARE-HCAP subsample, weighted^a. Total household income per month (average) ADL, Activities of Daily Living; IADL, Instrumental Activities of Daily Living"
- **Screenshot**: table1.png
- **Extraction type**: raw_table

| Characteristic | SHARE-HCAP subsample (N=2687) | SHARE parent Wave 9 (N=47,733) |
|---|---|---|
| Response rate, % | 75.8 | 68.4 |
| **Age** | | |
| Mean (SD), y | 75.5 (7.5) | 75.6 (7.7) |
| **Sex** | | |
| Female, % | 56.2 | 56.6 |
| Male, % | 43.8 | 43.4 |
| **Education (ISCED 1997)** | | |
| primary school or less, % | 20.0 | 23.2 |
| Some high school, % | 14.9 | 17.7 |
| High school or some college, % | 39.8 | 37.7 |
| college degree or more, % | 25.3 | 21.4 |
| **Health** | | |
| ADL + IADL, mean (SD) | 0.9 (2.1) | 1.2 (2.9) |
| **Household income** | | |
| Median in Euro (IQR) | 2000 (1700) | 1600 (1800) |

## Notes
- a Total household income per month (average). ADL = Activities of Daily Living; IADL = Instrumental Activities of Daily Living.
- The table header states the SHARE parent Wave 9 N as 47,733. Elsewhere in the paper, the Methods intro text (p.2) states "It includes 47,733 individuals of age 65 and older," while the Abstract (p.1) states "SHARE, 47,773 individuals age 65 and older" — a digit-transposition discrepancy (47,733 vs 47,773) between the Abstract and the Methods/Table 1 text. Neither number is the analytical sample used for prevalence estimation, which is N=47,193 (Table 3; see `logic/solution/constraints.md` for the full discrepancy note).
- The SHARE-HCAP subsample N is given as 2,687 here and in the Results text ("Of the 3,546 eligible individuals, 2,687 participated"), but the Methods intro (p.2) states "we drew a validation subsample (N = 2,678)" — a similar digit-transposition discrepancy (2,678 vs 2,687). This ARA reports both instances verbatim and does not silently resolve them (see `logic/solution/constraints.md`).
