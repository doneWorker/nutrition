from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str
    nickname: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_verified: Optional[bool] = False
    auth_type: Optional[str] = "internal"


class UserUpdate(BaseModel):
    nickname: str
    first_name: str
    last_name: str
    email: str
    password: str
    is_verified: bool
    auth_type: str


class UserInDB(UserCreate):
    id: int
    date_created: str
    date_updated: str


class User(UserInDB):
    pass
