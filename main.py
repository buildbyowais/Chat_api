from fastapi import FastAPI
from app.scehmas import ChatRequest,ChatResponse
from app.summary_chat import ask_ai

app = FastAPI()


@app.get("/")
def hello():
    return{
        "message" : "Chat API running!"
    }

@app.post("/chat",response_model=ChatResponse)
def chat(data:ChatRequest):

    response = ask_ai(data.question)

    return{
        "answer" : response
    }