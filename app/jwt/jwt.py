from typing import Optional
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr

from .handler import decode_jwt


class JwtClaims(BaseModel):
    email: EmailStr
    is_supperuser: Optional[bool] = False
    is_active: Optional[bool] = False


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication scheme")
            payload = self.verify_jwt(credentials.credentials)
            if payload is None:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token or expired token.")
            request.user_ctx = payload
        return await super().__call__(request)

    def verify_jwt(self, jwt_token: str) -> JwtClaims:
        try:
            payload: JwtClaims = decode_jwt(jwt_token)
        except:
            payload = None
        return JwtClaims(**payload)
