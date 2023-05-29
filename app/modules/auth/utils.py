from datetime import datetime
from datetime import timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext

import config
from app.modules.auth.schemas.auth import TokenData

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/token')
SECRET_KEY = config.get_settings().secret_key
ALGORITHM = config.get_settings().algorithm


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Couldn't validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})

    return get_token_data(token, credentials_exception)


def get_token_data(token, credential_exception):
    try:
        payload: dict = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credential_exception
        token_data = TokenData(sub=email)
    except JWTError:
        raise credential_exception

    return token_data


def verify_password(plain_password, hashed_password):
    try:
        is_verified = pwd_context.verify(plain_password, hashed_password)
    except ValueError or TypeError:
        return False

    return is_verified


def get_password_hash(password):
    return pwd_context.hash(password)
