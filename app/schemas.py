from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    # to read a data even it isn't a dict
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    # all information about user which we allow into UserOut schema
    owner: UserOut

    # to read a data even it isn't a dict
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


# schema for data which we embedded into access_token
class TokenData(BaseModel):
    id: Optional[str] = None
