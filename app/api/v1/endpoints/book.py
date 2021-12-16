from fastapi import APIRouter
from fastapi import Path
from fastapi.param_functions import Depends
from models.book import BookModel
from typing import List
from pre_start.main import appSetting

from jwt.jwt import JWTBearer

router = APIRouter(dependencies=[Depends(JWTBearer())])


@router.get("/{grade}", response_model=List[BookModel])
def get_books(grade: int = Path(..., ge=1, le=12)):
    cursor = appSetting.database.get_collection("books").find({"grade": grade})
    books = [book for book in cursor]
    return books
