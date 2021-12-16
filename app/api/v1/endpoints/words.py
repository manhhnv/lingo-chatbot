from typing import List
from fastapi import APIRouter, Path, Query, Body, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from pre_start.main import appSetting
from jwt.jwt import JWTBearer
from models.word import WordModel
from schemas import UpdateWord

router = APIRouter()


@router.get("", dependencies=[Depends(JWTBearer())], response_model=List[WordModel])
def get_words(page: int = Query(..., ge=1, description="Pagination")):
    limit = 50
    skip = page * 50
    cursor = appSetting.database.words.find({}).skip(skip).limit(limit)
    words = [word for word in cursor]
    return words


@router.get("/search", dependencies=[Depends(JWTBearer())])
def search_word(key: str = Query(...)):
    cursor = appSetting.database.words.find({"content": {"$regex": key}}, {
                                            "content": 1, "meaning": 1, "imageRoot": 1})
    words = [w for w in cursor]
    return words


@router.put("/{id}", summary="Update word", dependencies=[Depends(JWTBearer())])
def update_word(id: str = Path(...), body: UpdateWord = Body(...)):
    word = appSetting.database.words.find_one({"_id": id})
    if word is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Word not found")
    if not body.content:
        body.content = word["content"]
    if not body.meaning:
        body.meaning = word["meaning"]
    if not body.imageRoot:
        body.imageRoot = word["imageRoot"]
    update_result = appSetting.database.words.update_one(
        {"_id": id}, {"$set": {**body.dict()}})
    if update_result.modified_count != 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return {
        "success": True,
        "message": None
    }
