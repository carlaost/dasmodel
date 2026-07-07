# Claims

All numbers are copied exactly from the paper text (paper.pdf). Values describing the review's own screening/appraisal output are tagged `[result]`; values that are pre-specified review-design parameters (search string, timeframe, thresholds) are tagged `[input]`. Two claims below (C01, C04) flag internal numeric inconsistencies within the source paper itself (Abstract vs. Results; stated-n vs. listed-citation-count) — these are reported honestly, not resolved by guessing.

## C01: Systematic search and screening yielded 29 included studies
- **Statement**: The main database search identified 1748 studies; 4 additional studies were identified through reference mining of three systematic reviews. After removing duplicates, 1202 unique studies remained. Title/abstract screening excluded 1129 as irrelevant, leaving 73 publications for full-text review. Full-text review excluded 44 studies, yielding 29 studies that met the inclusion criteria.
- **Status**: supported
- **Falsification criteria**: Disproved if the PRISMA flow numbers (1748, 4, 1202, 1129, 73, 44, 29) reported in the Results/Fig. 1 differ from these values.
- **Proof**: [E01]
- **Evidence basis**: §Results "Study selection and quality assessment" and Fig. 1 (PRISMA flow diagram) report this pipeline in full.
- **Interpretation**: The review's evidence base (29 studies) represents roughly 1.7–2.4% of the initially identified/screened record pool, reflecting a narrow but PRISMA-compliant filter for Europe-specific, barrier-focused, non-RCT original research.
- **Dependencies**: none
- **Sources**:
  - 1748 studies identified ← paper.pdf §Results "The main research search identified 1748 studies." [result]
  - 4 studies via reference mining ← paper.pdf §Results "Additionally, 4 studies were identified through reference mining of three systematic reviews [36–38]." [result]
  - 1202 unique studies after dedup ← paper.pdf §Results "duplicates were removed using Rayyan, and a database of 1202 unique studies was compiled." [result]
  - 1129 excluded at title/abstract ← paper.pdf §Results "Upon review of their titles and abstracts, 1129 studies were deemed irrelevant and excluded." [result]
  - 73 full-text reviewed ← paper.pdf §Results "Subsequently, 73 publications underwent a full-text review, resulting in the selection of 29 studies meeting the inclusion criteria." [result]
  - 29 studies included ← same sentence as above. [result]
  - Fig. 1 confirms the same figures: 1748 (database), 4 (reference list), 1202 (after dedup), 1129 (excluded titles/abstracts), 73 (full-text assessed), 44 (full-text excluded), 29 (included) ← paper.pdf Fig. 1 caption/diagram. [result]
- **Note — internal source inconsistency**: The Abstract states "Over 1298 articles, 29 studies met the inclusion criteria" ← paper.pdf Abstract "Over 1298 articles, 29 studies met the inclusion criteria." [result] — this figure (1298) does not match any of the Results/Fig. 1 pipeline numbers (1748 identified, 1202 unique, 73 full-text reviewed). This is an unresolved discrepancy within the source document itself, reported here without guessing which number is authoritative.
- **Tags**: PRISMA, screening, search-strategy

## C02: 44 studies were excluded at full-text review for four documented reasons
- **Statement**: Of the 73 full-text-reviewed publications, 44 were excluded: 27 lacked assessments of barriers, 12 were excluded due to study design or type, 4 were not set in a European nation, and 1 was not focused on people living with dementia.
- **Status**: supported
- **Falsification criteria**: Disproved if the stated exclusion-reason counts (27, 12, 4, 1) do not sum to 44 or differ from the text.
- **Proof**: [E01]
- **Evidence basis**: §Results "Study selection and quality assessment" states these four exclusion-reason counts explicitly; they sum to 44 (27+12+4+1=44), matching Fig. 1.
- **Interpretation**: The dominant reason for full-text exclusion (27/44, ~61%) was that a paper — despite passing title/abstract screening — did not actually assess a barrier to care, indicating that "dementia care" framing alone was an imprecise screening signal at the abstract stage.
- **Dependencies**: C01
- **Sources**:
  - 27 lacked barrier assessments ← paper.pdf §Results "27 studies lacked assessments of barriers" [result]
  - 12 excluded for study design/type ← paper.pdf §Results "12 studies were excluded due to study design or type" [result]
  - 4 not set in Europe ← paper.pdf §Results "4 studies were not set in a European nation" [result]
  - 1 wrong population ← paper.pdf §Results "1 study was not focused on people living with dementia" [result]
  - Fig. 1 corroborates: "Did not analyse barriers (n=27); Study design/type (n=12); Not set in a European nation (n=4); Different population (n=1)" ← paper.pdf Fig. 1. [result]
- **Tags**: PRISMA, exclusion-reasons, eligibility

## C03: Most included studies scored the maximum MMAT quality rating; three scored lower
- **Statement**: Most studies received an MMAT quality score of 100%, meeting all criteria for methodological rigor. Three studies scored below 100%: Giebel C. et al., 2021 [58] and Rusowicz J. et al., 2021 [63] each scored 30%, and Dibao-Dina C. et al., 2022 [67] scored 40%; these were mixed-methods or quantitative studies with limitations such as potential sampling/non-response biases or insufficient methodological detail.
- **Status**: supported
- **Falsification criteria**: Disproved if Table 3's per-study quality scores differ from 100% for any study not listed here, or if the three named lower-scoring studies do not carry 30%/30%/40% respectively.
- **Proof**: [E02]
- **Evidence basis**: §Results "Study selection and quality assessment" narrative + Table 3 per-study "Quality score" column (26 of 29 studies listed at 100%; the 3 exceptions at 30%, 30%, 40%).
- **Interpretation**: In mixed-methods studies, MMAT scoring rules dictate that the overall quality score cannot surpass the weakest component's score, which is why mixed-methods studies with a weak quantitative arm (ref 58, ref 67) score lower than purely qualitative studies.
- **Dependencies**: none
- **Sources**:
  - "Most studies received a quality score of 100%" ← paper.pdf §Results "Most studies received a quality score of 100%, meeting all criteria for methodological rigor" [result]
  - "Articles with scores below 100%—particularly those with scores of 30% or 40%—were mixed methods or quantitative studies" ← paper.pdf §Results (same paragraph) [result]
  - Giebel C. et al., 2021 [58] = 30% ← paper.pdf Table 3 row "Giebel C. et al., 2021 [58] ... 30%" [result]
  - Rusowicz J. et al., 2021 [63] = 30% ← paper.pdf Table 3 row "Rusowicz J. et al., 2021 [63] ... 30%" [result]
  - Dibao-Dina C. et al., 2022 [67] = 40% ← paper.pdf Table 3 row "Dibao-Dina C. et al., 2022 [67] ... 40%" [result]
  - MMAT scoring rule ← paper.pdf §Methods "In mixed methods studies, the overall quality of the combination cannot surpass the quality of its weakest component." [input]
- **Tags**: quality-assessment, MMAT, risk-of-bias

## C04: Barriers were categorised into five/six named domains with reported study counts
- **Statement**: Identified barriers were categorised into: organisational barriers (n=17), information and educational barriers (n=11), cultural and stigma-related barriers (n=10), logistical barriers (n=6), and financial barriers (n=4).
- **Status**: supported (with a noted citation-count inconsistency for the cultural/stigma category)
- **Falsification criteria**: Disproved if the stated per-category counts (17, 11, 10, 6, 4) differ from the text, or if a study's citation number appears in a category count total to which it was not assigned.
- **Proof**: [E03]
- **Evidence basis**: §Results "Identified barriers" paragraph states each category and its n, each followed by a citation list.
- **Interpretation**: Organisational barriers (poor coordination, unclear access procedures) are the most commonly reported domain, affecting well over half the included studies (17/29, ~59%), consistent with the Discussion's emphasis on fragmented services and poor care-team coordination as pan-European issues.
- **Dependencies**: C01
- **Sources**:
  - organisational barriers n=17 ← paper.pdf §Results "organisational barriers (n = 17) [40–44, 46–51, 53, 59–63, 65, 66]" [result]
  - informational/educational barriers n=11 ← paper.pdf §Results "information and educational barriers (n = 11) [39, 40, 44, 46, 48, 49, 51, 54, 56, 62, 66]" [result]
  - cultural/stigma-related barriers n=10 ← paper.pdf §Results "cultural and stigma-related barriers (n = 10) [42, 48, 52, 54, 57, 58, 66]" [result]
  - logistical barriers n=6 ← paper.pdf §Results "logistical barriers (n = 6) [44, 48, 49, 51, 55, 64]" [result]
  - financial barriers n=4 ← paper.pdf §Results "financial barriers (n = 4) [43, 48, 49, 67]" [result]
- **Note — internal source inconsistency**: The cultural/stigma-related category is stated as n=10 but the paper lists only 7 citation numbers ([42, 48, 52, 54, 57, 58, 66]) immediately after it, a mismatch between the stated count and the enumerated reference list. This is reported as-is from the source rather than silently corrected or padded with invented citations.
- **Tags**: barrier-taxonomy, narrative-synthesis, thematic-categorisation

## C05: The 29 included studies span 2013–2022 with a concentration in 2020–2021
- **Statement**: The 29 included studies, spanning from 2013 to 2022, were published as follows: two in 2013, one in 2014, one in 2015, one in 2017, three in 2018, three in 2019, eight in 2020, eight in 2021, and two in 2022.
- **Status**: supported
- **Falsification criteria**: Disproved if these per-year counts do not sum to 29 or differ from the text.
- **Proof**: [E04]
- **Evidence basis**: §Results "Study characteristics" states the year-by-year breakdown explicitly; counts sum to 29 (2+1+1+1+3+3+8+8+2=29).
- **Interpretation**: 16 of 29 studies (55%) were published in 2020–2021, coinciding with the COVID-19 pandemic period, which the review separately notes affected several studies' focus (4 explicitly focused on COVID-19, 3 did not focus on it, 2 did not mention it).
- **Dependencies**: C01
- **Sources**:
  - year distribution ← paper.pdf §Results "The publication years were: two studies in 2013 [39, 40], one study in 2014 [41], one in 2015 [42], one in 2017 [43], three in 2018 [44–46], three in 2019 [47–49], eight in 2020 [50–57], eight in 2021 [58–65], and two in 2022 [66, 67]." [result]
  - COVID-19 focus breakdown ← paper.pdf §Results "explicitly focused on it (n = 4) [55, 59, 60, 63, 64], did not focus on it (n = 3) [61, 66, 67], did not mention it (n = 2) [58, 65]." [result]
- **Tags**: study-characteristics, publication-timeline, COVID-19

## C06: Included studies are geographically concentrated in the UK, with several multi-country projects
- **Statement**: Most of the 29 studies were conducted primarily in the UK (n=13); other studies were multi-country (Actifcare project, n=2; Intermediate care for dementia in Europe, n=1; Italy and the Netherlands, n=1; Switzerland and Liechtenstein, n=1; the UK and the Netherlands, n=1) or single-country (Germany n=2, Norway n=2, Spain n=1, Denmark n=1, Finland n=1, Poland n=1, Portugal n=1, Ireland n=1).
- **Status**: supported
- **Falsification criteria**: Disproved if these per-country/project counts differ from the text or do not account for all 29 studies.
- **Proof**: [E04]
- **Evidence basis**: §Results "Study characteristics" enumerates the geographic distribution explicitly.
- **Interpretation**: The strong UK concentration (13/29, ~45%) likely reflects publication/language bias (English-only inclusion criterion) more than an actual geographic concentration of the underlying barriers, a limitation the authors acknowledge separately (restriction to English-language studies "may introduce language and geographical biases").
- **Dependencies**: C01
- **Sources**:
  - UK n=13 ← paper.pdf §Results "Most of the studies were conducted primarily in the United Kingdom (UK) (n = 13) [39–41, 44, 47, 49, 52, 54, 55, 59, 60, 64, 65]" [result]
  - Actifcare n=2 ← paper.pdf §Results "multi-country studies under the Actifcare project (n = 2) [46, 48]" [result]
  - Intermediate care for dementia in Europe n=1 ← paper.pdf §Results "the Intermediate care for dementia in Europe (n = 1) [67]" [result]
  - two-country studies (Italy/Netherlands n=1, Switzerland/Liechtenstein n=1, UK/Netherlands n=1) ← paper.pdf §Results "Italy and the Netherlands (n = 1) [43], Switzerland and Liechtenstein (n = 1) [61] and the UK and the Netherlands (n = 1) [58]" [result]
  - single-country counts (Germany n=2, Norway n=2, Spain n=1, Denmark n=1, Finland n=1, Poland n=1, Portugal n=1, Ireland n=1) ← paper.pdf §Results "in Germany (n = 2) [42, 56], in Norway (n = 2) [45, 50], Spain (n = 1) [51], Denmark (n = 1) [53], Finland (n = 1) [62], Poland (n = 1) [63], Portugal (n = 1) [66], and Ireland (n = 1) [57]." [result]
  - English-language bias acknowledgement ← paper.pdf §Discussion "Strengths and limitations" "the restriction to studies published in English may introduce language and geographical biases, potentially overlooking valuable insights from non-English literature." [result]
- **Tags**: study-characteristics, geographic-distribution, limitation

