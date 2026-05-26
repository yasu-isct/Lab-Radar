# Lab Radar

Lab Radar is a RAG-based academic advisor matching engine. It helps students find suitable research supervisors by matching a statement of purpose (SOP) against professor and laboratory research profiles.

The project is currently in Phase 0: repository initialization and architecture design.

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

- Backend: FastAPI, Pydantic
- Data collection: Scrapy, BeautifulSoup
- Embeddings: OpenAI embeddings or Sentence Transformers
- Vector database: Qdrant by default, ChromaDB as an alternative
- Reranking: Cohere Rerank or open-source cross-encoder models
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

## Current Phase 0 Tasks

- [x] Repository structure
- [x] Initial technology choices
- [x] Core Pydantic data models
- [x] FastAPI API skeleton
- [x] Environment configuration template
- [x] Basic CI workflow
- [ ] Production crawler implementation
- [ ] Embedding pipeline implementation
- [ ] Vector database deployment
- [ ] Reranker integration
- [ ] Frontend application
