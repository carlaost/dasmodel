# Environment

Reproducibility facts for the **oshima/api** implementation artifact. Every version below is
grounded in `oshima/api/pyproject.toml` (project dependencies) unless noted otherwise.

- **Language/runtime**: Python `>=3.11` (`pyproject.toml` `requires-python = ">=3.11"`;
  classifiers list 3.11 and 3.12). Repo pins a local interpreter via `.python-version`.
- **Package/build manager**: `uv` (ultra-fast installer, per README) with `hatchling` build
  backend (`pyproject.toml` `[build-system]`). Lockfile: `uv.lock`.
- **Web framework**: FastAPI `>=0.104.0` served by `uvicorn[standard] >=0.24.0` (ASGI).
  Application factory in `app/main.py`; API v1 router in `app/api/v1/api.py`.

## Key dependencies (versions from `pyproject.toml`)

| Dependency | Version constraint | Role in the system |
|------------|--------------------|--------------------|
| `fastapi` | `>=0.104.0` | HTTP API framework |
| `uvicorn[standard]` | `>=0.24.0` | ASGI server |
| `pydantic[email]` | `>=2.5.0` | Schemas / validation (Pydantic v2) |
| `pydantic-settings` | `>=2.1.0` | Typed settings (`app/core/config.py`) |
| `supabase` | `>=2.10.0` | Postgres-backed storage, auth (JWT/RLS), RPC, object storage |
| `openai` | `>=1.101.0` | LLM claim/evidence extraction (default model `gpt-5-mini-2025-08-07`) |
| `anthropic` | `>=0.68.0` | Claude models (DSPy backend: `anthropic/claude-sonnet-4-5-20250929` in `main.py`) |
| `dspy` | `>=3.0.3` | Structured LLM extraction signatures (claims/evidence/themes) |
| `pdfservices-sdk` | `>=4.2.0` | Adobe PDF Services — PDF → structured JSON ingest |
| `pycorenlp` | `>=0.3.0` | Stanford CoreNLP client (NLP2FOL parsing) |
| `nltk` | `>=3.9.1` | WordNet / NLP support for SUMO ontology linking |
| `scikit-learn` | `>=1.3.0` | Embedding / clustering for theme consolidation |
| `umap-learn` | `>=0.5.0` | Dimensionality reduction for theme embeddings |
| `numpy` | `>=1.24.0` | Numerics |
| `pandas` | `>=2.0.0` | Tabular processing |
| `rapidfuzz` | `>=3.13.0` | Fuzzy matching (dedup / attribution) |
| `httpx` | `>=0.25.0` | Async HTTP client |
| `aiohttp` | `>=3.12.15` | Async HTTP (parallel LLM/CoreNLP calls) |
| `structlog` | `>=23.2.0` + `rich >=13.7.0` | Structured JSON logging |
| `python-jose[cryptography]` | `>=3.3.0`, `passlib[bcrypt]` `>=1.7.4` | JWT / auth helpers |
| `beautifulsoup4` `>=4.14.2`, `selenium` `>=4.36.0` | metadata / peripheral web search |
| `plotly`/`matplotlib`/`seaborn` | `>=5.0`/`>=3.7`/`>=0.12` | visualization of themes |

Optional extras (`pyproject.toml [project.optional-dependencies]`): `dev` (pytest `>=7.4.0`,
pytest-asyncio, pytest-cov, black, isort, flake8 `>=6.1.0`, mypy `>=1.7.0`, pre-commit),
`db` (sqlalchemy/alembic/asyncpg — currently unused; runtime persistence is Supabase),
`redis`, `monitoring` (prometheus + opentelemetry).

## How to run (from `README.md`)

```bash
cd api
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
cp .env.example .env            # then set secrets (Supabase, OpenAI, Adobe, ...)
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
# or: python -m app.main
```
Health check: `GET /health`. Interactive docs at `/docs` and `/redoc` (only when `DEBUG=true`).
Live deployment runs on Hetzner (see `README_Hetzner_API.md`); production also fronted by
`*.oshimascience.com` (TrustedHost in `app/main.py`, CORS origins in `app/core/config.py`).

## Data sources

- **Input**: user-uploaded PDF research papers (multipart upload at `POST /api/v1/papers/`,
  `app/api/v1/endpoints/papers.py`). Max 40 MB (`papers_service.py` `MAX_FILE_SIZE`,
  `config.py` `MAX_FILE_SIZE = 41943040`). PDFs stored in Supabase Storage bucket
  `pdf-papers` (`papers_service.py` `STORAGE_BUCKET`).
- **Persistence**: Supabase Postgres tables — `papers`, `extraction_runs`, `extracts`
  (claims/evidence), `libraries`, `library_papers`, `library_themes` — plus stored procedures
  invoked via `supabase.rpc(...)` (`app/services/jobs/job_service.py`). Access control via
  Supabase JWT + Row Level Security; service-role client bypasses RLS for background workers
  (`app/db/supabase_client.py`).
- **External knowledge**: SUMO ontology + WordNet (NLTK) for NLP2FOL typing; OpenAlex client
  (`app/services/search/openalex_client.py`) for paper metadata enrichment.

## Configuration / env (from `.env.example` + `app/core/config.py`)

Required for full operation:
- `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY` (service-role needed for
  background workers — `supabase_client.py` raises if missing).
- `OPENAI_API_KEY` (claim/evidence extraction); `ANTHROPIC` key via env when `USE_DSPY_EXTRACTION=true`.
- Adobe PDF Services: `PDF_SERVICES_CLIENT_ID`, `PDF_SERVICES_CLIENT_SECRET`,
  `PDF_SERVICES_ORGANIZATION_ID` (or `INGEST_PROVIDER=azure` with `AZURE_DOCINTEL_ENDPOINT`/`_KEY`).
- `SECRET_KEY`, `ALGORITHM=HS256`, `ACCESS_TOKEN_EXPIRE_MINUTES=30` (JWT).
- Workers: `WORKER_ENABLED=true`, `WORKER_COUNT=4`, `LLM_RPS=1.0`, `JOB_POLL_SEC=5`,
  `JOB_CLAIM_TTL_SEC=600`, `MAX_JOB_RETRY_ATTEMPTS=3` (`config.py`).
- CoreNLP: `CORENLP_URLS` (default `http://localhost:9000`), `CORENLP_MAX_CONCURRENCY=3`.

## Hardware

- **n/a (service/CPU)** — no GPU required by the app itself; heavy compute is delegated to
  external APIs (OpenAI/Anthropic LLMs, Adobe/Azure document intelligence) and a CoreNLP server.
  Background processing uses a `ThreadPoolExecutor` worker pool (`app/workers/worker_manager.py`).

## Protocols / seeds

- No fixed random seed is configured in the captured source. Pipeline determinism is bounded by
  LLM stochasticity; structured outputs are constrained via Pydantic/DSPy schemas
  (`app/models/extract.py`).
