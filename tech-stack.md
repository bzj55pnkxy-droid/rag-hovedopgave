# Technology Stack

## Core Technologies

### RAG Framework

#### LangChain
- **Status:** Selected
- **Purpose:** RAG orchestration framework
- **Website:** https://www.langchain.com/
- **Rationale:**
  - Industry-standard framework for building LLM applications
  - Extensive RAG tooling and abstractions
  - Large community and ecosystem
  - Excellent integration with vector databases (including Chroma)
  - Built-in chains for document loading, splitting, retrieval
- **Key Features:**
  - Document loaders for multiple formats
  - Text splitters for chunking
  - Retrieval chains and prompts
  - Memory management
  - Agent capabilities
  - LLM provider abstraction

### Vector Database

#### Chroma
- **Status:** Selected
- **Purpose:** Vector database for RAG implementation
- **Website:** https://www.trychroma.com/
- **Rationale:**
  - Open-source vector database
  - Python-native with simple API
  - Supports multiple embedding models
  - Good for development and prototyping
  - Native LangChain integration
- **Key Features:**
  - In-memory or persistent storage
  - Built-in embedding functions
  - Filtering and metadata support
  - Easy local development

### Backend Framework

#### FastAPI
- **Status:** Selected
- **Purpose:** REST API backend
- **Website:** https://fastapi.tiangolo.com/
- **Rationale:**
  - Modern, fast Python framework
  - Automatic API documentation (OpenAPI/Swagger)
  - Async support for LLM calls
  - Type hints and validation
  - Production-ready
- **Key Features:**
  - Automatic request validation
  - Built-in docs UI
  - Easy integration with async operations
  - Great for ML/AI services

### Frontend/UI

#### Gradio
- **Status:** Selected
- **Purpose:** User interface for RAG demo
- **Website:** https://www.gradio.app/
- **Rationale:**
  - Quick to build ML/AI interfaces
  - Built-in chat components
  - Perfect for demos and prototypes
  - Can integrate with FastAPI
  - Minimal frontend code needed
- **Key Features:**
  - Pre-built chat interface
  - Easy to create shareable demos
  - Simple API
  - Good for academic projects

## Development Tools

### Package Manager

#### uv
- **Status:** Selected
- **Purpose:** Fast Python package manager
- **Website:** https://github.com/astral-sh/uv
- **Rationale:**
  - 10-100x faster than pip
  - Built in Rust
  - Drop-in replacement for pip
  - Better dependency resolution
- **Key Features:**
  - Fast installation
  - Lock files for reproducibility
  - Compatible with pip requirements

### Linting/Formatting

#### Ruff
- **Status:** Selected
- **Purpose:** Python linter and formatter
- **Website:** https://github.com/astral-sh/ruff
- **Rationale:**
  - Extremely fast (written in Rust)
  - Replaces multiple tools (Flake8, Black, isort)
  - Easy configuration
  - Great VS Code integration
- **Key Features:**
  - Fast linting and formatting
  - Autofix capabilities
  - Extensive rule set

### Testing

#### pytest
- **Status:** Selected
- **Purpose:** General testing framework
- **Website:** https://pytest.org/
- **Rationale:**
  - Industry standard for Python
  - Simple and powerful
  - Great plugin ecosystem
  - Easy to write and maintain tests
- **Key Features:**
  - Fixtures for test setup
  - Parametrized testing
  - Great assertion introspection
  - Coverage reporting

#### RAGAS
- **Status:** Under Consideration
- **Purpose:** RAG evaluation framework
- **Website:** https://docs.ragas.io/
- **Rationale:**
  - Specialized for evaluating RAG systems
  - Provides metrics for retrieval and generation quality
  - Important for demonstrating system effectiveness in report
  - Industry-standard evaluation approach
- **Key Metrics:**
  - Faithfulness (factual accuracy)
  - Answer relevancy
  - Context relevancy
  - Context recall
  - Answer similarity
- **Use Case:** Evaluate and compare RAG configurations, demonstrate system quality in hovedopgave report

### Containerization

