from fastapi import APIRouter

from app.modules.auth.utils import get_current_user
from ..service import *

usersRouter = APIRouter()


@usersRouter.post("/user")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db),
                         current_user: str = Depends(get_current_user)):
    return create_user(user, db)


@usersRouter.get("/users")
def get_all_users_endpoint(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_all_users(db)
