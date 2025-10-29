---
date: 2025-10-29T16:30:32+0000
researcher: Claude
git_commit: N/A (not a git repository)
branch: N/A (not a git repository)
repository: rag-hovedopgave
topic: "RAG Hovedopgave Problem Statement Definition"
tags: [planning, problem-statement, rag, educational-technology, datamatiker]
status: complete
last_updated: 2025-10-29
last_updated_by: Claude
type: implementation_strategy
---

# Handoff: Problem Statement & Planning Complete

## Task(s)

**Status: COMPLETED**

1. ✅ **Define detailed problem statement** for huvudopgave RAG project
2. ✅ **Align problem with DatamatikGuide project** - Identified synergy between huvudopgave requirements and existing DatamatikGuide materials
3. ✅ **Update all project documentation** to reflect finalized problem statement and project focus

### Context
User is planning a 10-week Datamatiker hovedopgave (final project) and wanted to implement a RAG system. Through discussion, we identified that their existing DatamatikGuide project (personal EdTech initiative) provides perfect data source for a curriculum-aligned RAG assistant. The synergy: DatamatikGuide materials are already structured as markdown with frontmatter metadata (semester, difficulty, prerequisites, tags) - exactly what's needed for metadata-aware RAG filtering.

## Critical References

1. **docs/problem-statement.md** - Comprehensive 13-section academic problem statement (newly created)
2. **tech-stack.md** - Technology decisions and rationale (LangChain, Chroma, FastAPI, Gradio, RAGAS)
3. **/Users/kevinstrandberg/datamatiker/planning/features/ai-code-review/RAG/RAG-idea.md** - Original RAG concept from DatamatikGuide project that inspired this approach

## Recent Changes

- docs/problem-statement.md:1-350 (new file) - Complete academic problem statement
- docs/project-planning.md:3-36 - Updated with finalized problem statement and status
- docs/project-planning.md:40-66 - Updated all 4 phases with concrete tasks
- docs/project-planning.md:89-113 - Answered all 5 initial questions, added 3 new questions
- README.md:10-25 - Added project title and quick summary
- README.md:46-73 - Added core features, tech stack summary, and updated next steps

## Learnings

### Key Insight: Perfect Synergy Discovered
The DatamatikGuide project (/Users/kevinstrandberg/datamatiker/) contains learning materials that are **already structured perfectly for RAG**:
- Markdown files with YAML frontmatter
- Metadata: semester, difficulty, prerequisites, tags, estimated_time
- Content covers entire datamatiker curriculum
- User is creating these materials anyway (Phase 2 of DatamatikGuide)

This means:
- No external data access agreements needed
- Authentic curriculum content
- Self-referential demonstration value (can demo during thesis defense using actual course materials)
- PoC can evolve into DatamatikGuide Phase 3 feature

### Problem Statement Focus
**Core Problem**: Generic AI assistants (ChatGPT, GitHub Copilot) provide technically correct but **pedagogically misaligned** answers. Example: First-semester student asks about databases, gets feedback about ORMs, connection pooling, transactions - concepts they haven't learned yet.

**Solution**: RAG-powered assistant that filters by curriculum metadata (semester, difficulty, prerequisites) to provide **curriculum-appropriate** responses.

### Feasibility Confirmed
- Only needs 10-20 documents for PoC (not hundreds)
- Tech stack already selected is perfect (LangChain, Chroma, FastAPI, Gradio)
- Clear evaluation methodology via RAGAS framework
- Well-scoped for 10-week timeline

## Artifacts

### Created
1. **docs/problem-statement.md** - Comprehensive problem statement covering:
   - Executive summary
   - Problem analysis (educational context, technical context, gap analysis)
   - Proposed solution with 4 core features
   - Technical approach (architecture, tech stack, evaluation)
   - Success criteria (functional requirements, RAGAS metrics)
   - Scope and limitations (in/out of scope for 10-week PoC)
   - Academic value (alignment with course learning objectives)
   - Next steps with 4 phases
   - References and appendix

