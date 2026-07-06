# Claims

> Grounding: abstract-only. Every load-bearing number is copied verbatim from the provided abstract (`metadata.md`, line 13). Source references quote the abstract text and are tagged `[result]` because they report review findings. No full text, tables, figures, or model-level evidence files were available.

## C01: The review maps a large AD digital-biomarker literature and an AI-model subset
- **Statement**: The review conducts a bibliometric analysis of 431 studies from five online databases and a scoping review of 86 artificial intelligence models.
- **Status**: supported
- **Falsification criteria**: Access to the full review showing a different bibliometric corpus size, a different number of databases, or a different AI-model count than the abstract reports.
- **Proof**: [E01, E02]
- **Evidence basis**: The abstract states the bibliometric corpus size, database count, named databases, and AI-model count directly.
- **Interpretation**: The paper is both a bibliometric landscape analysis and an AI-model scoping review.
- **Sources**:
  - 431 studies, five online databases, 86 AI models <- metadata.md:13 «This review conducts a bibliometric analysis of 431 studies from five online databases: Web of Science, PubMed, Embase, IEEE Xplore, and CINAHL, and provides a scoping review of 86 artificial intelligence (AI) models.» [result]
- **Dependencies**: none
- **Tags**: bibliometrics, scoping-review, AI-models

## C02: AD digital-biomarker research is multidisciplinary and internationally distributed
- **Statement**: Research in this field is supported by 224 grants across 54 disciplines and 1403 institutions in 44 countries, with 2571 contributing researchers.
- **Status**: supported
- **Falsification criteria**: Full-text bibliometric tables or reproducible bibliometric data showing that any of these counts differ materially from the abstract.
- **Proof**: [E01]
- **Evidence basis**: The abstract reports the grant, discipline, institution, country, and researcher counts.
- **Interpretation**: The field is broad across funding, disciplinary, organizational, geographic, and personnel dimensions.
- **Sources**:
  - 224 grants, 54 disciplines, 1403 institutions, 44 countries, 2571 researchers <- metadata.md:13 «Research in this field is supported by 224 grants across 54 disciplines and 1403 institutions in 44 countries, with 2571 contributing researchers.» [result]
- **Dependencies**: C01
- **Tags**: bibliometrics, research-landscape, interdisciplinarity

## C03: Four digital-biomarker focus areas are emphasized
- **Statement**: The abstract identifies motor activity, neurocognitive tests, eye tracking, and speech analysis as key focus areas.
- **Status**: supported
- **Falsification criteria**: Full-text taxonomy showing these are not key focus areas or that the abstract's focus-area summary is inconsistent with the underlying study classification.
- **Proof**: [E03]
- **Evidence basis**: The abstract names these four focus areas directly.
- **Interpretation**: The review frames AD digital biomarkers around measurable behavioral, cognitive, ocular, and speech-derived signals.
- **Sources**:
  - four focus areas <- metadata.md:13 «Key focuses include motor activity, neurocognitive tests, eye tracking, and speech analysis.» [result]
- **Dependencies**: C01
- **Tags**: digital-biomarkers, motor-activity, neurocognitive-tests, eye-tracking, speech-analysis

## C04: Classical machine learning dominates, but performance reporting is incomplete
- **Statement**: Classical machine learning models dominate AI research in the reviewed literature, though many lack performance reporting.
- **Status**: supported
- **Falsification criteria**: Full model inventory showing that classical machine learning is not the dominant model family, or that most models include complete performance reporting.
- **Proof**: [E04]
- **Evidence basis**: The abstract states both the dominance of classical machine learning and the lack of performance reporting for many models.
- **Interpretation**: The AI-model literature may be less mature for comparison and translation than the model count alone suggests.
- **Sources**:
  - classical machine learning dominance and missing performance reporting <- metadata.md:13 «Classical machine learning models dominate AI research, though many lack performance reporting.» [result]
- **Dependencies**: C01
- **Tags**: machine-learning, reporting-quality, model-transparency

## C05: Reported AUC summaries are promising but validation and calibration are rare
- **Statement**: Among scoped models, 21 AD-focused models have average AUC 0.887, 45 mild-cognitive-impairment models have average AUC 0.821, only 2 studies incorporated external validation, and 3 studies performed model calibration.
- **Status**: supported
- **Falsification criteria**: Full-text model tables or extracted model data showing different model counts, AUC averages, external-validation count, or calibration count than the abstract reports.
- **Proof**: [E04, E05]
- **Evidence basis**: The abstract reports the AD-focused and MCI model counts with average AUCs, then reports external-validation and calibration counts.
- **Interpretation**: Discrimination metrics appear promising at the abstract level, but clinical integration is limited by sparse validation and calibration.
- **Sources**:
  - 21 AD-focused models, average AUC 0.887, 45 MCI models, average AUC 0.821 <- metadata.md:13 «Of 21 AD-focused models, the average AUC is 0.887, while 45 models for mild cognitive impairment show an average AUC of 0.821.» [result]
  - only 2 external validation studies and 3 calibration studies <- metadata.md:13 «Notably, only 2 studies incorporated external validation, and 3 studies performed model calibration.» [result]
- **Dependencies**: C01, C04
- **Tags**: AUC, Alzheimer's-disease, mild-cognitive-impairment, external-validation, calibration
