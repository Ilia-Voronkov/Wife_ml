KNOWN_SKILLS = [
    "python", "javascript", "sql", "git", "docker",
    "fastapi", "react", "html", "css", "linux",
    "aws", "postgresql", "mongodb", "redis", "api",
    "machine learning", "deep learning", "nlp",
    "pandas", "numpy", "scikit-learn", "tensorflow",
    "pytorch", "data analysis", "statistics"
]


def analyze_cv(cv_text: str, job_description: str) -> dict:
    cv_text = cv_text.lower()
    job_description = job_description.lower()

    required_skills = [skill for skill in KNOWN_SKILLS if skill in job_description]
    matching_skills = [skill for skill in required_skills if skill in cv_text]
    missing_skills = [skill for skill in required_skills if skill not in cv_text]

    if len(required_skills) == 0:
        score = 0
    else:
        score = round(len(matching_skills) / len(required_skills) * 100)

    suggestions = [f"Добавьте навык: {skill}" for skill in missing_skills]

    return {
        "score": score,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }
