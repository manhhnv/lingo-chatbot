from pre_start.main import appSetting
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, appSetting.secret_key, algorithm='HS256')
    return encoded_jwt


async def find_by_email(email: str):
    admin_collection = appSetting.db.get_collection("admins")
    user = await admin_collection.find_one({"email": email})
    return user
