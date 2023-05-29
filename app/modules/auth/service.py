from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db


def get_user(email: str, password: str, db: Session = Depends(get_db)):
    pass
