from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from config.main import set_up
from setting.main import AppSetting
from starlette.middleware.cors import CORSMiddleware
from api.v1.api import api_router

# Set environment variables
set_up()

# Create appsSetting instance include (mongo_url, port)
appSetting = AppSetting()


app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

app.include_router(api_router, prefix="/api-v1")

if __name__ == "app.main":
    uvicorn.run(app, host="127.0.0.1", port=appSetting.port)
