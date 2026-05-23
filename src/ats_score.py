from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import clean_text
from skill_extractor import extract_skills

def ats_score(resume_text: str, jd_text: str):
    a = clean_text(resume_text); b = clean_text(jd_text)
    if not a or not b:
        return {"score": 0.0, "matched_skills": [], "missing_skills": []}
    v = TfidfVectorizer(ngram_range=(1,2), max_features=3000)
    m = v.fit_transform([a, b])
    sim = float(cosine_similarity(m[0], m[1])[0,0])

    resume_skills = set(extract_skills(resume_text))
    jd_skills     = set(extract_skills(jd_text))

    matched = sorted(resume_skills & jd_skills)
    missing = sorted(jd_skills - resume_skills)

    # Blended ATS score: 60% semantic + 40% skill coverage
    coverage = (len(matched) / len(jd_skills)) if jd_skills else 0.0
    score = round((0.6 * sim + 0.4 * coverage) * 100, 2)
    return {
        "score": score,
        "semantic_similarity": round(sim * 100, 2),
        "skill_coverage": round(coverage * 100, 2),
        "matched_skills": matched,
        "missing_skills": missing,
    }
