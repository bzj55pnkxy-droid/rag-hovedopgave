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
