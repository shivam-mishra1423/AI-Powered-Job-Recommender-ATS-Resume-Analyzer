"""Domain-aware interview question generator based on detected skills."""

BANK = {
    "python":     ["Explain Python's GIL.", "Difference between list and tuple?", "What are decorators?"],
    "sql":        ["Difference between WHERE and HAVING.", "Explain window functions.", "Optimize a slow query — your approach?"],
    "pandas":     ["GroupBy vs Pivot in pandas.", "How do you handle missing values?", "Difference between merge and join."],
    "machine learning": ["Bias vs Variance tradeoff.", "Explain cross-validation.", "How do you handle class imbalance?"],
    "deep learning":    ["Vanishing gradient — what & how to fix?", "Adam vs SGD?", "Explain dropout."],
    "nlp":        ["TF-IDF vs Word2Vec vs BERT.", "What is attention?", "How does BERT differ from GPT?"],
    "transformers":["What is multi-head attention?", "Encoder vs Decoder transformer.", "Fine-tuning vs prompting."],
    "react":      ["useEffect vs useLayoutEffect.", "Reconciliation in React.", "How does Context differ from Redux?"],
    "fastapi":    ["Why is FastAPI fast?", "Pydantic validation example.", "Dependency Injection in FastAPI."],
    "docker":     ["Image vs Container.", "What is a multi-stage build?", "Docker Compose vs Kubernetes."],
    "aws":        ["Difference between EC2 and Lambda.", "What is S3 lifecycle policy?", "When would you use SageMaker?"],
    "spark":      ["Transformation vs Action in Spark.", "What is a DAG?", "Broadcast joins — when?"],
    "kubernetes": ["Pod vs Deployment.", "What is a Service?", "How does autoscaling work?"],
    "recommendation system": ["Content-based vs Collaborative filtering.", "Cold-start problem solutions.", "How to evaluate recommendations?"],
}

GENERIC = [
    "Walk me through your most challenging project.",
    "How do you debug a model that performs well in training but poorly in production?",
    "Describe a time you optimized a slow pipeline.",
    "How do you stay updated with new tech?",
    "What does 'production-ready code' mean to you?",
]

def generate_questions(skills, max_q=12):
    qs = []
    seen = set()
    for s in skills:
        for q in BANK.get(s, []):
            if q not in seen:
                qs.append({"skill": s, "question": q})
                seen.add(q)
            if len(qs) >= max_q:
                return qs
    for q in GENERIC:
        if len(qs) >= max_q: break
        if q not in seen:
            qs.append({"skill": "general", "question": q})
            seen.add(q)
    return qs
