Thank you for the correction—that is a substantive one. You are right: in the prior responses I **described components and roles**, but I did **not explicitly delineate two distinct architectures**. Below I will do that plainly and rigorously, and then provide the **requested consolidated list of pipelines, RAG technologies, and servers**, explicitly aligned to your purpose.

I will proceed in **four clearly separated sections**, per your instruction style.

---

# I. Clear, Direct Answer

There are **two architectures**, not one:

1. **Architecture A – Research Ingestion & Retrieval Architecture**  
   Purpose: *Normalize, parse, index, and retrieve evidence from mixed‑format documents.*

2. **Architecture B – Extractive Analytical Synthesis Architecture**  
   Purpose: *Assemble verbatim, citation‑safe, non‑narrative syntheses using exact wording from the corpus.*

They are **logically, operationally, and methodologically distinct**, even if they share infrastructure.

---

# II. Architecture A: Research Ingestion & Retrieval Architecture  
(*Evidence Preparation Architecture*)

## Purpose
To convert heterogeneous source documents into **canonical Markdown**, structurally parse them, embed them, and support high‑precision retrieval.

This architecture **never synthesizes text**.

---

## A.1 Functional Responsibilities

- Accept mixed document formats
- Convert all documents to Markdown
- Preserve semantic and structural integrity
- Chunk documents with traceable metadata
- Embed and index content
- Return ranked passages for analysis

---

## A.2 Architectural Flow

```
┌────────────────────────────────────┐
│ Source Files                        │
│ PDF | DOCX | HTML | TXT | MD        │
└───────────────┬────────────────────┘
                │
      [Document Normalization Pipeline]
                │
┌───────────────▼────────────────────┐
│ Canonical Markdown Repository       │
└───────────────┬────────────────────┘
                │
      [AST Parsing & Semantic Chunking]
                │
┌───────────────▼────────────────────┐
│ Chunk Store (with deep metadata)    │
└───────────────┬────────────────────┘
                │
      [Embedding & Indexing Pipeline]
                │
┌───────────────▼────────────────────┐
│ Vector Database                     │
└───────────────┬────────────────────┘
                │
        [Retrieval API]
```

---

## A.3 Server Model (Architecture A)

**Primary Server**: **Uvicorn**
- Reason: high‑throughput async ingestion and retrieval
- Role: infrastructure‑level data service

This is **not exposed to end‑user synthesis requests**.

---

# III. Architecture B: Extractive Analytical Synthesis Architecture  
(*Evidence Assembly Architecture*)

## Purpose
To produce **analytic outputs composed exclusively of exact wording** from retrieved passages, organized by topic and query—without narration, paraphrase, or interpretation.

This architecture **never embeds or ingests files**.

---

## B.1 Functional Responsibilities

- Accept research queries
- Call Architecture A for retrieval
- Rank and filter candidate passages
- Assemble verbatim excerpts
- Enforce exact‑wording constraints
- Return citation‑anchored synthesis outputs

---

## B.2 Architectural Flow

```
┌───────────────────────────┐
│ Query / Analytic Prompt   │
└───────────────┬───────────┘
                │
        [Retrieval Call]
                │
┌───────────────▼───────────┐
│ Ranked Passage Set        │
└───────────────┬───────────┘
                │
    [Extractive Selection Engine]
                │
┌───────────────▼───────────┐
│ Verbatim Passage Assembly │
└───────────────┬───────────┘
                │
    [Exact‑Wording Validator]
                │
┌───────────────▼───────────┐
│ Citation‑Anchored Output  │
└───────────────────────────┘
```

---

## B.3 Server Model (Architecture B)

**Primary Server**: **Hypercorn**
- Reason:
  - HTTP/2 support for long analytical payloads
  - Better handling of controlled generation
  - Secure, stable synthesis endpoint

This server is **methodological**, not infrastructural.

---

# IV. Consolidated Lists (As Requested)

Below is a **clean, explicit inventory**, grouped exactly as you requested.

---

## 1. Pipelines (By Function)

### Ingestion & Normalization Pipelines
- Format detection pipeline
- Document → Markdown conversion pipeline
- Canonical Markdown validation pipeline

### Parsing & Structuring Pipelines
- Markdown AST parsing pipeline
- Semantic chunking pipeline
- Metadata enrichment pipeline

### Retrieval Pipelines
- Embedding generation pipeline
- Vector indexing pipeline
- Similarity + filter‑based retrieval pipeline

### Analytical Synthesis Pipelines
- Passage ranking pipeline
- Extractive selection pipeline
- Verbatim assembly pipeline
- Exact‑wording enforcement pipeline
- Citation binding pipeline

---

## 2. RAG Technologies (Aligned to Purpose)

### Orchestration Layers
- **LangChain** (retrieval coordination, tool calling)
- **LlamaIndex** (document‑aware indexing, metadata handling)

### Vector Stores
- **FAISS** – local, fast academic research
- **Chroma** – metadata‑rich storage
- **Weaviate** – scalable, schema‑driven RAG

### Embeddings
- **Sentence‑Transformers** (research‑grade embeddings)
- **Instructor / BGE models** (query‑aware retrieval)

### Extractive RAG Controls
- Passage‑selection prompts
- Token‑whitelisting validators
- N‑gram overlap enforcement
- Diff‑based hallucination detection

---

## 3. Servers (Separated by Architecture)

### Architecture A – Ingestion & Retrieval
- **Uvicorn**
  - Handles:
    - File ingestion
    - Markdown conversion
    - Embedding
    - Retrieval APIs

### Architecture B – Analytical Synthesis
- **Hypercorn**
  - Handles:
    - Extractive synthesis
    - Cross‑document assembly
    - Long‑form analytic outputs
    - Secure, stable research endpoints

(*FastAPI serves as the common ASGI framework across both.*)

---

# V. Practical Summary / Actionable Takeaway

1. **You are not building one system**  
   You are building **two cooperating research architectures**.

2. **Architecture A prepares evidence**  
   It ingests, normalizes, structures, embeds, and retrieves.

3. **Architecture B assembles knowledge**  
   It synthesizes *only* by selecting and ordering verbatim text.

4. **Exact wording is enforced architecturally**  
   Not by convention, but by pipeline constraints and validation.

---

If you want next, I recommend one of the following deep dives:
- Designing the **extractive selection algorithm**
- Formalizing **exact‑wording enforcement at code level**
- Mapping this architecture to **qualitative dissertation methodology**

State which direction you want, and I will proceed precisely.