# RAG Hovedopgave Project

## Project Overview
This is a RAG (Retrieval-Augmented Generation) application project.

## Technology Stack

### Frontend
- **assistant-ui**: React-based UI component library for AI chat interfaces
  - Note: Chainlit and other frontend frameworks have been deprecated

### Backend
- **Python-based backend** using LangChain for RAG pipeline
- **Package management**: uv
- **Memory handling**: Backend-managed (using LangChain memory classes)
- **API**: Must expose streaming endpoint compatible with assistant-ui/AI SDK

## Project Structure
- `src/rag_hovedopgave/chat.py`: Chat functionality
- `src/rag_hovedopgave/chat_bot.py`: Chatbot implementation
- `src/rag_hovedopgave/document.py`: Document handling

## Architecture Decisions
- **Memory**: Handled on backend for persistence, security, and RAG integration
- **Frontend**: assistant-ui for all UI components and chat interface
- **Communication**: Backend exposes streaming API endpoint that assistant-ui consumes

## Claude Code Memory Guidelines

### CLAUDE.md vs Knowledge Graph

Use the appropriate storage for different types of information:

**CLAUDE.md** (this file) — Project instructions
- Coding conventions and style guides
- Project architecture decisions
- How to run, build, test the project
- Technology choices and constraints
- Deployment procedures
- Anything that should be version-controlled and shared with the team

**Knowledge Graph** — Dynamic, personal memory
- Server IPs, instance IDs, resource names
- Personal preferences and workflows
- Current project status and ongoing work
- Environment-specific details (dev/staging/prod endpoints)
- Relationships between resources (e.g., "EC2 uses this key")
- Anything that changes frequently or is personal to the user

**Rule of thumb:** If it belongs in git, put it in CLAUDE.md. If it's personal context or evolving state, use the knowledge graph.
