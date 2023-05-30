from datetime import datetime

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from .models.user import User
from .schemas.user import UserCreate


def get_user(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email, User.password == password).first()
    return user


def get_user_by_email(email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    return user


def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(user.email, db):
        raise Exception("User already exists")

    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def change_user_password(user_id: str, new_password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise Exception("User not found")

    user.password = new_password
    user.date_updated = datetime.now()
    db.commit()

    return True


def update_user(db):
    pass


def delete_user(db):
    pass
