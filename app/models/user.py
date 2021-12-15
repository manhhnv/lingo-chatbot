from typing import Optional
from pydantic import BaseModel
from bson.objectid import ObjectId
from datetime import datetime


class UserModel(BaseModel):
    _id: Optional[ObjectId] = None
    email: Optional[str] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    last_modified: Optional[datetime] = None