#### Docker
- **Status:** Selected
- **Purpose:** Containerization for deployment
- **Website:** https://www.docker.com/
- **Rationale:**
  - Standard for deployment
  - Ensures consistency across environments
  - Required for most cloud platforms
  - Simplifies dependency management
- **Key Features:**
  - Reproducible builds
  - Easy deployment
  - Works with all cloud platforms

## To Be Determined

### LLM/Embedding Model
- **Options:** OpenAI, Anthropic, Open-source models (LLaMA, Mistral)
- **Decision Pending**

### Deployment Platform

#### Google Cloud Run (Primary Choice)
- **Status:** Selected (with Railway as backup)
- **Purpose:** Serverless container deployment
- **Website:** https://cloud.google.com/run
- **Rationale:**
  - Serverless, scales to zero (pay only for usage)
  - Part of GCP ecosystem (good for resume/job market)
  - Production-grade infrastructure
  - Generous free tier (2M requests/month)
  - Better learning experience for professional development
- **Key Features:**
  - Automatic scaling
  - Built-in HTTPS
  - Container-based deployment
  - Easy integration with other GCP services
- **Backup Plan:** If setup proves too complex, pivot to Railway

#### Railway (Backup Option)
- **Status:** Backup deployment option
- **Purpose:** Simplified deployment alternative
- **Website:** https://railway.app/
- **Why as backup:**
  - Much simpler setup process
  - Modern developer experience
  - Quick to deploy
  - Good for getting project live quickly if time is constrained

## Decision Log

| Date | Technology | Decision | Rationale |
|------|-----------|----------|-----------|
| 2025-10-29 | Vector DB | Chroma | Ease of use, Python-native, good for RAG |
| 2025-10-29 | RAG Framework | LangChain | Industry standard, extensive tooling, Chroma integration |
| 2025-10-29 | Programming Language | Python | Required for LangChain + Chroma stack |
| 2025-10-29 | Backend Framework | FastAPI | Modern, async support, great for ML services |
| 2025-10-29 | Frontend/UI | Gradio | Quick ML demos, built-in chat interface |
| 2025-10-29 | Package Manager | uv | 10-100x faster than pip, better dependency resolution |
| 2025-10-29 | Linter/Formatter | Ruff | Extremely fast, replaces multiple tools |
| 2025-10-29 | Testing | pytest | Industry standard, powerful and simple |
| 2025-10-29 | RAG Evaluation | RAGAS (considering) | Specialized RAG metrics, important for project evaluation |
| 2025-10-29 | Containerization | Docker | Standard for deployment, consistency |
| 2025-10-29 | Deployment | Google Cloud Run | Enterprise-grade, GCP experience, generous free tier (Railway as backup) |

## Resources

### General
- [What is RAG?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [Awesome RAG](https://github.com/Danielskry/Awesome-RAG) - Comprehensive collection of RAG papers, tools, frameworks, and tutorials

### Research Papers & Methodology
- [How to Avoid Machine Learning Pitfalls](https://arxiv.org/html/2108.02497v4) - Academic guide for rigorous ML research methodology (see research/ml-best-practices.md for detailed notes)

### LangChain
- [LangChain Documentation](https://python.langchain.com/)
- [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)

### Chroma
- [Chroma Documentation](https://docs.trychroma.com/)
- [LangChain + Chroma Integration](https://python.langchain.com/docs/integrations/vectorstores/chroma/)

### FastAPI
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI GitHub](https://github.com/tiangolo/fastapi)

### Gradio
- [Gradio Documentation](https://www.gradio.app/docs)
- [Gradio GitHub](https://github.com/gradio-app/gradio)

### Development Tools
- [uv Documentation](https://github.com/astral-sh/uv)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [pytest Documentation](https://docs.pytest.org/)
- [RAGAS Documentation](https://docs.ragas.io/en/stable/) - RAG evaluation framework
- [Docker Documentation](https://docs.docker.com/)

### Deployment
- [Render Documentation](https://render.com/docs)
- [Railway Documentation](https://docs.railway.app/)
- [Google Cloud Run Documentation](https://cloud.google.com/run/docs)

## Notes

Add any additional notes, comparisons, or considerations here.
