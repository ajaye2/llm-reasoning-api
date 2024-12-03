from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse
from reasoners.lm import OpenAIModel
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from typing import List, Dict, Any

load_dotenv()

app = FastAPI()

MODEL_NAME = os.getenv("MODEL_NAME")

class ChainOfThoughtRequest(BaseModel):
    prompt: str
    temperature: float | None = 1.0

@app.get("/")
async def root():
    return {"response": "Welcome to the LLM Reasoning API"}

@app.get("/stream")
async def stream_intermediate_states():
    async def fake_streamer():
        for i in range(1, 6):
            yield f"Processing chunk {i}\n"
    return StreamingResponse(fake_streamer(), media_type="text/plain")

@app.post("/chain_of_thought")
def chain_of_thought(request: ChainOfThoughtRequest):
    try:
        model = OpenAIModel(model=MODEL_NAME, use_azure=True)
        
        prompt = "Let's think step by step. \n" + request.prompt

        response = model.generate(
            [prompt],
            temperature=request.temperature
        ).text[0]
        
        return {
            "response": response,
        }
    except Exception as e:
        raise HTTPException(status_code=500)
