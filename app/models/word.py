from typing import List, Optional
from pydantic import BaseModel


class WordModel(BaseModel):
    _id: Optional[str] = None
    meanings: Optional[List[str]] = []
    pronunciations: Optional[List[str]] = []
    types: Optional[List[str]] = []
    bookNId: Optional[int] = None
    unitNId: Optional[int] = None
    content: Optional[str] = None
    meaning: Optional[str] = None
    imageRoot: Optional[str] = None
