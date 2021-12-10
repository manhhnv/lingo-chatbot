from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from config.main import set_up
from setting.main import AppSetting

# Set environment variables
set_up()

# Create appsSetting instance include (mongo_url, port)
appSetting = AppSetting()


app = FastAPI()


class Sentence(BaseModel):
    content: str


@app.post("/chat/", tags=["React message"])
async def react(sentence: Sentence):
    return {"message": "Hello World"}

if __name__ == "app.main":
    uvicorn.run(app, host="127.0.0.1", port=appSetting.port)
