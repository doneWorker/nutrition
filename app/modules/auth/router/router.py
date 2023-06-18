from datetime import timedelta

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

import config
from app.common.schemas import ApiResponse, APIHttpException
from app.core.database import get_db
from app.modules.auth.utils import get_current_user
from app.modules.users import service as users_service
from app.modules.users.schemas.user import UserCreate, UserSignInOut
from ..schemas.auth import SignUpRequest, SignInRequest, ChangePasswordRequest, TokenData
from ..utils import verify_password, get_password_hash, create_access_token

authRouter = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = config.get_settings().access_token_expire_minutes


@authRouter.post("/auth/sign-in", response_model=ApiResponse)
def sign_in_endpoint(response: Response, request: SignInRequest, db: Session = Depends(get_db)):
    user = users_service.get_user_by_email(request.email, db)

    if not user or not verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return {"success": True, "message": "Successfully signed in!", "data": UserSignInOut.from_orm(user)}


@authRouter.post("/auth/sign-up", response_model=ApiResponse)
def sign_up_endpoint(request: SignUpRequest, response: Response, db: Session = Depends(get_db)):
    # passwords are not equal
    if request.password != request.confirm_password:
        raise HTTPException(status_code=400, detail="Password and confirm password must be the same")

    # email occupied
    if users_service.get_user_by_email(request.email, db):
        raise HTTPException(status_code=400, detail="User with same email is already exists")

    initial_user_data: UserCreate = UserCreate(email=request.email, password=get_password_hash(request.password))
    created_user = users_service.create_user(initial_user_data, db)

    if not created_user:
        raise HTTPException(status_code=400, detail="Something went wrong")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": created_user.email}, expires_delta=access_token_expires
    )

    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return {"success": True, "message": "Successfully signed up!", "data": UserSignInOut.from_orm(created_user)}


@authRouter.post("/auth/sign-out")
def sign_out_endpoint(response: Response):
    response.delete_cookie(key="access_token")
    return {"success": True, "message": "Successfully signed out!"}


@authRouter.post("/auth/change-password", response_model=ApiResponse)
def change_password_endpoint(request: ChangePasswordRequest, db: Session = Depends(get_db),
                             current_user: TokenData = Depends(get_current_user)):
    email = current_user.sub
    user = users_service.get_user_by_email(email, db)

    if user is None or not verify_password(request.old_password, user.password):
        raise APIHttpException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Please re-login")

    updated_hash_password = get_password_hash(request.new_password)
    updated_successfully = users_service.change_user_password(user.id, updated_hash_password, db)

    if not updated_successfully:
        raise APIHttpException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Something went wrong")

    return {"success": True, "message": "Password successfully changed"}


@authRouter.post("/auth/reset-password")
def reset_password_endpoint():
    pass


@authRouter.post("/auth/refresh-access-token")
def refresh_access_token_endpoint(email: str, db: Session = Depends(get_db)):
    pass


@authRouter.post("/auth/verify-email")
def verify_email_endpoint():
    pass


@authRouter.post("/auth/check-email", response_model=bool)
def check_email_endpoint(email: str, db: Session = Depends(get_db)):
    if users_service.get_user_by_email(email, db):
        return True
    return False
