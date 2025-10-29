# Problem Statement

**Project Title:** Building a Curriculum-Aligned RAG Assistant for Datamatiker Students

**Course:** Datamatiker Afsluttende Projekt (3050552)
**Semester:** 5th Semester, 2025-2026
**Duration:** 10 weeks
**Credits:** 15 ECTS
**Type:** Individual Project

## Executive Summary

This project addresses the pedagogical misalignment problem in AI-assisted learning by building a Retrieval-Augmented Generation (RAG) system that provides curriculum-appropriate guidance to datamatiker students. Unlike generic AI assistants that provide technically correct but contextually inappropriate answers, this system grounds responses in structured educational materials with metadata about semester, difficulty level, and prerequisites.

## Problem Analysis

### The Core Problem

Generic AI assistants (ChatGPT, GitHub Copilot, etc.) provide technically correct but pedagogically misaligned answers to students. When students seek help with their coursework, they often receive:

- **Terminology beyond their current knowledge**: A first-semester student asking about databases might receive feedback mentioning ORMs, connection pooling, and transaction isolation levels—concepts they haven't learned yet
- **Solutions requiring advanced patterns**: Suggestions to use design patterns or frameworks not covered in their curriculum
- **Missing pedagogical context**: No connection to learning objectives, course materials, or prerequisite knowledge
- **Inconsistent guidance**: Different answers from different tools, creating confusion about "correct" approaches

**Impact:** This creates confusion rather than learning. Students copy-paste solutions they don't understand, fail to build foundational knowledge, and struggle to progress through increasingly complex topics.

### Why This Matters

**Educational Context:**
- Danish datamatiker programs face 25% first-year and 45-55% total dropout rates
- Inadequate learning resources contribute to student struggles
- Traditional textbooks and documentation don't adapt to individual student levels
- Teachers can't provide individualized real-time feedback at scale

**Technical Context:**
- AI assistants are becoming ubiquitous in programming education
- Students will use these tools regardless of institutional policy
- Current tools don't understand curriculum structure or learning progression
- No existing solution bridges the gap between "technically correct" and "pedagogically appropriate"

### Gap in Current Solutions

**Generic AI Assistants:**
- ✅ Accessible, free/cheap, fast responses
- ❌ No curriculum awareness
- ❌ No difficulty filtering
- ❌ No citation of learning materials
- ❌ Inconsistent with course teaching

**Traditional E-Learning Platforms:**
- ✅ Curriculum-aligned content
- ✅ Structured learning paths
- ❌ No natural language querying
- ❌ Requires knowing exact terminology
- ❌ Limited cross-topic discovery
- ❌ No personalized feedback

**This Project Bridges Both:**
- ✅ Natural language interaction (like AI assistants)
- ✅ Curriculum-aligned responses (like e-learning)
- ✅ Metadata-aware filtering (adaptive to student level)
- ✅ Citation mechanism (transparent source attribution)

## Proposed Solution

### System Overview

A RAG-powered learning assistant that:
1. **Indexes structured educational content** (markdown files with frontmatter metadata)
2. **Enables semantic search** in natural language
3. **Filters results** by semester, difficulty, and prerequisites
4. **Provides cited answers** with explicit references to source materials
5. **Discovers related topics** to build conceptual connections

### Core Features for PoC

#### 1. Semantic Search
**Functionality:**
- Students query in natural language: "how do I undo a Git commit?"
- System embeds query in vector space
- Retrieves relevant curriculum sections based on semantic similarity
- Returns results even when exact terminology doesn't match

**Advantage over keyword search:**
- Beginner asks: "how to stop people from breaking my database queries"
- System finds: SQL injection prevention, prepared statements, input validation
- Bridges the vocabulary gap between beginners and experts

#### 2. Metadata-Aware Filtering
**Functionality:**
- Filter results by:
  - **Semester** (1-5): Scope content to appropriate stage
  - **Difficulty** (beginner/intermediate/advanced): Match cognitive load
  - **Prerequisites**: Check required foundational knowledge
  - **Tags**: Topic-based filtering

**Example:**
- Semester 1 student searches "databases"
  - Returns: SQL basics, table design, simple queries
  - Hides: Query optimization, indexing strategies, sharding
