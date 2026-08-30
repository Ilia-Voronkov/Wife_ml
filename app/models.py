from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    cv_text: str
    job_description: str

class AnalysisResponse(BaseModel):
    score: int
    matching_skills: list[str]
    missing_skills: list[str]
    suggestions: list[str]
    