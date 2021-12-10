from fastapi import APIRouter
from schemas import Token

router = APIRouter()


@router.post("/login", response_model=Token)
def login():
    return {
        "access_token": "access_token",
        "token_type": "bearer"
    }
