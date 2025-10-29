# ML Best Practices for Hovedopgave

## Key Paper: How to Avoid Machine Learning Pitfalls

**Paper:** [How to avoid machine learning pitfalls: a guide for academic researchers](https://arxiv.org/html/2108.02497v4)
**Author:** Michael A. Lones, Heriot-Watt University
**Status:** To Read

### Why This Matters for RAG Project

This paper covers common mistakes in ML research across five stages:
1. **Pre-model planning** - Data quality and preparation
2. **Reliable model development** - Avoiding overfitting
3. **Robust evaluation** - Test set integrity
4. **Fair model comparison** - Statistical testing
5. **Result reporting** - Transparency and reproducibility

### Relevance to Your RAG System

**Data Quality**
- Applies to your document corpus curation for Chroma
- "Garbage in, garbage out" - ensure quality retrieval data

**Test Set Integrity**
- Critical for RAG evaluation with RAGAS
- Avoid data leakage between training and test sets
- Make sure retrieved documents don't appear in training data

**Evaluation Methodology**
- Use multiple metrics (connects well with RAGAS)
- Cross-validation for robust results
- Important for comparing different RAG configurations

**Fair Comparison**
- When comparing RAG approaches or baseline systems
- Statistical significance testing
- Avoid benchmark gaming

**Transparent Reporting**
- Document your retrieval corpus clearly
- Reproducibility (Docker helps here)
- Component ablation studies
- Critical for hovedopgave report quality

### Action Items

- [ ] Read paper thoroughly
- [ ] Apply checklist to RAG system design
- [ ] Use guidelines for evaluation methodology section in report
- [ ] Ensure reproducibility with Docker + documentation
- [ ] Follow reporting standards for academic integrity

### Notes

This will strengthen your hovedopgave by:
1. Avoiding common ML mistakes
2. Ensuring rigorous evaluation methodology
3. Supporting academic quality in your report
4. Demonstrating professional research approach
