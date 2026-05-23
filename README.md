# AI Powered Job Recommendation & Resume Analyzer System

An end-to-end Data Science / NLP project that:
- Accepts a candidate resume (PDF / DOCX / TXT)
- Extracts skills using NLP
- Recommends best matching jobs (TF-IDF + Cosine Similarity / BERT embeddings)
- Calculates an ATS score for a target Job Description
- Identifies missing skills the candidate should learn
- Generates likely interview questions based on the resume's domain

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, NLTK, Sentence-Transformers (BERT),
Streamlit (UI), FastAPI (REST API), Joblib, PyPDF2, python-docx, Docker-ready.

## Project Structure
```
job_recommender/
├── data/                  # Jobs + Resume datasets (CSV)
├── src/
│   ├── preprocess.py      # Text cleaning utilities
│   ├── skill_extractor.py # Skill extraction from resume text
│   ├── recommender.py     # Job recommendation engine
│   ├── ats_score.py       # ATS score + missing skills
│   ├── interview_qs.py    # Interview question generator
│   ├── resume_parser.py   # PDF/DOCX/TXT parser
│   ├── train.py           # Build TF-IDF + job index
│   ├── app.py             # Streamlit UI
│   └── api.py             # FastAPI backend
├── models/                # Saved vectorizers / indexes
├── notebooks/             # EDA + Modeling notebook
├── sample_resumes/        # Example resumes
├── Dockerfile
├── requirements.txt
└── README.md
```

## Run

```bash
pip install -r requirements.txt
python src/train.py
streamlit run src/app.py
# or
uvicorn src.api:app --reload
```

## Resume-ready bullet points
- Built an AI-powered Job Recommendation & Resume Analyzer using NLP, TF-IDF
  and Sentence-BERT embeddings, achieving high-quality top-N job matches
  over a 5,000+ jobs dataset.
- Implemented an ATS scoring engine that computes resume–JD similarity and
  flags missing skills, mimicking real HR Applicant Tracking Systems.
- Designed a domain-aware interview question generator covering Data
  Science, Web Dev, DevOps, etc.
- Deployed dual interfaces — Streamlit web app and FastAPI REST API —
  containerized via Docker, deployable to AWS / Render.

## Author
Built as a portfolio project to showcase end-to-end ML + NLP + Deployment skills.
