from fastapi import APIRouter
from schemas import Token, Login

router = APIRouter()


@router.post("/login", response_model=Token)
def user_login(body: Login):
    return {
        "access_token": "access_token",
        "token_type": "bearer"
    }
