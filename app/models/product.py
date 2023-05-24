from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime

from app.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(255), nullable=True)
    image_url = Column(String(255), nullable=True)
    brand = Column(String(50), nullable=True)
    serving_size = Column(Integer, nullable=True)
    calories = Column(Float, nullable=True)
    total_fat = Column(Float, nullable=True)
    saturated_fat = Column(Float, nullable=True)
    trans_fat = Column(Float, nullable=True)
    cholesterol = Column(Float, nullable=True)
    sodium = Column(Float, nullable=True)
    total_carbohydrates = Column(Float, nullable=True)
    dietary_fiber = Column(Float, nullable=True)
    sugars = Column(Float, nullable=True)
    protein = Column(Float, nullable=True)
    vitamin_a = Column(Float, nullable=True)
    vitamin_c = Column(Float, nullable=True)
    calcium = Column(Float, nullable=True)
    iron = Column(Float, nullable=True)
    date_created = Column(DateTime, default=datetime.utcnow)
    date_updated = Column(DateTime, default=datetime.utcnow)
