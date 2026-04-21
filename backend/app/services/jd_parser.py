def extract_skills(jd: str):
    keywords = ["react", "python", "node", "ai", "ml", "java"]
    return [k for k in keywords if k in jd.lower()]