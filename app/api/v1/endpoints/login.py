from fastapi import APIRouter
from schemas import Token, Login, UserCreate
from pre_start.main import appSetting
from passlib.context import CryptContext
from fastapi.encoders import jsonable_encoder

router = APIRouter()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


@router.post("/create")
async def create_user(user: UserCreate):
    pass

@router.post("/login")
async def user_login(body: Login):
    admin_collection = appSetting.db.get_collection("admins")
    hash_password = get_password_hash(body.password)
    await admin_collection.insert_one({"username": body.username, "password": "abc"})
    return {
        "items": ''
    }
