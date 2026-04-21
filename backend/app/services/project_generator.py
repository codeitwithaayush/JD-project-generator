import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Stable model
model = genai.GenerativeModel("models/gemini-2.5-flash")

def generate_projects(jd: str):
    try:
        prompt = f"""
You are a senior software architect.

Given this job description:
{jd}

Generate EXACTLY 2 high-quality, non-generic projects.

For EACH project provide:
- name
- description
- tech_stack (array)
- resume_points (3 bullet points)
- folder_structure (string)

IMPORTANT:
- Make projects real-world and resume-worthy
- Avoid generic ideas like todo apps
- Use tech stack strictly from JD

Return ONLY valid JSON. No explanation.

Format:
{{
  "projects": [
    {{
      "name": "",
      "description": "",
      "tech_stack": [],
      "resume_points": [],
      "folder_structure": ""
    }}
  ]
}}
"""

        response = model.generate_content(prompt)

        text = response.text
        print("RAW GEMINI OUTPUT:", text)

        # Extract JSON safely
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if not match:
            return {"error": "Invalid JSON from Gemini", "projects": []}

        return json.loads(match.group())

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e), "projects": []}