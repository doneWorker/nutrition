from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP

from app.core.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    is_verified = Column(Boolean)
    auth_type = Column(String(50))
    date_created = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', nullable=False)
    date_updated = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate=True, nullable=False)
