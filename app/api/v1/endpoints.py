from fastapi import APIRouter

from app.modules.auth.router.router import authRouter
from app.modules.users.router.router import usersRouter

router = APIRouter()

router.include_router(usersRouter, tags=["users"])
router.include_router(authRouter, tags=["auth"])
