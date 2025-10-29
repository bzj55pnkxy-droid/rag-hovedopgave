# Project Planning

## Problem Statement

**Status:** ✅ Defined

**See:** [docs/problem-statement.md](./problem-statement.md)

### Project Focus
**Building a Curriculum-Aligned RAG Assistant for Datamatiker Students**

**Core Problem:** Generic AI assistants provide technically correct but pedagogically misaligned answers to students, causing confusion rather than learning.

**Solution:** A RAG-powered learning assistant that grounds responses in curriculum-appropriate materials (markdown files with metadata about semester, difficulty, prerequisites).

**Data Source:** Learning materials from DatamatikGuide project (personal EdTech initiative)

**Key Features:**
1. Semantic search in natural language
2. Metadata-aware filtering (semester, difficulty, prerequisites)
3. Citation mechanism (references to source materials)
4. Related topics discovery

**Success Criteria:**
- RAGAS evaluation metrics (faithfulness, relevancy, recall)
- Metadata filtering works correctly
- Citations provide clear source attribution
- Deployed via Docker for reproducibility

### Requirements Alignment
This project addresses course learning objectives by demonstrating:
- ✅ Systematic identification of system requirements
- ✅ Application of modern programming techniques and tools (RAG, vector databases, LLMs)
- ✅ Proper documentation for intended audience
- ✅ Systematic error detection (RAGAS evaluation framework)
- ✅ Communication of IT problems and solutions

## Project Phases

### Phase 1: Planning (Current)
- [x] Define specific problem/use case
- [ ] Research RAG implementations
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

## Timeline

**Total Duration:** 10 weeks

| Week | Phase | Goals |
|------|-------|-------|
| 1-2  | Planning | Define problem, finalize tech stack |
| 3-7  | Development | Implementation |
| 8-9  | Testing & Documentation | Quality assurance |
| 10   | Report & Presentation | Final deliverables |

*Timeline to be refined once problem statement is defined*

## Ideas & Brainstorming

Add ideas here as they come up:

-

## Questions to Answer

1. ✅ What specific problem will the RAG system solve?
   - **Answer:** Pedagogical misalignment in generic AI assistants that provide technically correct but contextually inappropriate answers to students

2. ✅ What data source(s) will be used for retrieval?
   - **Answer:** Learning materials from DatamatikGuide project (markdown files with frontmatter metadata)

3. ✅ Who is the target user/audience?
   - **Answer:** Datamatiker students seeking curriculum-aligned learning assistance

4. ✅ What are the success criteria?
   - **Answer:** RAGAS evaluation metrics, metadata filtering accuracy, citation clarity, Docker reproducibility

5. ✅ Individual or group project?
   - **Answer:** Individual project

### Additional Questions

6. Which LLM/Embedding model to use?
   - **Status:** TBD (Options: OpenAI, Anthropic, open-source models)

7. How many curriculum documents for PoC?
   - **Status:** TBD (Recommendation: 10-20 documents to demonstrate concept)

8. User testing participants?
   - **Status:** TBD (Target: 5 datamatiker students)

## Meeting Notes

Add notes from supervisor meetings, planning sessions, etc.
