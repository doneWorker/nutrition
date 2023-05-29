from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import config
from app.core.database import get_db
from app.modules.users import service as users_service
from app.modules.users.schemas.user import UserCreate
from ..schemas.auth import SignUpRequest, Token
from ..utils import verify_password, get_password_hash, create_access_token

authRouter = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = config.get_settings().access_token_expire_minutes


@authRouter.post("/auth/sign-in", response_model=Token)
def sign_in_endpoint(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = users_service.get_user_by_email(request.username, db)

    if user is None or not verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@authRouter.post("/auth/sign-up")
def sign_up_endpoint(request: SignUpRequest, db: Session = Depends(get_db)):
    # passwords are not equal
    if request.password != request.confirm_password:
        raise HTTPException(status_code=400, detail="Password and confirm password must be the same")

    # email occupied
    if users_service.get_user_by_email(request.email, db):
        raise HTTPException(status_code=400, detail="User with same email is already exists")

    initial_user_data: UserCreate = UserCreate(email=request.email, password=get_password_hash(request.password), )
    return users_service.create_user(initial_user_data, db)


@authRouter.post("/auth/sign-out")
def sign_out_endpoint():
    pass


@authRouter.post("/auth/reset-password")
def reset_password_endpoint():
    pass


@authRouter.post("/auth/refresh-access-token")
def refresh_access_token_endpoint(email: str, db: Session = Depends(get_db)):
    users_service.get_user_by_email(email, db)


@authRouter.post("/auth/change-password")
def change_password_endpoint():
    pass


@authRouter.post("/auth/verify-email")
def verify_email_endpoint():
    pass


@authRouter.post("/auth/check-email", response_model=bool)
def check_email_endpoint(email: str, db: Session = Depends(get_db)):
    if users_service.get_user_by_email(email, db):
        return True
    return False
