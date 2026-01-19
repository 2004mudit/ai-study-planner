
# AI Study Planner (Pydantic-AI Agent)

This is a full-stack generative AI application that creates a personalized daily study plan.

## Features
- FastAPI backend
- Pydantic-AI agent orchestration
- OpenRouter LLM integration
- Simple HTML/CSS frontend
- End-to-end AI generation

## How it works
1. User enters subjects, exam date, hours/day, and weak topics
2. Backend agent generates a structured study plan
3. Frontend displays the plan

## Tech Stack
- Python (FastAPI)
- Pydantic-AI
- OpenRouter (Mistral 7B)
- HTML/CSS/JS

---

Built for Potpie AI Round 1 Assessment.
## How to run locally

1. Clone the repository  
2. Install dependencies  
   pip install -r backend/requirements.txt  

3. Run the backend  
   uvicorn backend.app:app --reload  

4. Open frontend/index.html in your browser
