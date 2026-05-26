# Lab-Radar

Lab-Radar is a scalable RAG-based academic advisor matching engine. It helps prospective students match a statement of purpose (SOP) with relevant professors, laboratories, and research groups.

The initial proof of concept focuses on Japanese university data, where professor pages, laboratory websites, and PDF publications are often highly unstandardized. The architecture is modular so the data pipeline can later expand to other regions and languages.

## Current Status

The repository is in Phase 0: project initialization and architecture design.

This scaffold provides:

- FastAPI application entry point
- Pydantic schemas for professors, SOP documents, and match results
- Placeholder recommendation API boundary
- Environment variable template
- CI workflow for linting and tests
- Initial directories for crawler, embedding, and frontend work

## Workflow

1. Data ingestion and preprocessing
   - Crawl university lab websites, professor pages, and academic PDFs.
   - Extract structured professor profiles, research areas, publications, and contact metadata.
   - Clean and normalize Japanese academic text.
   - Split long documents into retrieval-ready chunks.

2. Embedding and indexing
   - Convert chunks into embeddings.
   - Store dense vectors and metadata in a vector database.
   - Prepare for hybrid retrieval with dense search and BM25.

3. Semantic matching and reranking
   - Embed the student SOP.
   - Retrieve top professor candidates.
   - Rerank candidates with a cross-encoder or reranking API.
   - Filter low-confidence matches.

4. Recommendation generation and frontend display
   - Generate personalized recommendation reasons with an LLM.
   - Explain research-field, method, and background matches.
   - Present ranked professors and contact suggestions in a web UI.

## Repository Layout

```text
backend/
  app/
    api/          FastAPI routers and request handlers
    core/         settings and shared configuration
    models/       Pydantic schemas for professors, SOPs, and matches
    services/     matching and recommendation service boundaries
crawler/          future crawlers and ingestion utilities
embedding/        future chunking, embedding, and vector indexing pipelines
frontend/         future student-facing web interface
tests/            backend tests
```

## Tech Stack

- AI and NLP: OpenAI API or open-source LLMs
- Embeddings: OpenAI embeddings or Sentence Transformers
- Vector database: Qdrant by default, ChromaDB as an alternative
- Reranking: Cohere Rerank or open-source cross-encoder models
- Backend: FastAPI, Pydantic
- Data engineering: Scrapy, BeautifulSoup, Pandas
- Evaluation: Ragas and custom matching metrics
- Deployment: Docker and Docker Compose in later phases

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs`.

## Configuration

Copy `.env.example` to `.env` and fill in provider credentials before connecting live services.

## Validation

```powershell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m pytest
```

## Roadmap

- [x] Phase 0: Project initialization and architecture design
- [ ] Phase 1: Japanese university MVP data ingestion and basic retrieval
- [ ] Phase 2: Reranking, hybrid retrieval, and automated RAG evaluation
- [ ] Phase 3: Frontend deployment, authentication, feedback, and global expansion
