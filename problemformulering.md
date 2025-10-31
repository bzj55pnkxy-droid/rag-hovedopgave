Proposed Problem Statement for Hovedopgave:

"Building a Curriculum-Aligned RAG Assistant for Datamatiker Students"

Problem:
Generic AI assistants (ChatGPT, GitHub Copilot) provide technically correct but pedagogically misaligned answers to students. A first-semester student asking about databases might receive feedback mentioning
ORMs, connection pooling, and transactions—concepts they haven't learned yet. This creates confusion rather than learning.

Solution:
A RAG-powered learning assistant that grounds responses in curriculum-appropriate materials. By indexing structured educational content (markdown files with metadata about semester, difficulty,
prerequisites), the system provides answers aligned with what students should know at their current stage.

Core Features for PoC:

1. Semantic Search: Students query in natural language ("how do I undo a Git commit?") and receive relevant curriculum sections
2. Metadata-Aware Filtering: Filter results by semester, difficulty level, and prerequisites
3. Citation Mechanism: All answers cite specific sections from source materials
4. Related Topics Discovery: Surface prerequisite and related concepts

Data Source:
Learning materials created for DatamatikGuide project (planning/topics/ directory) covering datamatiker curriculum topics

Success Criteria:

- Semantic search returns curriculum-appropriate results (evaluated with RAGAS metrics)
- Metadata filtering correctly scopes content to student level
- Citations provide clear source attribution
- System can be deployed via Docker for reproducibility

Would you like me to:

1. Create a detailed problem statement document for your hovedopgave project?
2. Define the specific features to include/exclude from the PoC?
3. Create a project structure that integrates with your DatamatikGuide materials?
