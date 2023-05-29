from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from .models.user import User
from .schemas.user import UserCreate


def get_user(email: str, password: str, db: Session = Depends(get_db)):
    users = db.query(User).filter(User.email == email, User.password == password).first()
    return users


def get_user_by_email(email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    return user


def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db):
    pass


def delete_user(db):
    pass
