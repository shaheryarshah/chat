from fastapi import FastAPI
from pydantic import BaseModel
import openai  # or import your chatbot model here

app = FastAPI()

# Define the request schema
class Question(BaseModel):
    question: str

# API endpoint that processes the question and returns an answer
@app.post("/get-answer")
async def get_answer(question: Question):
    # Replace this with actual chatbot processing code
    # Example:
    # response = your_chatbot.generate_response(question.question)
    response = {"answer": f"Answer to '{question.question}'"}
    
    return response

# Run the app with: uvicorn chatbot_api:app --host 0.0.0.0 --port 8000

