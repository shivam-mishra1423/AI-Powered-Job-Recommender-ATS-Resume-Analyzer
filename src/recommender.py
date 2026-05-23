import os, joblib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(ROOT, "models")

def load_index():
    vec  = joblib.load(os.path.join(MODEL_DIR, "tfidf_jobs.joblib"))
    mat  = joblib.load(os.path.join(MODEL_DIR, "jobs_matrix.joblib"))
    jobs = pd.read_csv(os.path.join(ROOT, "data", "jobs.csv"))
    return vec, mat, jobs

def recommend_jobs(resume_text: str, top_n: int = 10):
    from preprocess import clean_text
    vec, mat, jobs = load_index()
    q = vec.transform([clean_text(resume_text)])
    sims = cosine_similarity(q, mat).ravel()
    idx = np.argsort(-sims)[:top_n]
    out = jobs.iloc[idx].copy()
    out["match_score"] = (sims[idx] * 100).round(2)
    return out.reset_index(drop=True)
