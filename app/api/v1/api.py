from fastapi import APIRouter

from .endpoints import login, words

api_router = APIRouter()
api_router.include_router(login.router, tags=["User-management"], prefix="/users")
api_router.include_router(words.router, tags=["Word-management"], prefix="/words")
