"""Skill extractor using a curated tech skill dictionary."""
import re

SKILLS = sorted(set([
    # Programming
    "python","java","c++","c#","javascript","typescript","go","rust","kotlin","swift","scala","r","matlab","sql","nosql","bash","shell",
    # Data / ML
    "pandas","numpy","scipy","scikit-learn","sklearn","tensorflow","keras","pytorch","xgboost","lightgbm","catboost",
    "matplotlib","seaborn","plotly","statsmodels","spacy","nltk","huggingface","transformers","bert","gpt","llm","rag",
    "machine learning","deep learning","nlp","computer vision","reinforcement learning","data analysis","data visualization",
    "feature engineering","time series","recommendation system","clustering","classification","regression",
    # Big data
    "spark","pyspark","hadoop","hive","kafka","airflow","dbt","snowflake","databricks","bigquery","redshift",
    # Web
    "react","angular","vue","next.js","node.js","express","django","flask","fastapi","spring","graphql","rest api","html","css","tailwind",
    # DB
    "mysql","postgresql","mongodb","sqlite","oracle","redis","elasticsearch","cassandra",
    # Cloud / DevOps
    "aws","azure","gcp","docker","kubernetes","terraform","jenkins","ci/cd","git","github","gitlab","linux",
    "lambda","s3","ec2","sagemaker","cloudwatch","render","heroku","vercel",
    # Misc
    "excel","power bi","tableau","looker","jira","agile","scrum","etl","mlops","streamlit","selenium",
]))

# Sort longest first to greedily match multi-word skills first
SKILL_PATTERNS = sorted(SKILLS, key=len, reverse=True)

def extract_skills(text: str):
    if not isinstance(text, str):
        return []
    t = " " + text.lower() + " "
    found = []
    for skill in SKILL_PATTERNS:
        pat = r'(?<![a-z0-9])' + re.escape(skill) + r'(?![a-z0-9])'
        if re.search(pat, t):
            found.append(skill)
    # dedupe preserving order
    seen = set(); out = []
    for s in found:
        if s not in seen:
            seen.add(s); out.append(s)
    return out
