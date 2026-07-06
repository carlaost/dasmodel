# Artifacts — oshima/api

The deliverable is a **running FastAPI backend** ("Oshima API") that ingests scientific papers
(PDFs) and turns them into a structured, queryable knowledge representation: per-paper **claims**
and **evidence** (typed support/contradict/contextual links), first-order-logic (FOL)
representations of those statements, and library-level **themes**. This is the concrete
implementation artifact behind the desciencemodel research project's agent-native scientific
knowledge representation. The real runnable source is captured under `src/execution/app/...`
(`# Grounding: transcribed`); the blocks below describe it as a system and point at verified files.

## Oshima API service (FastAPI application)
- **File(s) in repo**: `app/main.py` (app factory, lifespan, CORS/TrustedHost, `/`, `/health`),
  `app/api/v1/api.py` (router wiring), `app/core/config.py` (Pydantic settings).
- **Nature**: HTTP API / system.
- **What it does / contains**: Mounts all v1 routers under `/api/v1`; on startup optionally
  configures DSPy with Claude Sonnet 4.5, starts the background job worker pool, and starts the
  theme-extraction monitor. CORS allows the oshima frontends and `*.oshimascience.com`.
- **How to use / run**: `uv run uvicorn app.main:app --host 0.0.0.0 --port 8000`; docs at `/docs`.
- **Claims supported**: C01, C06.

## Paper ingestion endpoint
- **File(s) in repo**: `app/api/v1/endpoints/papers.py`, `app/services/papers_service.py`,
  `app/services/ingest/ingest_pdf.py`, `app/services/storage/storage_client.py`.
- **Nature**: REST endpoints + service layer.
- **What it does / contains**: `POST /api/v1/papers/` accepts a multipart PDF (≤40 MB) plus
  optional `title`/`doi`/`field`/`topic`; validates MIME, computes SHA256, upserts the paper
  idempotently by hash, uploads the PDF to the Supabase `pdf-papers` bucket, and creates an
  `extraction_runs` row with `status='queued'`. `GET /api/v1/papers/` lists the user's papers;
  `GET /api/v1/papers/{paper_id}` returns metadata + storage refs + processing status.
- **How to use / run**: authenticated with a Supabase JWT Bearer token (RLS enforced).
- **Claims supported**: C01, C02.

## Six-stage extraction pipeline (background workers)
- **File(s) in repo**: `app/workers/worker_manager.py` (parallel worker pool + DB job claiming),
  `app/services/jobs/job_service.py` (DB-only job/library/artifact ops via Supabase RPC),
  `app/services/pipeline/storage_pipeline.py` (the 6-stage orchestrator).
- **Nature**: asynchronous processing system.
- **What it does / contains**: A `ThreadPoolExecutor`-backed worker pool atomically claims queued
  `extraction_runs` and runs each paper through, per `storage_pipeline.py` docstring:
  (1) **Ingest** PDF → structured JSON (Adobe PDF Services, or Azure),
  (2) **Extract** claims & evidence via LLM,
  (3) **Attribution** linking statements to source locations,
  (4) **NLP2FOL** conversion to first-order logic,
  (5) **Deduplication** of logical duplicates,
  (6) **Consolidation** into a single final output. Stage status is tracked in DB manifests.
- **How to use / run**: starts automatically with the app (`WORKER_ENABLED=true`, `WORKER_COUNT=4`).
- **Claims supported**: C02, C03, C04, C05.

## Claim & evidence extraction
- **File(s) in repo**: `app/services/extract/extract_paper.py` (`PaperExtractor`),
  `app/services/extract/dspy_claims_extractor.py`, `app/models/extract.py` (schemas),
  `app/services/extract/build_prompt.py`, `app/services/extract/prompts/v5/`.
- **Nature**: LLM extraction module.
- **What it does / contains**: Chunks long papers with section-aware splitting, extracts
  **claims** (original authorial assertions, with confidence + centrality) and **evidence**
  (typed `support`/`contradict`/`contextual` per claim) using either OpenAI structured outputs
  (`gpt-5-mini-2025-08-07`, Pydantic `Claims`/`EvidenceList`) or DSPy signatures
  (`ClaimCore`/`ExtractClaims`), then bulk-writes claim/evidence rows + relationships to the DB.
- **How to use / run**: invoked by the pipeline; also runnable as a CLI (`extract_paper.py --type ...`).
- **Claims supported**: C03.

## NLP-to-FOL logical representation
- **File(s) in repo**: `app/services/nlp2fol/complete_pipeline_processor.py`,
  `app/services/nlp2fol/logic_mapper.py`, plus `parser.py`, `splitter.py`, `composer.py`,
  `triple_wrapper.py`, `variable_binder.py`, `logic_feature_detector.py`, and the SUMO ontology
  stages `app/services/nlp2fol/ontologies/sumo/s0_resources.py` … `s6_typing_hints.py`.
- **Nature**: symbolic NLP processing pipeline.
- **What it does / contains**: Converts natural-language claims/evidence into first-order-logic
  ASTs: CoreNLP triple extraction → neutral operator/quantifier/implication cue detection →
  domain-agnostic "logic plan" (`logic_mapper.py`: NEG/AND/OR/XOR/implication ops) → SUMO+WordNet
  entity typing → composed FOL formula. `fol_json` is then stored on each extract row.
- **How to use / run**: stage 4 of the pipeline (`CompletePipelineProcessor.process_claims_and_evidence`).
- **Claims supported**: C04.

## Libraries, collections & cross-paper themes
- **File(s) in repo**: `app/api/v1/endpoints/library_papers.py`,
  `app/api/v1/endpoints/libraries/collections_new.py`, `app/api/v1/endpoints/libraries_crud.py`,
  `app/api/v1/endpoints/themes.py`, `app/services/themes/theme_service.py`,
  `app/services/themes/theme_monitor.py`, `app/services/extract/dspy_themes_extractor.py`.
- **Nature**: organization + cross-document synthesis layer.
- **What it does / contains**: Libraries group papers (many-to-many via `library_papers`).
  A theme monitor watches libraries and runs DSPy theme extraction over all claims in a library
  (full extraction or incremental update when papers are added/removed), persisting versioned
  `library_themes`. `GET /api/v1/libraries/{id}/themes` serves them read-only.
- **Claims supported**: C05.

## Persistence & access control
- **File(s) in repo**: `app/db/supabase_client.py`, `app/db/queries/extracts.py`,
  `app/db/queries/papers.py`, `app/db/queries/libraries.py`, `app/models/db_models.py`.
- **Nature**: data-access layer.
- **What it does / contains**: Two Supabase client factories — `user_client(jwt)` (per-request,
  RLS-enforced) and a cached service-role `service_client()` (RLS-bypass, for workers).
  `extracts.py` provides `bulk_insert_with_relationships` for batch claim/evidence writes with
  claim↔evidence relationship creation. `db_models.py` defines `Paper`, `ExtractIn`, bounding-box
  / text-span source-location models.
- **Claims supported**: C01, C02, C06.

## Supporting artifacts (described, not all captured)
- `app/api/v1/endpoints/jobs_new.py`, `app/api/v1/endpoints/storage.py`,
  `app/api/v1/endpoints/artifacts/` — job status/management, signed-URL storage access, artifact
  download/final-output endpoints.
- `mechanisms_library.json`, `subtheme_embeddings.json` (repo root) — precomputed knowledge/embedding
  artifacts; `llm_playground/` — DSPy optimization experiments (out of scope for the running API).