- Semester 3 student searches "databases"
  - Prioritizes: Advanced queries, performance tuning, normalization
  - Still accessible: Basic content for review

#### 3. Citation Mechanism
**Functionality:**
- All responses cite source materials
- Format: "According to Git Fundamentals (Section 3.2), resource URLs should be nouns..."
- Includes links to specific sections (e.g., `/topics/git-fundamentals#undoing-commits`)

**Pedagogical value:**
- Transforms AI feedback from "opinion" to "here's what your curriculum says"
- Students know where to review
- Builds trust in system accuracy
- Teachers can reference same materials in follow-up discussions

#### 4. Related Topics Discovery
**Functionality:**
- Surface prerequisite concepts students might need to review
- Show related topics for deeper understanding
- Create conceptual navigation paths

**Example:**
- Student views "REST API design"
- System suggests:
  - Prerequisites: HTTP methods, JSON, status codes
  - Related: Error handling, authentication, API testing
  - Next steps: GraphQL, WebSockets

### Data Source

**Learning materials from DatamatikGuide project** (separate EdTech SaaS initiative):
- Location: `planning/topics/` directory
- Format: Markdown files with YAML frontmatter
- Metadata includes: title, category, semester, difficulty, tags, prerequisites, estimated_time
- Topics cover: Programming, databases, version control, web development, DevOps, testing, system development

**Example frontmatter:**
```yaml
---
title: "Git Fundamentals"
category: "Version Control"
semester: 1
difficulty: "beginner"
tags: [git, cli, version-control]
estimated_time: 20
prerequisites: []
---
```

**Synergy advantage:**
- Materials created regardless for personal learning and future EdTech platform
- No external data agreements needed
- Authentic datamatiker curriculum coverage
- Can demonstrate tool's value during thesis defense using actual course materials

## Technical Approach

### Technology Stack

**Core Technologies:**
- **RAG Framework**: LangChain (industry standard, extensive RAG tooling)
- **Vector Database**: Chroma (Python-native, easy to prototype)
- **Backend**: FastAPI (async support, automatic docs)
- **Frontend**: Gradio (fast ML demo interfaces)
- **LLM**: TBD (OpenAI, Anthropic, or open-source)

**Development Tools:**
- **Package Manager**: uv (10-100x faster than pip)
- **Linting/Formatting**: Ruff (replaces Flake8, Black, isort)
- **Testing**: pytest, RAGAS (RAG-specific evaluation)
- **Containerization**: Docker (reproducibility)
- **Deployment**: Google Cloud Run (with Railway as backup)

### System Architecture (Simplified)

```
User Query (Natural Language)
    ↓
FastAPI Backend
    ↓
LangChain Orchestration
    ↓
Query Embedding (Vector)
    ↓
Chroma Vector Search (with metadata filters)
    ↓
Retrieved Documents (Top-K relevant sections)
    ↓
LLM Synthesis (with citations)
    ↓
Response to User (via Gradio UI)
```

### Evaluation Methodology

**RAGAS Framework** for RAG-specific metrics:
- **Faithfulness**: Are responses factually grounded in retrieved documents?
- **Answer Relevancy**: Do responses address the user's question?
- **Context Relevancy**: Are retrieved documents relevant to the query?
- **Context Recall**: Are all relevant documents retrieved?

**Baseline Comparisons:**
- RAG system vs. generic ChatGPT responses
- With metadata filtering vs. without
- Different chunking strategies
- Different embedding models

**Academic Rigor:**
- Follow ML best practices from "How to avoid machine learning pitfalls" (arxiv 2108.02497v4)
- Ensure test set integrity (no data leakage)
- Statistical significance testing
- Transparent reporting of limitations
- Reproducible via Docker

## Success Criteria

### Functional Requirements
- ✅ System accepts natural language queries
- ✅ Semantic search returns relevant curriculum sections
- ✅ Metadata filtering correctly scopes results by semester/difficulty
- ✅ Responses include citations to source materials
- ✅ Related topics surfaced based on query context
- ✅ Deployed via Docker for reproducibility

