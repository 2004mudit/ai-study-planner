from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic_ai import Agent
import requests
import traceback

app = FastAPI()

# ---------------------------
# CORS CONFIG (allow frontend)
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all for now (safe for demo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# Input Schema
# ---------------------------
class StudyInput(BaseModel):
    subjects: str
    exam_date: str
    hours_per_day: int
    weak_topics: str

# ---------------------------
# System Prompt
# ---------------------------
SYSTEM_PROMPT = (
    "You are an AI Study Planner. "
    "Generate a clear, structured daily study plan. "
    "Include revision slots. "
    "Keep it concise and practical."
)

# ---------------------------
# Pydantic-AI Agent
# ---------------------------
agent = Agent(system_prompt=SYSTEM_PROMPT)

# ---------------------------
# OpenRouter Setup (HARDCODED KEY)
# ---------------------------
OPENROUTER_API_KEY = "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"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://srmist.edu.in",
    "X-Title": "AI Study Planner"
}

def call_openrouter(prompt: str) -> str:
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 1000
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=60
    )

    if response.status_code != 200:
        return f"Error: AI service failed ({response.status_code}) | {response.text}"

    data = response.json()
    return data["choices"][0]["message"]["content"]

# ---------------------------
# API Endpoint
# ---------------------------
@app.post("/generate-plan")
async def generate_plan(data: StudyInput):
    try:
        prompt = f"""
Subjects: {data.subjects}
Exam Date: {data.exam_date}
Hours per day: {data.hours_per_day}
Weak topics: {data.weak_topics}

Create a daily study plan with revision slots.
"""

        ai_text = call_openrouter(prompt)

        return {"plan": ai_text}

    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}

@app.get("/")
def root():
    return {"message": "AI Study Planner API (CORS enabled) is running"}
