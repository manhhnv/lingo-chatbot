from fastapi import APIRouter, Path, Query
from typing import Optional

router = APIRouter()


@router.get("/words/{word_id}")
async def get_words(
        word_id: int = Path(..., title="The ID of word to get"),
        q: Optional[str] = Query(None, alias="word-query")):
    return {
        "_id": "id",
        "content": "ball",
        "meanings": ["qua bong", "trai bong"]
    }
