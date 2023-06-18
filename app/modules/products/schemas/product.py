from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ProductsQuery(BaseModel):
    sort_by: Optional[str] = None
    skip: Optional[int] = 0
    limit: Optional[int] = 50
    name: Optional[str] = None
    min_calories: Optional[float] = None
    min_protein: Optional[float] = None
    min_fat: Optional[float] = None
    min_carbs: Optional[float] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None


class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    brand: Optional[str] = None
    serving_size: Optional[int] = None
    calories: Optional[float] = None
    total_fat: Optional[float] = None
    saturated_fat: Optional[float] = None
    trans_fat: Optional[float] = None
    cholesterol: Optional[float] = None
    sodium: Optional[float] = None
    total_carbohydrates: Optional[float] = None
    dietary_fiber: Optional[float] = None
    sugars: Optional[float] = None
    protein: Optional[float] = None
    vitamin_a: Optional[float] = None
    vitamin_c: Optional[float] = None
    calcium: Optional[float] = None
    iron: Optional[float] = None


class ProductUpdate(BaseModel):
    name: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    brand: Optional[str] = None
    serving_size: Optional[int] = None
    calories: Optional[float] = None
    total_fat: Optional[float] = None
    saturated_fat: Optional[float] = None
    trans_fat: Optional[float] = None
    cholesterol: Optional[float] = None
    sodium: Optional[float] = None
    total_carbohydrates: Optional[float] = None
    dietary_fiber: Optional[float] = None
    sugars: Optional[float] = None
    protein: Optional[float] = None
    vitamin_a: Optional[float] = None
    vitamin_c: Optional[float] = None
    calcium: Optional[float] = None
    iron: Optional[float] = None


class ProductOut(BaseModel):
    class Config:
        orm_mode = True

    id: int
    name: str
    description: Optional[str]
    image_url: Optional[str]
    brand: Optional[str]
    serving_size: Optional[int]
    calories: Optional[float]
    total_fat: Optional[float]
    saturated_fat: Optional[float]
    trans_fat: Optional[float]
    cholesterol: Optional[float]
    sodium: Optional[float]
    total_carbohydrates: Optional[float]
    dietary_fiber: Optional[float]
    sugars: Optional[float]
    protein: Optional[float]
    vitamin_a: Optional[float]
    vitamin_c: Optional[float]
    calcium: Optional[float]
    iron: Optional[float]
    date_created: Optional[datetime]
    date_updated: Optional[datetime]
