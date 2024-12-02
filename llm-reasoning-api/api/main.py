from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from reasoners.lm import OpenAIModel
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()

MODEL_NAME = os.getenv("MODEL_NAME")

@app.get("/")
async def root():
    model = OpenAIModel(model=MODEL_NAME, use_azure=True)
    output = model.generate(["Hello, world!"]).text[0].strip()
    return {"message": output}


@app.get("/stream")
async def stream_intermediate_states():
    async def fake_streamer():
        for i in range(1, 6):
            yield f"Processing chunk {i}\n"
    return StreamingResponse(fake_streamer(), media_type="text/plain")
