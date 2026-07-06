# Grounding: reconstructed — from explicit paper equations (Aku25b §2, Eqs. 3 and 6).
# No repository or released code exists for this paper (no Code Availability statement;
# sources.yaml `code: []`). This module reconstructs ONLY the novel closed-form mechanism —
# the PAF-based exposure/vulnerability decomposition of a disparity factor — directly from the
# printed equations. Cox-model estimation itself is prose-only in the paper and is NOT reimplemented
# here (it would be invented plumbing). Inputs are the estimated relative risks and prevalences.

import math


def paf(prevalence: float, relative_risk: float) -> float:
    """Population attributable fraction for one subpopulation and one predictor.

    Aku25b Eq. 3:
        PAF = P * (R - 1) / [ P * (R - 1) + 1 ]
    where P is the baseline prevalence of the predictor in the subpopulation and R its relative
    risk (R_0i = exp(beta_0i) for the advantaged group, R_1i = exp(beta_1i) for the disadvantaged).
    """
    return prevalence * (relative_risk - 1.0) / (prevalence * (relative_risk - 1.0) + 1.0)


def predictor_factor(p0: float, p1: float, r0: float, r1: float) -> float:
    """Total factor f_i of a predictor in the disparity (Aku25b Eq. 6).

        f_i = (1 - PAF_0i) / (1 - PAF_1i)
            = [1 + P_1i (R_1i - 1)] / [1 + P_0i (R_0i - 1)]

    p0, p1: prevalences in advantaged (0) and disadvantaged (1) subpopulations.
    r0, r1: relative risks R_0i, R_1i.
    """
    return (1.0 + p1 * (r1 - 1.0)) / (1.0 + p0 * (r0 - 1.0))


def exposure_effect(p0: float, p1: float, r0: float, r1: float) -> float:
    """Exposure effect E_i (Aku25b Eq. 6): the prevalence-driven contribution.

        E_i = sqrt( (1 + P_1i(R_0i - 1)) / (1 + P_0i(R_0i - 1))
                    * (1 + P_1i(R_1i - 1)) / (1 + P_0i(R_1i - 1)) )
    """
    term_a = (1.0 + p1 * (r0 - 1.0)) / (1.0 + p0 * (r0 - 1.0))
    term_b = (1.0 + p1 * (r1 - 1.0)) / (1.0 + p0 * (r1 - 1.0))
    return math.sqrt(term_a * term_b)


def vulnerability_effect(p0: float, p1: float, r0: float, r1: float) -> float:
    """Vulnerability effect V_i (Aku25b Eq. 6): the per-exposure-risk-driven contribution.

        V_i = sqrt( (1 + P_1i(R_1i - 1)) / (1 + P_1i(R_0i - 1))
                    * (1 + P_0i(R_1i - 1)) / (1 + P_0i(R_0i - 1)) )
    """
    term_a = (1.0 + p1 * (r1 - 1.0)) / (1.0 + p1 * (r0 - 1.0))
    term_b = (1.0 + p0 * (r1 - 1.0)) / (1.0 + p0 * (r0 - 1.0))
    return math.sqrt(term_a * term_b)


def observed_risk_ratio(r_r: float, factors: list) -> float:
    """Observed disparity RR = R_r * prod_i f_i  (Aku25b Eq. 6).

    r_r: unexplained disparity R_r = exp(beta_r).
    factors: list of per-predictor total factors f_i from `predictor_factor`.
    """
    rr = r_r
    for f in factors:
        rr *= f
    return rr


# Identity guaranteed by Eq. 6: f_i = E_i * V_i (multiplicative decomposition; Table 4 footnote c).
# The paper does not report per-predictor prevalences and relative risks numerically for every cell,
# so no worked numeric example from raw inputs is asserted here (would be fabrication). The tabulated
# f_i = E_i * V_i values are reproduced verbatim in evidence/tables/table4.md.
