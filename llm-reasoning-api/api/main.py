from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the LLM Reasoning API"}

@app.get("/stream")
async def stream_intermediate_states():
    async def fake_streamer():
        for i in range(1, 6):
            yield f"Processing chunk {i}\n"
    return StreamingResponse(fake_streamer(), media_type="text/plain")
