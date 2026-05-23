"""Streamlit web app for AI Job Recommender + Resume Analyzer."""
import os, sys, tempfile
import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resume_parser import parse_resume
from skill_extractor import extract_skills
from recommender import recommend_jobs
from ats_score import ats_score
from interview_qs import generate_questions

st.set_page_config(page_title="AI Job Recommender & Resume Analyzer", page_icon="🚀", layout="wide")
st.title("🚀 AI Powered Job Recommendation & Resume Analyzer")

uploaded = st.file_uploader("Upload your Resume (PDF / DOCX / TXT)", type=["pdf","docx","txt"])
manual = st.text_area("...or paste your resume text here", height=180)

resume_text = ""
if uploaded:
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded.name)[1]) as t:
        t.write(uploaded.read()); path = t.name
    resume_text = parse_resume(path)
elif manual.strip():
    resume_text = manual

tab1, tab2, tab3, tab4 = st.tabs(["🔍 Extract Skills", "💼 Recommend Jobs", "📊 ATS Score (vs JD)", "🎤 Interview Qs"])

with tab1:
    if resume_text:
        skills = extract_skills(resume_text)
        st.success(f"Detected {len(skills)} skills")
        st.write(skills)
    else:
        st.info("Upload a resume to extract skills.")

with tab2:
    top_n = st.slider("Top N jobs", 5, 30, 10)
    if st.button("Recommend Jobs", type="primary"):
        if not resume_text:
            st.warning("Please upload/paste a resume first.")
        else:
            res = recommend_jobs(resume_text, top_n=top_n)
            st.dataframe(res[["match_score","title","company","location","experience","salary","skills"]], use_container_width=True)

with tab3:
    jd = st.text_area("Paste a target Job Description", height=200, key="jd")
    if st.button("Calculate ATS Score"):
        if not resume_text or not jd.strip():
            st.warning("Need both resume and JD.")
        else:
            r = ats_score(resume_text, jd)
            c1,c2,c3 = st.columns(3)
            c1.metric("ATS Score", f"{r['score']}%")
            c2.metric("Semantic Similarity", f"{r['semantic_similarity']}%")
            c3.metric("Skill Coverage", f"{r['skill_coverage']}%")
            st.subheader("✅ Matched Skills"); st.write(r["matched_skills"] or "—")
            st.subheader("❗ Missing Skills (learn these)"); st.write(r["missing_skills"] or "—")

with tab4:
    if st.button("Generate Interview Questions"):
        if not resume_text:
            st.warning("Upload a resume first.")
        else:
            skills = extract_skills(resume_text)
            qs = generate_questions(skills, max_q=15)
            for i,q in enumerate(qs,1):
                st.markdown(f"**Q{i}.** _({q['skill']})_ {q['question']}")
