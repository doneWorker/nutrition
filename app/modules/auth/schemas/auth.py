from pydantic import BaseModel
from pydantic import validator, EmailStr, constr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    sub: str | None = None


class SignInRequest(BaseModel):
    email: EmailStr
    password: str


class ChangePasswordRequest(BaseModel):
    old_password: constr(strip_whitespace=True, min_length=10)
    new_password: constr(strip_whitespace=True, min_length=10)
    confirm_password: str

    @validator('confirm_password')
    def passwords_match(cls, v, values, **kwargs):
        if 'confirm_password' in values and v != values['new_password']:
            raise ValueError('passwords do not match')
        return v


class SignUpRequest(BaseModel):
    email: EmailStr
    password: constr(strip_whitespace=True, min_length=10)
    confirm_password: str

    @validator('password')
    def passwords_match(cls, v, values, **kwargs):
        if 'confirm_password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v