## C07: Included studies used predominantly qualitative methods
- **Statement**: Of the 29 studies, 24 were qualitative (13 using interviews, 3 using focus groups, 7 using both interviews and focus groups, 1 using a combination of survey and focus groups), 2 were mixed-methods (1 survey-only, 1 combining surveys and interviews), and 3 were quantitative studies using a survey.
- **Status**: supported
- **Falsification criteria**: Disproved if these method-type counts (24 qualitative, 2 mixed, 3 quantitative, with the stated sub-breakdowns) do not sum to 29 or differ from the text.
- **Proof**: [E04]
- **Evidence basis**: §Results "Study characteristics" states the methods breakdown explicitly; 24+2+3=29.
- **Interpretation**: The dominance of qualitative designs (24/29, ~83%) reflects the review's a priori exclusion of RCTs, prioritizing in-depth, context-specific accounts of barriers over intervention-testing designs — a deliberate scope decision the authors defend in the Discussion despite it being "a fundamental limitation."
- **Dependencies**: C01
- **Sources**:
  - qualitative n=24, interviews n=13, focus groups n=3, both n=7, survey+focus-group n=1 ← paper.pdf §Results "Qualitative studies (n = 24) utilised various techniques, including interviews (n = 13) [39–41, 44, 47, 48, 50, 55–57, 59, 61, 64], focus groups (n = 3) [42, 43, 46], both interviews and focus groups (n = 7) [45, 49, 52, 54, 62, 65, 66], and a combination of survey and focus groups (n = 1) [51]." [result]
  - mixed-methods n=2 (surveys n=1, surveys+interviews n=1) ← paper.pdf §Results "Mixed-methods studies (n = 2) included surveys (n = 1) [67] and a combination of surveys and interviews (n = 1) [58]." [result]
  - quantitative n=3, all survey ← paper.pdf §Results "three quantitative studies (n = 3) employed a survey [53, 60, 63]." [result]
  - RCT exclusion as deliberate design choice ← paper.pdf §Discussion "Strengths and limitations" "A fundamental limitation of this review is the deliberate exclusion of randomized controlled trials (RCTs)... this choice was made to prioritize an in-depth assessment of real-world challenges, which aligns closely with research objectives." [result]
- **Tags**: study-characteristics, methodology, qualitative-vs-quantitative

## C08: Included studies varied in population focus, spanning six population-group combinations
- **Statement**: Across the 29 studies, population focus was: HCWs only (n=9), people living with dementia only (n=1), caregivers only (n=5), both caregivers and HCWs (n=6), both PLWD and caregivers (n=5), and PLWD + caregivers + HCWs together (n=3).
- **Status**: supported
- **Falsification criteria**: Disproved if these six population-group counts do not sum to 29 or differ from the text.
- **Proof**: [E04]
- **Evidence basis**: §Results "Study characteristics" enumerates population focus explicitly; 9+1+5+6+5+3=29.
- **Interpretation**: HCWs are the single most-studied population as a sole focus (9/29), while direct study of PLWD alone is rare (1/29) — most studies triangulate perspectives (caregivers+HCWs, or all three groups together) rather than isolating the PLWD viewpoint.
- **Dependencies**: C01
- **Sources**:
  - HCWs only n=9 ← paper.pdf §Results "the focus of most studies was on HCWs (n = 9) [43–45, 47, 51, 53, 61, 62, 67]" [result]
  - PLWD only n=1 ← paper.pdf §Results "others concentrated solely on people living with dementia (n = 1) [52]" [result]
  - caregivers only n=5 ← paper.pdf §Results "and on caregivers (n = 5) [41, 54, 56, 63, 64]" [result]
  - caregivers+HCWs n=6 ← paper.pdf §Results "Both caregivers and HCWs participated in six studies [42, 49, 50, 57–59]." [result]
  - PLWD+caregivers n=5 ← paper.pdf §Results "Some studies (n = 5) included both people living with dementia and caregivers [39, 40, 48, 55, 60]." [result]
  - PLWD+caregivers+HCWs n=3 ← paper.pdf §Results "several studies (n = 3) included people living with dementia, caregivers, and HCWs [46, 65, 66]." [result]
- **Tags**: study-characteristics, population-focus, stakeholder-groups

