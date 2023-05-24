from pydantic import BaseModel


class UserCreate(BaseModel):
    nickname: str
    first_name: str
    last_name: str
    email: str
    password: str
    is_verified: bool
    auth_type: str


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
