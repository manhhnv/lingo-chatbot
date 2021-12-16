from fastapi import APIRouter

from .endpoints import words, auth, book

api_router = APIRouter()
api_router.include_router(auth.router, tags=["User-management"], prefix="/users")
api_router.include_router(words.router, tags=["Word-management"], prefix="/words")
api_router.include_router(book.router, tags=["Book-management"], prefix="/books")
