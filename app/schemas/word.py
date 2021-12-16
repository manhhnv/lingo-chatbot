from typing import Optional
from pydantic import BaseModel


class UpdateWord(BaseModel):
    content: Optional[str] = None
    meaning: Optional[str] = None
    imageRoot: Optional[str] = None
