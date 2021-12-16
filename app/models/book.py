from pydantic import BaseModel
from typing import Optional


class BookModel(BaseModel):
    _id: Optional[str] = None
    description: Optional[str] = None
    cover: Optional[str] = None
    grade: Optional[int] = None
    name: Optional[str] = None
