from __future__ import annotations

from pydantic import BaseModel, Field


class Nutriments(BaseModel):
    energy_value: int = Field(..., alias='energy-kcal')
    carbohydrates: int
    fat_value: int
    proteins_value: int


class OFFProduct(BaseModel):
    id: str
    product_name: str
    product_name_en: str
    categories: str
    nutriments: Nutriments