## C09: Included studies covered a range of care settings, individually and combined
- **Statement**: Across the 29 studies, the single-setting focus was: home-based care (n=11), primary care (n=2), clinical or hospital-based care (n=3), residential or long-term care facilities (n=3), and community-based care (n=2); multi-setting studies combined home-based + community-based care (n=1), home-based + respite care (n=3), home-based + residential/long-term + community-based care (n=3), and home-based + respite + clinical/hospital-based care (n=1).
- **Status**: supported
- **Falsification criteria**: Disproved if these setting counts do not sum to 29 or differ from the text.
- **Proof**: [E04]
- **Evidence basis**: §Results "Study characteristics" enumerates settings explicitly; 11+2+3+3+2+1+3+3+1=29.
- **Interpretation**: Home-based care is both the most common single-setting focus (11/29) and a component of every listed multi-setting combination (8/29 additional studies), indicating that home-based dementia care is the dominant venue examined in the European barriers literature.
- **Dependencies**: C01
- **Sources**:
  - single-setting counts (home-based n=11, primary care n=2, clinical/hospital n=3, residential/LTC n=3, community-based n=2) ← paper.pdf §Results "The majority of studies (n = 11) focused on home-based care [39, 41, 44, 50, 53–56, 60, 63, 64], primary care (n = 2) [62, 66], clinical or hospital-based care (n = 3) [47, 51, 65], residential or long-term care facilities (n = 3) [43, 45, 61], and community-based care (n = 2) [52, 57]." [result]
  - multi-setting combination counts ← paper.pdf §Results "there were studies that combined home-based care with community-based care (n = 1) [48], while others combined home-based care with respite care (n = 3) [46, 58, 59]. Additionally, some studies (n = 3) examined a combination of home-based care, residential or long-term care facilities, and community-based care [40, 42, 67], whereas one study investigated a mix of home-based care, respite care, and clinical or hospital-based care (n = 1) [49]." [result]
- **Tags**: study-characteristics, care-setting

## C10: Minority and migrant populations face distinct, additional cultural/communication barriers
- **Statement**: In the UK, Sikh caregivers struggle with community and cultural norms that hinder access to health and social care services. HCWs in England encounter difficulties understanding the cultural and religious values of Bangladeshi communities. In Denmark, HCWs working with minorities from the Middle East (particularly Turkey and Iran), Eastern Europe (mainly the former Yugoslavia and Poland), and Pakistan report communication difficulties, strong cultural norms, and stigma within these groups. A similar situation is present in Norway for minority groups such as Somalis, Pakistanis, Turks, Poles, Croatians, and Indians.
- **Status**: supported
- **Falsification criteria**: Disproved if the named minority groups/countries do not match the cited studies, or if the review did not report communication/cultural-norm barriers for these groups.
- **Proof**: [E03]
- **Evidence basis**: §Discussion "Cultural and stigma-related barriers" reports each minority-specific finding with its source citation.
- **Interpretation**: Minority-specific barriers compound the general cultural/stigma-related barrier domain (C04, n=10) with additional dimensions — language, unfamiliarity with the host country's care system, and culturally-specific stigma — that generic (non-ethnicity-stratified) studies do not capture, and which most of the 29 studies do not report on at all (per the acknowledged limitation that "most studies did not specify the race and ethnicity of the participants").
- **Dependencies**: C04
- **Sources**:
  - Sikh caregivers in the UK ← paper.pdf §Discussion "In the UK, Sikh caregivers struggle with community and cultural norms that hinder access to health and social care services [41]." [result]
  - Bangladeshi communities in England ← paper.pdf §Discussion "HCWs encounter difficulties in understanding the cultural and religious values of Bangladeshi communities [54]." [result]
  - Denmark minorities (Middle East/Turkey/Iran, Eastern Europe/former Yugoslavia/Poland, Pakistan) ← paper.pdf §Discussion "In Denmark, HCWs working with minorities from the Middle East (particularly Turkey and Iran), Eastern Europe (mainly the former Yugoslavia and Poland), and Pakistan minorities report communication difficulties, strong cultural norms, and stigma within these groups [53]" [result]
  - Norway minorities (Somalis, Pakistanis, Turks, Poles, Croatians, Indians) ← paper.pdf §Discussion "A similar situation is present in Norway for minority groups such as Somalis, Pakistanis, Turks, Poles, Croatians, and Indians [50]." [result]
  - ethnicity-reporting limitation ← paper.pdf §Discussion "Strengths and limitations" "most studies did not specify the race and ethnicity of the participants, limiting the understanding of barriers across different racial and ethnic groups. Nonetheless, some studies did investigate the specific barriers faced by ethnic minorities" [result]
- **Tags**: minority-populations, migration, cultural-barriers, stigma
