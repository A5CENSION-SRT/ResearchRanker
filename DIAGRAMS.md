# ResearchRanker Diagram Specification Library

This document serves as the master specification repository for all architectural, sequence, workflow, and relational diagrams supporting the **ResearchRanker** platform. Pre-rendered high-resolution PNG figures generated from these sources are embedded in [README.md](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/README.md).

---

## Table of Contents

1. [High-Level System Architecture](#1-high-level-system-architecture)
2. [End-to-End System Sequence Flow](#2-end-to-end-system-sequence-flow)
3. [Multi-Agent Analysis Pipeline Stages](#3-multi-agent-analysis-pipeline-stages)
4. [Relational Database ER Schema](#4-relational-database-er-schema)
5. [Automated Data Ingestion & Plagiarism Pipeline](#5-automated-data-ingestion--plagiarism-pipeline)

---

## 1. High-Level System Architecture

- **Source File**: [system_architecture.mmd](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/system_architecture.mmd)
- **Rendered Figure**: [system_architecture.png](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/system_architecture.png)

```mermaid
graph TB
    %% Nodes
    subgraph ClientTier ["Client & Web Tier"]
        UI["Web Browser User Interface<br/>(Jinja2 HTML5 / Bootstrap 5 / Vanilla CSS)"]
        AUTH["Authentication Controller<br/>(Google OAuth2 / Flask Session)"]
    end

    subgraph ApplicationTier ["Application Server Layer (Flask App)"]
        APP["Flask Application Engine<br/>(app.py - Routing & Context)"]
        FORM["Input Validator & Forms<br/>(WTForms / Werkzeug)"]
        READER["PDF Extractor Module<br/>(PyMuPDF / pdfplumber)"]
        COMPARE["Comparative Analyzer Module<br/>(utils/comparison.py)"]
        GRAMMAR["Grammar Diagnostic Engine<br/>(utils/grammar.py / LanguageTool)"]
        PLAG["Plagiarism Engine<br/>(utils/plagiarism_detector.py)"]
    end

    subgraph IntelligentServices ["Intelligent AI & External Services"]
        OLLAMA["Local LLM Inference Engine<br/>(Ollama: Gemma3 / Phi4 / DeepSeek R1)"]
        CORE["CORE AC API Service<br/>(v3 REST Endpoint)"]
        SBERT["S-BERT Vector Engine<br/>(all-MiniLM-L6-v2 Embeddings)"]
    end

    subgraph PersistenceTier ["Persistence & Data Store"]
        DB[("SQLite Database<br/>(Users.db - SQLAlchemy ORM)")]
        FS["Local Upload Directory<br/>(static/uploads)"]
    end

    %% Connections
    UI -->|HTTP Requests| APP
    APP --> AUTH
    AUTH -->|User Credentials / Tokens| DB
    APP --> FORM
    APP --> FS
    APP --> READER
    READER --> COMPARE
    READER --> GRAMMAR
    READER --> PLAG

    COMPARE -->|Ollama API Prompts| OLLAMA
    GRAMMAR -->|LanguageTool Rules & LLM| OLLAMA
    PLAG -->|Metadata Query| CORE
    PLAG -->|Vector Embeddings| SBERT
    OLLAMA -->|Analysis Output| APP
    SBERT -->|Similarity Score| APP
    APP -->|Rendered Response| UI

    %% Styling
    style UI fill:#dbeafe,stroke:#1e40af,stroke-width:2px
    style AUTH fill:#dbeafe,stroke:#1e40af,stroke-width:2px
    style APP fill:#f3e8ff,stroke:#6b21a8,stroke-width:2px
    style FORM fill:#f3e8ff,stroke:#6b21a8,stroke-width:2px
    style READER fill:#f3e8ff,stroke:#6b21a8,stroke-width:2px
    style COMPARE fill:#fef3c7,stroke:#b45309,stroke-width:2px
    style GRAMMAR fill:#fef3c7,stroke:#b45309,stroke-width:2px
    style PLAG fill:#fef3c7,stroke:#b45309,stroke-width:2px
    style OLLAMA fill:#dcfce7,stroke:#15803d,stroke-width:2px
    style CORE fill:#dcfce7,stroke:#15803d,stroke-width:2px
    style SBERT fill:#dcfce7,stroke:#15803d,stroke-width:2px
    style DB fill:#ffe4e6,stroke:#be123c,stroke-width:2px
    style FS fill:#ffe4e6,stroke:#be123c,stroke-width:2px
```

---

## 2. End-to-End System Sequence Flow

- **Source File**: [sequence_flow.mmd](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/sequence_flow.mmd)
- **Rendered Figure**: [sequence_flow.png](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/sequence_flow.png)

```mermaid
sequenceDiagram
    autonumber
    actor User as Researcher / Student
    participant UI as Flask Web Frontend
    participant App as Flask Controller (app.py)
    participant Reader as PDF Extractor (fitz)
    participant CORE as CORE AC API (v3)
    participant LLM as Ollama Engine (Phi4/Gemma3)
    participant SBERT as S-BERT Model (MiniLM)
    participant DB as SQLite Database

    User->>UI: Access ResearchRanker Portal
    UI->>App: GET /login or OAuth Callback
    App->>DB: Query User Record / Validate Session
    DB-->>App: Session Confirmed
    App-->>UI: Render User Workspace

    rect rgb(219, 234, 254)
        note right of User: Phase 1: Paper Comparison & Template Check
        User->>UI: Upload User & Reference PDFs
        UI->>App: POST /compare-papers (Multi-part upload)
        App->>Reader: Extract Text Streams (fitz.open)
        Reader-->>App: Raw Text Content
        App->>LLM: comparePDF(reference, user, aimodel)
        LLM-->>App: Structured Methodology Analysis
        App-->>UI: Render Comparison Results Page
    end

    rect rgb(254, 243, 199)
        note right of User: Phase 2: Plagiarism Detection & Corpus Search
        User->>UI: Upload Draft PDF for Plagiarism Audit
        UI->>App: POST /check-plagarism
        App->>LLM: extract_title(first_page_text)
        LLM-->>App: Candidate Paper Titles
        App->>CORE: coreAPICall(title, limit=15)
        CORE-->>App: Open Access PDF Downloads (URLs)
        App->>Reader: Download & Extract Reference PDF Bytes
        Reader-->>App: Aggregated Corpus Text
        App->>SBERT: compute_similarity(user_text, corpus_text)
        SBERT-->>App: Cosine Distance & Match Percentage
        App->>DB: Store Audit Log Result
        App-->>UI: Display Plagiarism Score & Report
    end
```

---

## 3. Multi-Agent Analysis Pipeline Stages

- **Source File**: [pipeline_stages.mmd](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/pipeline_stages.mmd)
- **Rendered Figure**: [pipeline_stages.png](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/pipeline_stages.png)

```mermaid
graph LR
    subgraph Stage1 ["Stage 1: Document Ingestion"]
        S1A["Upload PDF"] --> S1B["PyMuPDF Stream Parsing"]
        S1B --> S1C["Normalized Text Extraction"]
    end

    subgraph Stage2 ["Stage 2: Feature Fingerprinting"]
        S2A["Page Layout Extraction"] --> S2B["Section Hierarchy Match"]
        S2B --> S2C["Font & Margin Verification"]
    end

    subgraph Stage3 ["Stage 3: Multi-Agent Analysis"]
        S3A["Ollama LLM Prompts"] --> S3B["Methodology Comparison"]
        S3B --> S3C["Structural Scoring Algorithm"]
        S3C --> S3D["Grammar Diagnostic Engine"]
    end

    subgraph Stage4 ["Stage 4: Corpus Validation"]
        S4A["Title Generation"] --> S4B["CORE AC API Retrieval"]
        S4B --> S4C["S-BERT Vector Encoding"]
        S4C --> S4D["Cosine Similarity Matrix"]
    end

    Stage1 --> Stage2
    Stage2 --> Stage3
    Stage3 --> Stage4

    %% Styling
    style Stage1 fill:#dbeafe,stroke:#1e40af,stroke-width:2px
    style Stage2 fill:#f3e8ff,stroke:#6b21a8,stroke-width:2px
    style Stage3 fill:#fef3c7,stroke:#b45309,stroke-width:2px
    style Stage4 fill:#dcfce7,stroke:#15803d,stroke-width:2px
```

---

## 4. Relational Database ER Schema

- **Source File**: [er_schema.mmd](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/er_schema.mmd)
- **Rendered Figure**: [er_schema.png](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/er_schema.png)

```mermaid
erDiagram
    USER ||--o{ ANALYSIS_SESSION : initiates
    USER ||--o{ OAUTH_ACCOUNT : links
    ANALYSIS_SESSION ||--o{ PLAGIARISM_REPORT : generates
    ANALYSIS_SESSION ||--o{ COMPARISON_REPORT : generates

    USER {
        int id PK
        string username UK
        string email UK
        string password_hash
        datetime created_on
    }

    OAUTH_ACCOUNT {
        int id PK
        int user_id FK
        string provider
        string oauth_token
        string refresh_token
        datetime created_at
    }

    ANALYSIS_SESSION {
        string session_id PK
        int user_id FK
        string user_paper_name
        datetime timestamp
    }

    PLAGIARISM_REPORT {
        int id PK
        string session_id FK
        float similarity_score
        int corpus_count
        datetime executed_at
    }

    COMPARISON_REPORT {
        int id PK
        string session_id FK
        string target_paper_name
        string model_used
        text ai_analysis_text
    }
```

---

## 5. Automated Data Ingestion & Plagiarism Pipeline

- **Source File**: [data_ingestion.mmd](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/data_ingestion.mmd)
- **Rendered Figure**: [data_ingestion.png](file:///home/snehal-reddy/Coding/Repositories/ResearchRanker/docs/diagrams/data_ingestion.png)

```mermaid
graph TB
    subgraph Input ["Document Upload"]
        PDF["User Research PDF"]
    end

    subgraph Extraction ["Header & Text Extraction"]
        PAGE1["First Page Extractor<br/>(fitz.open stream)"]
        TITLE_GEN["Title Extractor Prompt<br/>(Ollama Gemma3:4b)"]
    end

    subgraph CorpusIngestion ["Corpus Ingestion Pipeline"]
        CORE_API["CORE AC Search API<br/>(q=Title, limit=15)"]
        FILTER["PDF URL Validator"]
        FETCH["Asynchronous Byte Fetcher"]
        AGGREGATE["Corpus Text Aggregator"]
    end

    subgraph VectorProcessing ["Semantic Similarity Pipeline"]
        TOKENIZE["Sentence Tokenizer<br/>(nltk sent_tokenize)"]
        SBERT_MODEL["SentenceTransformer<br/>(all-MiniLM-L6-v2)"]
        COSINE["Cosine Similarity Matrix<br/>(sklearn metrics)"]
        SCORE["Similarity Percentage"]
    end

    PDF --> PAGE1
    PAGE1 --> TITLE_GEN
    TITLE_GEN -->|Derived Titles| CORE_API
    CORE_API --> FILTER
    FILTER -->|PDF Links| FETCH
    FETCH --> AGGREGATE
    AGGREGATE --> TOKENIZE
    PDF --> TOKENIZE
    TOKENIZE --> SBERT_MODEL
    SBERT_MODEL --> COSINE
    COSINE --> SCORE

    %% Styling
    style Input fill:#dbeafe,stroke:#1e40af,stroke-width:2px
    style Extraction fill:#f3e8ff,stroke:#6b21a8,stroke-width:2px
    style CorpusIngestion fill:#fef3c7,stroke:#b45309,stroke-width:2px
    style VectorProcessing fill:#dcfce7,stroke:#15803d,stroke-width:2px
```
