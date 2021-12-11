from fastapi import APIRouter, Depends, HTTPException, status
from schemas import Token, Login, UserCreate
from pre_start.main import appSetting
from passlib.context import CryptContext
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()


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


async def get_current_user(token):
    print(token)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, appSetting.secret_key, algorithms=['HS256'])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

# async def

async def authenticate_user(email: str, password: str):
    pass

@router.post("/token", response_model=Token)
async def login_for_access_token(body: Login):
    pass

@router.post("/create")
async def create_user(user: UserCreate):
    print(jsonable_encoder(user))
    return {
        "token": create_access_token(jsonable_encoder(user))
    }


@router.post("/login")
def user_login(body: UserCreate):
    admin_collection = appSetting.db.get_collection("words")
    # hash_password = get_password_hash(body.password)
    return admin_collection.find_one({"content": "ball"})
    # return {
    #     "items": w
    # }

@router.get("/me")
async def me(user: UserCreate = Depends(get_current_user)):
    pass