### Quality Metrics
- **Faithfulness > 0.8**: Responses grounded in retrieved documents
- **Answer Relevancy > 0.7**: Responses address user queries
- **Context Relevancy > 0.7**: Retrieved documents are relevant
- **User Study**: 5 datamatiker students test system, provide feedback

### Documentation Requirements
- System architecture documented
- Retrieval corpus described (which materials, how structured)
- Evaluation methodology detailed
- Limitations and future work identified
- Code repository with README

## Scope and Limitations

### In Scope (PoC for 10 weeks)
- Semantic search over structured markdown content
- Metadata-aware filtering
- Citation mechanism
- Evaluation with RAGAS
- Docker deployment
- 10-20 example curriculum documents

### Out of Scope
- Full curriculum coverage (hundreds of documents)
- Production-scale deployment (scalability testing)
- User authentication/authorization
- Code review feedback (future feature)
- Multi-language support
- Real-time collaborative features

### Known Limitations
- Limited to available curriculum materials
- No real-time content updates (requires re-embedding)
- LLM costs may limit query volume during testing
- Citation accuracy depends on chunking strategy
- English-language system (curriculum may be Danish)

## Academic and Professional Value

### Demonstrates Course Learning Objectives

Per course requirements (3050552), this project demonstrates:
1. **Systematic identification of system requirements**: Problem analysis, feature scoping, success criteria
2. **Application of modern programming techniques and tools**: RAG, vector databases, LLM integration, containerization
3. **Proper documentation for intended audience**: Technical docs, evaluation methodology, reproducible setup
4. **Systematic error detection**: RAGAS evaluation, comparison with baseline, user testing
5. **Communication of IT problems and solutions**: Problem statement, architectural decisions, presentation

### Career Development

**Technical Skills:**
- RAG implementation (increasingly valuable in AI/ML roles)
- Vector databases and semantic search
- LLM integration and prompt engineering
- API design with FastAPI
- Evaluation methodology for AI systems

**Portfolio Value:**
- Deployed system (Docker + Cloud Run)
- GitHub repository with professional README
- Demonstrates understanding of educational technology
- Shows ability to identify and solve real-world problems

**Resume Impact:**
- Experience with modern AI stack (LangChain, vector DBs, LLMs)
- GCP deployment experience
- Published educational tool
- Bridges software engineering and pedagogy

## Next Steps

### Phase 1: Planning (Weeks 1-2) ✓
- [x] Define problem statement
- [x] Finalize technology stack
- [ ] Create system architecture diagram
- [ ] Set up development environment
- [ ] Create evaluation dataset (test queries)

### Phase 2: Development (Weeks 3-7)
- [ ] Implement document ingestion pipeline
- [ ] Set up Chroma vector database
- [ ] Build FastAPI endpoints
- [ ] Integrate LangChain RAG chain
- [ ] Create Gradio UI
- [ ] Implement metadata filtering

### Phase 3: Testing & Evaluation (Weeks 8-9)
- [ ] Run RAGAS evaluation
- [ ] Compare with baseline (generic ChatGPT)
- [ ] User testing with datamatiker students
- [ ] Document limitations and findings

### Phase 4: Report & Presentation (Week 10)
- [ ] Write hovedopgave report (max 40 pages)
- [ ] Prepare 10-minute presentation
- [ ] Finalize Docker deployment
- [ ] Submit deliverables

## References

- **RAG Fundamentals**: [AWS - What is RAG?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- **LangChain RAG Tutorial**: https://python.langchain.com/docs/tutorials/rag/
- **RAGAS Evaluation**: https://docs.ragas.io/
- **ML Best Practices**: [How to avoid machine learning pitfalls](https://arxiv.org/html/2108.02497v4)
- **Awesome RAG**: https://github.com/Danielskry/Awesome-RAG

## Appendix: Alignment with DatamatikGuide

This hovedopgave serves as a functional prototype for **DatamatikGuide Phase 3** (AI Code Review feature). The semantic search and metadata filtering infrastructure built here will power:

1. **Curriculum-aligned code review feedback**
2. **Semantic search across learning materials**
3. **Related topics discovery**
4. **Prerequisite checking**

This creates a feedback loop: hlavopgave → prototype → thesis defense → refined EdTech product → benefit future students.
