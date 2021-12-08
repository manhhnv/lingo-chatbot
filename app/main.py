from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Sentence(BaseModel):
    content: str


@app.post("/chat/", tags=["React message"])
async def react(sentence: Sentence):
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
