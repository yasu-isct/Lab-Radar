# Lab-Radar
This is a scalable, multilingual RAG engine designed to bridge the gap between prospective students and research labs. Our initial proof-of-concept focuses on the highly unstandardized data of Japanese universities, with a modular architecture ready to expand globally.
# 🎓 ScholarMatch-AI 
**An open-source RAG engine bridging the information gap between prospective students and research labs.**
*(致力于打破学术信息差的开源 RAG 匹配引擎 / 学生と研究室の情報格差をなくすRAGマッチングエンジン)*

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Architecture](https://img.shields.io/badge/Architecture-RAG-success)

---

## 📖 Overview | 项目简介 | 概要

**[EN]** Applying to graduate schools often involves navigating highly unstandardized lab websites and scattered PDFs. **ScholarMatch-AI** uses Large Language Models (LLMs) and Vector Search to semantically match a student's Statement of Purpose (SOP) with the most relevant Principal Investigators (PIs), explaining *why* they are a good fit. 

**[ZH]** 申请海外大学院往往需要面对极其非标准化的教授主页和零散的文献资料。**ScholarMatch-AI** 利用大语言模型（LLM）和向量检索技术，将学生的《研究计划书》与最契合的导师（PI）进行深度语义匹配，并生成具有逻辑支撑的推荐理由，实现跨国学术的双向奔赴。

**[JA]** 大学院への進学において、非標準的な研究室HPやPDFから自分に合う指導教員を探すのは困難です。**ScholarMatch-AI** は、LLMとベクトル検索を活用し、学生の研究計画書と最も適した研究室を意味的にマッチングし、その推薦理由を論理的に提示するオープンソースツールです。

---

## 🏗️ Architecture & Features | 核心架构与功能 | システム構成

- **Semantic Embedding & Vector Search (语义检索):** Moving beyond keyword matching, we use advanced embedding models to understand the deep academic context of SOPs and research papers.
- **Reranking Pipeline (重排机制):** High-precision matching ensuring the top results are highly relevant to the student's niche.
- **LLM-Powered Insights (大模型分析):** Generates personalized, actionable advice for contacting the matched professors.
- **Scalable Data Pipeline (高扩展数据管道):** Built to handle messy, unstructured academic data (starting with a Proof-of-Concept for Japanese universities, scalable globally).

*(Note: Architecture diagram will be updated here soon.)*

---

## 🛠️ Tech Stack | 技术栈 | 技術スタック

- **AI & NLP:** OpenAI API (GPT-4o) / Open-source LLMs, Embedding Models, Reranker
- **Vector Database:** Qdrant / ChromaDB
- **Backend Framework:** FastAPI, Pydantic
- **Data Engineering:** Scrapy, BeautifulSoup, Pandas

---

## 🗺️ Roadmap | 演进路线 | ロードマップ

- [x] **Phase 0:** Project Initialization & Architecture Design
- [ ] **Phase 1 (MVP):** Proof of Concept focusing on top Japanese Universities (Handling highly unstandardized Japanese academic data).
- [ ] **Phase 2:** Integration of Reranking models and automated evaluation metrics (e.g., Ragas).
- [ ] **Phase 3:** Frontend deployment and global universities expansion.

---

## 🚀 Getting Started | 快速开始 | 使い方

*(Documentation for local setup, environment variables, and deployment will be available once the MVP is released.)*

```bash
# Clone the repo
git clone [https://github.com/YourOrganization/ScholarMatch-AI.git](https://github.com/YourOrganization/ScholarMatch-AI.git)

# Install dependencies
pip install -r requirements.txt
