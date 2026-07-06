# Figure 1: Contribution of low income (dual eligibility) to AD-risk disparities across age

- **Source**: Figure 1, §3 Results (p. 8)
- **Caption**: "Hazard ratio of observed disparities (solid points), the unexplained part of the disparities (open dots), and the effect of low income (dashed line that shows the product of unexplained disparity factors and the factors representing the effect of dual eligibility/low income). BW, Black–White; FM, female–male; HR, hazard ratio; HW, Hispanic–White; SB, stroke belt; WA, White–Asian; WN, White–Native American."
- **Screenshot**: figure1.png
- **Figure type**: quantitative_plot
- **Extraction method**: exact_from_labels (the two point series are the exact Observed / Unexplained values tabulated in Table 4; the dashed low-income series is an ARA-computed product marked ≈)
- **Reading confidence**: high

- **Plot kind**: line (three series over age), six panels
- **Axes**: X = Age (years; values 70, 75, 80, 85; linear), Y = Hazard Ratio (dimensionless; linear; per-panel scale differs)
- **Panels**: BW (Black–White), WN (White–Native American), HW (Hispanic–White), WA (White–Asian), FM (female–male), SB (stroke belt)
- **Series**:
  - Observed HR (solid points) = "Observed … disparity" row of Table 4
  - HR of disparity indicator (open dots) = "Unexplained … disparity" row of Table 4 (`R_r = exp(β_r)`)
  - HR of disparity indicator and low income (dashed line, small filled dots) = Unexplained × low-income total factor (product of the unexplained disparity and the low-income `f = E*V` factor)

The point series below reproduce Table 4 exactly (not digitized). The dashed low-income series is computed here as (Unexplained × low-income total factor) and marked `≈`.

| Panel | Age | Observed HR (solid) | Unexplained HR (open) | + Low-income (dashed) ≈ |
|-------|-----|---------------------|-----------------------|--------------------------|
| BW | 70 | 1.65 | 1.43 | ≈1.59 |
| BW | 75 | 1.46 | 1.24 | ≈1.33 |
| BW | 80 | 1.30 | 1.15 | ≈1.23 |
| BW | 85 | 1.17 | 1.05 | ≈1.10 |
| WN | 70 | 1.26 | 2.10 | ≈1.62 |
| WN | 75 | 1.18 | 1.61 | ≈1.59 |
| WN | 80 | 1.12 | 1.33 | ≈1.33 |
| WN | 85 | 1.25 | 1.56 | ≈1.45 |
| HW | 70 | 1.21 | 0.77 | ≈1.00 |
| HW | 75 | 1.21 | 0.95 | ≈0.97 |
| HW | 80 | 1.19 | 0.96 | ≈0.94 |
| HW | 85 | 1.10 | 0.81 | ≈0.79 |
| WA | 70 | 1.40 | 1.86 | ≈1.40 |
| WA | 75 | 1.53 | 2.25 | ≈1.85 |
| WA | 80 | 1.46 | 1.79 | ≈1.81 |
| WA | 85 | 1.48 | 1.60 | ≈1.94 |
| FM | 70 | 1.24 | 1.20 | ≈1.22 |
| FM | 75 | 1.21 | 1.21 | ≈1.23 |
| FM | 80 | 1.20 | 1.26 | ≈1.29 |
| FM | 85 | 1.19 | 1.27 | ≈1.31 |
| SB | 70 | 1.58 | 1.47 | ≈1.53 |
| SB | 75 | 1.48 | 1.46 | ≈1.52 |
| SB | 80 | 1.43 | 1.42 | ≈1.49 |
| SB | 85 | 1.37 | 1.43 | ≈1.50 |

## Trend summary
- BW and SB: observed disparity **decreases monotonically** with baseline age (BW 1.65→1.17; SB 1.58→1.37); adding low income to the unexplained part lifts the curve toward the observed value, i.e., low income accounts for a visible share of the BW/SB disparity. The effect of low income is strongest for Black–White, White–Asian, and stroke-belt disparities (§3).
- HW: the unexplained part sits **below 1** (open dots 0.77–0.96), so predictors more than explain the observed Hispanic–White disparity; adding low income (dashed) tracks the unexplained curve closely, confirming low income as the dominant contributor.
- WN and WA: the unexplained part lies **above** the observed disparity across ages (open dots exceed solid points), so the examined predictors act to *increase* the apparent disparity; the low-income effect is notable mainly at age 70 for WN (§3, p. 9).
- FM: small effects — observed and unexplained curves are close (all within ≈1.19–1.27); the unexplained part slightly exceeds the observed disparity at older ages, meaning predictors explain a larger share of male risk at advanced ages, enlarging the unexplained female–male gap.
- Cross-panel: for all disparities the effect of low income is larger than the effect of vulnerability (dashed line moves the unexplained curve toward observed via the exposure channel).
