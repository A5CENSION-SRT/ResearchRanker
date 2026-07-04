# ResearchRanker

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.2-000000?style=for-the-badge&logo=flask&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000?style=for-the-badge&logo=ollama&logoColor=white)
![SentenceTransformers](https://img.shields.io/badge/S--BERT-all--MiniLM--L6--v2-FF6F00?style=for-the-badge&logo=pytorch&logoColor=white)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-fitz-1B72BE?style=for-the-badge)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

**An enterprise-grade, local AI-powered platform for academic research discovery, paper structure comparison, grammatical refinement, and semantic plagiarism verification.**

---

## Table of Contents

- [Overview](#overview)
- [Key Architectural Features](#key-architectural-features)
- [System Architecture & Pipeline](#system-architecture--pipeline)
- [System Sequence Flow & ER Schema](#system-sequence-flow--er-schema)
- [Repository Layout](#repository-layout)
- [Prerequisites & Installation](#prerequisites--installation)
- [Configuration & Environment Setup](#configuration--environment-setup)
- [Running the Application](#running-the-application)
- [Verification & Unit Testing](#verification--unit-testing)
- [Additional Technical Documentation](#additional-technical-documentation)

---

## Overview

**ResearchRanker** is a full-stack Flask web platform engineered to empower researchers and students throughout the lifecycle of drafting, comparing, and validating scientific literature—with specialized support for IEEE formatting and open-access publication standards.

By unifying local open-weight Large Language Models (executed via Ollama) with dense vector sentence transformers (`all-MiniLM-L6-v2`) and live metadata querying through the CORE AC REST API, ResearchRanker delivers privacy-preserving, local AI assistance without data leakage or subscription API costs.

---

## Key Architectural Features

- **Methodological Paper Comparison**: Upload draft PDFs alongside reference IEEE publications to extract and compare research objectives, computational efficiency, and methodology novelty using local models (`Phi4` / `Gemma 3`).
- **Template Compliance Checker**: Evaluate document formatting, section nesting hierarchy, column alignment, font consistency, and margin compliance against target templates.
- **Semantic Plagiarism Engine**: Extract paper titles using LLMs, fetch matching open-access publications via the CORE AC API, and calculate pairwise sentence cosine similarity using S-BERT vector embeddings.
- **Grammar & Style Diagnostic Engine**: Analyze PDF text streams with LanguageTool and local LLMs to generate page-level error reports and actionable revision suggestions.
- **Privacy-First Local Execution**: All paper contents are processed strictly locally using Ollama inference endpoints and local PyTorch embedding models.

---

## System Architecture & Pipeline

### High-Level Multi-Tier Architecture

![System Architecture](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/system_architecture.png)
*Figure 1: Multi-Tier High-Level System Architecture. Source: [system_architecture.mmd](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/system_architecture.mmd). Master Specification: [DIAGRAMS.md](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/DIAGRAMS.md).*

### Multi-Agent Analysis Pipeline Stages

![Pipeline Stages](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/pipeline_stages.png)
*Figure 2: Multi-Stage PDF Ingestion and Multi-Agent Processing Pipeline. Source: [pipeline_stages.mmd](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/pipeline_stages.mmd). Master Specification: [DIAGRAMS.md](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/DIAGRAMS.md).*

---

## System Sequence Flow & ER Schema

### End-to-End Execution Sequence Flow

![Sequence Flow](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/sequence_flow.png)
*Figure 3: System Sequence Diagram detailing user interaction, PDF extraction, CORE API queries, and LLM inference. Source: [sequence_flow.mmd](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/sequence_flow.mmd). Master Specification: [DIAGRAMS.md](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/DIAGRAMS.md).*

### Relational Database ER Schema

![Database ER Schema](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/er_schema.png)
*Figure 4: Relational SQLite Entity-Relationship Diagram. Source: [er_schema.mmd](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/er_schema.mmd). Master Specification: [DIAGRAMS.md](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/DIAGRAMS.md).*

---

## Repository Layout

```
ResearchRanker/
├── app/
│   ├── app.py                      # Main Flask application & route controllers
│   ├── instance/
│   │   └── Users.db                # SQLite user database (SQLAlchemy ORM)
│   ├── static/                     # Static CSS, JavaScript, and asset uploads
│   │   ├── css/                    # Custom CSS stylesheets
│   │   ├── images/                 # Static branding & UI images
│   │   └── uploads/                # Temporary PDF upload directory
│   ├── templates/                  # Jinja2 HTML templates
│   │   ├── compare.html            # Paper comparison view template
│   │   ├── grammer-correct.html    # Grammar fix view template
│   │   ├── index.html              # Landing page & model selector
│   │   ├── layout.html             # Base layout template
│   │   ├── plagarism.html          # Plagiarism report template
│   │   ├── signup.html             # Auth login/signup template
│   │   ├── template-checker.html   # Template checker view template
│   │   └── tools.html              # Tools index view template
│   └── utils/                      # Core AI & processing engines
│       ├── comparison.py           # Ollama comparative analysis prompts
│       ├── grammar.py              # LanguageTool & LLM grammar engine
│       ├── pdf_reader.py           # PyMuPDF text stream extraction
│       └── plagiarism_detector.py # CORE API + S-BERT similarity matrix
├── docs/
│   └── diagrams/                   # Mermaid diagram sources (.mmd) & PNGs
│   └── scripts/                    # Asset generator scripts (.py)
├── tests/
│   ├── GSES_PV-efficiency.pdf      # Sample evaluation PDF
│   ├── Reference.pdf               # Reference sample paper
│   ├── Template.pdf                # Reference sample template
│   ├── User.pdf                    # User draft sample paper
│   └── test_basic.py               # Automated unit test suite
├── ARCHITECTURE.md                 # Deep-dive architecture reference
├── DIAGRAMS.md                     # Master Mermaid diagram specification
├── README.md                       # Repository primary manual
└── run.py                          # Application entry point
```

---

## Prerequisites & Installation

### Environment Prerequisites
- **Python**: 3.10 or higher
- **Ollama Engine**: Local installation of Ollama (with `gemma3:1b`, `gemma3:4b`, and `phi4` models pulled)
- **Node.js**: 18+ (required only if rendering Mermaid `.mmd` diagrams via `@mermaid-js/mermaid-cli`)

### 1. Clone Repository & Setup Virtual Environment

```bash
git clone https://github.com/yourusername/ResearchRanker.git
cd ResearchRanker

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Python Dependencies

```bash
pip install -r app/requirements.txt
```

### 3. Pull Required Local LLM Models

```bash
ollama pull gemma3:1b
ollama pull gemma3:4b
ollama pull phi4
```

---

## Configuration & Environment Setup

Create a `.env` file inside the `app/` directory:

```env
CLIENT_ID=your_google_oauth_client_id
CLIENT_SECRET=your_google_oauth_client_secret
SECRET_KEY=25354b506e275410240b8376094ff9bd
```

---

## Running the Application

Launch the application using the entry point script:

```bash
python3 run.py
```

Access the web interface by navigating to [http://localhost:5001](http://localhost:5001) in your browser.

---

## Verification & Unit Testing

Execute the automated test suite to verify application routing and database initialization:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

---

## Additional Technical Documentation

For in-depth technical references and architectural specifications:

- [ARCHITECTURE.md](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/ARCHITECTURE.md) - Subsystem interactions, function specifications, async/sync pipelines, and latency tables.
- [DIAGRAMS.md](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/DIAGRAMS.md) - Master library containing raw Mermaid diagram source code.
