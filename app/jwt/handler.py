from typing import Optional
from datetime import datetime, timedelta
from pre_start.main import appSetting
from jose import jwt
import time


def sign_jwt(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, appSetting.secret_key, algorithm="HS256")
    return encoded_jwt


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token, appSetting.secret_key, algorithms=["HS256"])
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except:
        return {}
