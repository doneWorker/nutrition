from fastapi import APIRouter

from .service import *

usersRouter = APIRouter()


# Create a product
@usersRouter.post("/user")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)
