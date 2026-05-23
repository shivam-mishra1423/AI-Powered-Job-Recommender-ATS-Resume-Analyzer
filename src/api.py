"""FastAPI backend exposing the same capabilities as REST endpoints."""
import os, sys
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skill_extractor import extract_skills
from recommender import recommend_jobs
from ats_score import ats_score
from interview_qs import generate_questions

app = FastAPI(title="AI Job Recommender API", version="1.0")

class ResumeIn(BaseModel):
    resume_text: str
    top_n: int = 10

class ATSIn(BaseModel):
    resume_text: str
    jd_text: str

@app.get("/")
def root():
    return {"status":"ok","service":"AI Job Recommender & Resume Analyzer"}

@app.post("/skills")
def skills(p: ResumeIn):
    return {"skills": extract_skills(p.resume_text)}

@app.post("/recommend")
def recommend(p: ResumeIn):
    df = recommend_jobs(p.resume_text, top_n=p.top_n)
    return {"results": df.to_dict(orient="records")}

@app.post("/ats")
def ats(p: ATSIn):
    return ats_score(p.resume_text, p.jd_text)

@app.post("/interview_questions")
def iq(p: ResumeIn):
    return {"questions": generate_questions(extract_skills(p.resume_text))}