### Updated
2. **docs/project-planning.md** - Updated sections:
   - Problem statement status (marked as ✅ Defined)
   - All 5 initial questions answered
   - 3 additional questions added (LLM choice, document count, user testing)
   - All 4 phases updated with concrete tasks

3. **README.md** - Updated sections:
   - Project status and focus
   - Quick summary of problem/solution
   - 4 core features listed
   - Technology stack summary
   - Next steps with completed items checked off

## Action Items & Next Steps

### Immediate Next Steps (Phase 1 - Planning)
1. **Create system architecture diagram** - Visualize data flow from query → embedding → retrieval → synthesis → response
2. **Set up development environment** - Initialize Python project with uv, install dependencies (LangChain, Chroma, FastAPI, Gradio)
3. **Create evaluation dataset** - Prepare 20-30 test queries at different difficulty levels for RAGAS evaluation

### Phase 2 - Development (Weeks 3-7)
4. Implement document ingestion pipeline (parse markdown + frontmatter)
5. Set up Chroma vector database
6. Build FastAPI endpoints
7. Integrate LangChain RAG chain
8. Create Gradio UI
9. Implement metadata filtering

### Phase 3 - Testing & Evaluation (Weeks 8-9)
10. Run RAGAS evaluation
11. Compare with baseline (generic ChatGPT)
12. User testing with 5 datamatiker students
13. Document limitations and findings

### Phase 4 - Report & Presentation (Week 10)
14. Write hovedopgave report (max 40 pages)
15. Prepare 10-minute presentation
16. Finalize Docker deployment
17. Submit deliverables

### Still To Decide
- **LLM/Embedding Model**: OpenAI, Anthropic, or open-source (Mistral, LLaMA)
- **Number of Documents**: Recommendation is 10-20 for PoC, needs confirmation
- **User Testing Participants**: Target 5 datamatiker students

## Other Notes

### DatamatikGuide Connection
This hovedopgave serves as a functional prototype for DatamatikGuide Phase 3 (AI Code Review feature). The semantic search and metadata filtering infrastructure built here will directly power:
1. Curriculum-aligned code review feedback
2. Semantic search across learning materials
3. Related topics discovery
4. Prerequisite checking

### Course Requirements Alignment
Project demonstrates all required learning objectives per course 3050552:
- ✅ Systematic identification of system requirements
- ✅ Application of modern programming techniques (RAG, vector databases, LLMs)
- ✅ Proper documentation for intended audience
- ✅ Systematic error detection (RAGAS evaluation framework)
- ✅ Communication of IT problems and solutions

### Technology Stack Decisions
All core technologies selected and documented in tech-stack.md:
- **RAG Framework**: LangChain (industry standard, extensive RAG tooling)
- **Vector Database**: Chroma (Python-native, easy prototyping)
- **Backend**: FastAPI (async support, automatic docs)
- **Frontend**: Gradio (fast ML demo interfaces)
- **Evaluation**: RAGAS (RAG-specific metrics)
- **Deployment**: Google Cloud Run (with Railway as backup)
- **Dev Tools**: uv, Ruff, pytest, Docker

### Key Resources Referenced
- LangChain RAG Tutorial: https://python.langchain.com/docs/tutorials/rag/
- RAGAS Documentation: https://docs.ragas.io/
- ML Best Practices Paper: https://arxiv.org/html/2108.02497v4 (notes in research/ml-best-practices.md)
- Awesome RAG: https://github.com/Danielskry/Awesome-RAG

### User's Work Pattern
User has two related projects:
1. **/Users/kevinstrandberg/rag-hovedopgave/** - This hovedopgave project (current session)
2. **/Users/kevinstrandberg/datamatiker/** - DatamatikGuide EdTech SaaS project (data source)

Both projects are synergistic - the RAG system built for hovedopgave will become a feature in DatamatikGuide.
