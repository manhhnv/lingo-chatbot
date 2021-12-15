from typing import List, Optional
from fastapi import APIRouter, Path, Query
from fastapi.param_functions import Depends
from pre_start.main import appSetting
from jwt.jwt import JWTBearer
from models.word import WordModel

router = APIRouter()


@router.get("", dependencies=[Depends(JWTBearer())], response_model=List[WordModel])
def get_words(page: int = Query(..., ge=1, description="Pagination")):
    limit = 50
    skip = page * 50
    cursor = appSetting.database.words.find({}).skip(skip).limit(limit)
    words = [word for word in cursor]
    return words

@router.get("/search", dependencies=[Depends(JWTBearer())], response_model=List[WordModel])
def search_word(key: str = Query(...)):
    pass
