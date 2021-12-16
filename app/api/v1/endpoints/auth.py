from typing import Dict
from fastapi import APIRouter, HTTPException, status, Body, Request
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Depends
from schemas import CreateSuperuser, LoginResponse, UserBase
from pre_start.main import appSetting
from services.auth_service import get_password_hash, verify_password
from jwt.handler import sign_jwt
from jwt.jwt import JWTBearer
from datetime import datetime
from fastapi.security import HTTPBearer

reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)

router = APIRouter()


@router.post("/create-superuser", response_model=LoginResponse)
def create_superuser(body: CreateSuperuser):
    superuser = appSetting.database["admins"].find_one({"is_superuser": True})
    if superuser is None:

        hashed_password = get_password_hash(body.password)
        body.password = hashed_password
        json_encoded = jsonable_encoder(body)
        now = datetime.utcnow()
        json_encoded.update({"last_modified": now})
        result = appSetting.database["admins"].insert_one(json_encoded)

        if result.inserted_id:

            token = sign_jwt(
                {"email": body.email, "is_supperuser": body.is_superuser, "is_active": body.is_active})
        return {"token": token}

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="This operation not allowed")


@router.post("/create-user", dependencies=[Depends(JWTBearer())])
def create_user(body: CreateSuperuser):
    if body.is_superuser == True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="This action cannot be completed")
    user: Dict[str, any] = appSetting.database["admins"].find_one(
        {"$or": [{"email": body.email}, {"is_supperuser": body.is_superuser}]})
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="This email already exist")
    hashed_password = get_password_hash(body.password)
    body.password = hashed_password
    now = datetime.utcnow()
    json_encoded = jsonable_encoder(body)
    json_encoded.update({"last_modified": now})
    result = appSetting.database["admins"].insert_one(json_encoded)

    if result.inserted_id:
        token = sign_jwt(
            {"email": body.email, "is_supperuser": body.is_superuser, "is_active": body.is_active})
        return {"token": token}


@router.post("/login", response_model=LoginResponse)
def login(body: UserBase):
    user: Dict[str, any] = appSetting.database["admins"].find_one(
        {"email": body.email})
    if user is None or user["is_active"] == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email or password is wrong")
    is_valid_password = verify_password(body.password, user["password"])

    if is_valid_password == True:

        token = sign_jwt(
            {"email": body.email, "is_supperuser": user["is_superuser"], "is_active": user["is_active"]})
        return {"token": token}

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Email or password is wrong")


@router.put("/change-password", dependencies=[Depends(JWTBearer())])
def change_password(request: Request, password: str = Body(...)):
    print(request.user_ctx.dict())
    pass
