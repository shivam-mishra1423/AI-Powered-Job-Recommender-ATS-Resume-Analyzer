"""Build TF-IDF vectorizer + jobs matrix index."""
import os, joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from preprocess import clean_text

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "jobs.csv")
MODELS = os.path.join(ROOT, "models")
os.makedirs(MODELS, exist_ok=True)

def main():
    df = pd.read_csv(DATA)
    print(f"Loaded {len(df)} jobs")
    corpus = (df["title"].fillna("") + " " +
              df["skills"].fillna("") + " " +
              df["description"].fillna("")).apply(clean_text)

    vec = TfidfVectorizer(max_features=5000, ngram_range=(1,2), min_df=2)
    mat = vec.fit_transform(corpus)
    print("TF-IDF matrix:", mat.shape)

    joblib.dump(vec, os.path.join(MODELS, "tfidf_jobs.joblib"))
    joblib.dump(mat, os.path.join(MODELS, "jobs_matrix.joblib"))
    print("Saved models -> models/")

if __name__ == "__main__":
    main()
