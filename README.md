# 🚀 AI-Powered Job Recommendation & ATS Resume Analyzer

An advanced **Data Science + Artificial Intelligence + NLP** project that intelligently analyzes resumes, recommends jobs, calculates ATS scores, identifies missing skills, and generates interview questions using Machine Learning and Transformer-based NLP models.

🔗 **Live Demo:**  
https://shivam-ai-job-recommender.streamlit.app/

🔗 **GitHub Repository:**  
https://github.com/shivam-mishra1423/AI-Powered-Job-Recommender-ATS-Resume-Analyzer

---

# 📌 Project Overview

This project simulates a real-world **AI Hiring & Recruitment System** used by modern HR platforms and Applicant Tracking Systems (ATS).

The system can:

✅ Upload and analyze resumes (PDF / DOCX / TXT)  
✅ Extract technical skills using NLP  
✅ Recommend best matching jobs  
✅ Calculate ATS resume score against Job Description  
✅ Detect missing skills candidates should learn  
✅ Generate domain-specific interview questions  
✅ Provide an interactive Streamlit dashboard  
✅ Expose REST APIs using FastAPI  

---

# 🧠 Key AI & Data Science Features

## 🔹 Resume Parsing
The system extracts raw text from:
- PDF resumes
- DOCX resumes
- TXT files

using intelligent document parsing techniques.

---

## 🔹 NLP-Based Skill Extraction
Natural Language Processing (NLP) techniques are used to identify:
- Programming languages
- Frameworks
- Tools
- Technologies
- Soft skills

from candidate resumes automatically.

---

## 🔹 AI Job Recommendation Engine
The recommendation engine uses:

- TF-IDF Vectorization
- Cosine Similarity
- Sentence-BERT Embeddings

to match resumes with relevant jobs from large datasets.

---

## 🔹 ATS Score Calculation
The ATS engine compares:
- Resume content
- Target Job Description

and calculates a smart ATS compatibility score similar to real recruitment systems.

---

## 🔹 Missing Skill Detection
The project identifies:
- Missing technologies
- Required skills
- Learning gaps

that candidates should improve for better job matching.

---

## 🔹 AI Interview Question Generator
Generates interview questions dynamically for domains like:
- Data Science
- Machine Learning
- Python
- Web Development
- DevOps
- Artificial Intelligence

---

# 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| NLP | NLTK, Sentence-Transformers |
| Deep Learning | BERT Transformers |
| Backend API | FastAPI |
| Frontend UI | Streamlit |
| Model Serialization | Joblib |
| Resume Parsing | PyPDF2, python-docx |
| Deployment | Streamlit Cloud |
| Version Control | Git & GitHub |

---

# 📚 Libraries Explained

## 📌 Pandas
Used for:
- Data cleaning
- CSV handling
- Dataset preprocessing
- Tabular data manipulation

---

## 📌 NumPy
Used for:
- Numerical operations
- Vector calculations
- Matrix computations

---

## 📌 Scikit-learn
Used for:
- TF-IDF Vectorization
- Cosine Similarity
- Machine Learning utilities
- Feature extraction

---

## 📌 NLTK
Used for:
- Text preprocessing
- Stopword removal
- Tokenization
- NLP utilities

---

## 📌 Sentence-Transformers
Used for:
- Semantic similarity
- Sentence embeddings
- BERT-based intelligent matching

---

## 📌 Streamlit
Used for:
- Building interactive AI web applications
- Uploading resumes
- Displaying recommendations visually

---

## 📌 FastAPI
Used for:
- Building high-performance REST APIs
- Backend integration
- Model serving

---

# 📂 Project Structure

```bash
job_recommender/
│
├── data/                  
│   ├── jobs.csv
│   └── resumes.csv
│
├── models/                
│   ├── tfidf_vectorizer.pkl
│   └── job_index.pkl
│
├── notebooks/             
│   └── EDA_Modeling.ipynb
│
├── sample_resumes/        
│
├── src/
│   ├── preprocess.py
│   ├── skill_extractor.py
│   ├── recommender.py
│   ├── ats_score.py
│   ├── interview_qs.py
│   ├── resume_parser.py
│   ├── train.py
│   ├── app.py
│   └── api.py
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
