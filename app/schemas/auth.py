from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=20)


class CreateUser(UserBase):
    first_name: str = Field(...)
    last_name: str = Field(...)
    is_active: bool = Field(...)


class CreateSuperuser(CreateUser):
    is_superuser: bool = Field(...)

class LoginResponse(BaseModel):
    token: str
