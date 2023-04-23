from typing import Optional
from datetime import datetime
from pydantic import BaseModel



class Product:
    def __init__(
        self,
        id: int,
        name: str,
        description: Optional[str] = None,
        image_url: Optional[str] = None,
        brand: Optional[str] = None,
        serving_size: Optional[int] = None,
        calories: Optional[float] = None,
        total_fat: Optional[float] = None,
        saturated_fat: Optional[float] = None,
        trans_fat: Optional[float] = None,
        cholesterol: Optional[float] = None,
        sodium: Optional[float] = None,
        total_carbohydrates: Optional[float] = None,
        dietary_fiber: Optional[float] = None,
        sugars: Optional[float] = None,
        protein: Optional[float] = None,
        vitamin_a: Optional[float] = None,
        vitamin_c: Optional[float] = None,
        calcium: Optional[float] = None,
        iron: Optional[float] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.image_url = image_url
        self.brand = brand
        self.serving_size = serving_size
        self.calories = calories
        self.total_fat = total_fat
        self.saturated_fat = saturated_fat
        self.trans_fat = trans_fat
        self.cholesterol = cholesterol
        self.sodium = sodium
        self.total_carbohydrates = total_carbohydrates
        self.dietary_fiber = dietary_fiber
        self.sugars = sugars
        self.protein = protein
        self.vitamin_a = vitamin_a
        self.vitamin_c = vitamin_c
        self.calcium = calcium
        self.iron = iron
        self.created_at = created_at
        self.updated_at = updated_at


from typing import Optional
from pydantic import BaseModel

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

from typing import Optional
from pydantic import BaseModel

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
