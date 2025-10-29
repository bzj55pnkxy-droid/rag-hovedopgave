# RAG Hovedopgave - Datamatiker Final Project

## Project Overview

**Course:** Datamatiker Afsluttende Projekt (3050552)
**Semester:** 5th Semester, 2025-2026
**Duration:** 10 weeks
**Credits:** 15 ECTS

## Project Status

**Status:** Planning Phase
**Focus:** Building a Curriculum-Aligned RAG Assistant for Datamatiker Students

### Project Title
Building a Curriculum-Aligned RAG Assistant for Datamatiker Students

### Quick Summary
This project addresses the pedagogical misalignment problem in AI-assisted learning. Generic AI assistants (ChatGPT, GitHub Copilot) provide technically correct but contextually inappropriate answers to students—a first-semester student asking about databases might receive feedback mentioning ORMs and connection pooling before learning basic SQL.

**Solution:** A RAG-powered learning assistant that grounds responses in curriculum-appropriate materials, filtering by semester, difficulty, and prerequisites.

**Data Source:** Learning materials from DatamatikGuide project (personal EdTech initiative)

**See:** [docs/problem-statement.md](docs/problem-statement.md) for detailed problem analysis

## Key Deliverables

- Project Report (PDF, A4)
  - Individual: Max 40 pages
  - Group: Max 20 base pages + 20 per additional student
- Optional: Product/Software Implementation
- Presentation: 10 minutes per student
- Oral Exam: 20 minutes individual

## Repository Structure

```
/docs           - Project documentation and planning
/tech-stack.md  - Technology choices and rationale
/src            - Source code (TBD)
/tests          - Test suite (TBD)
/research       - Research notes and references
```

## Core Features (PoC)

1. **Semantic Search**: Query in natural language, get relevant curriculum sections
2. **Metadata-Aware Filtering**: Filter by semester, difficulty, prerequisites
3. **Citation Mechanism**: All responses cite source materials
4. **Related Topics Discovery**: Surface prerequisite and related concepts

## Technology Stack

- **RAG Framework**: LangChain
- **Vector Database**: Chroma
- **Backend**: FastAPI
- **Frontend**: Gradio
- **Evaluation**: RAGAS (faithfulness, relevancy, recall metrics)
- **Deployment**: Docker + Google Cloud Run

**See:** [tech-stack.md](tech-stack.md) for full technology decisions and rationale

## Next Steps

- [x] Define specific problem statement
- [x] Finalize technology stack
- [ ] Create system architecture diagram
- [ ] Set up development environment
- [ ] Create evaluation dataset (test queries)
- [ ] Implement document ingestion pipeline

**See:** [docs/project-planning.md](docs/project-planning.md) for detailed timeline and phases
