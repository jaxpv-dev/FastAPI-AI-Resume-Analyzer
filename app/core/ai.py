import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_resume(resume_text: str, job_description: str) -> dict:
    prompt = f"""
    You are an expert ATS (Applicant Tracking System) and career coach.
    
    Analyze the following resume against the job description and provide:
    1. A match score out of 100
    2. Missing keywords or skills
    3. Strengths of the resume
    4. Specific suggestions to improve the resume
    
    Resume:
    {resume_text}
    
    Job Description:
    {job_description}
    
    Respond in this exact format:
    SCORE: [number only]
    MISSING: [comma separated keywords]
    STRENGTHS: [brief points]
    SUGGESTIONS: [brief points]
    """
    
    response = model.generate_content(prompt)
    text = response.text
    
    lines = text.strip().split("\n")
    result = {}
    
    for line in lines:
        if line.startswith("SCORE:"):
            try:
                result["match_score"] = int(line.replace("SCORE:", "").strip())
            except:
                result["match_score"] = 0
        elif line.startswith("MISSING:"):
            result["missing_keywords"] = line.replace("MISSING:", "").strip()
        elif line.startswith("STRENGTHS:"):
            result["strengths"] = line.replace("STRENGTHS:", "").strip()
        elif line.startswith("SUGGESTIONS:"):
            result["suggestions"] = line.replace("SUGGESTIONS:", "").strip()
    
    result["full_analysis"] = text
    return result