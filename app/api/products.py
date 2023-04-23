from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.product import Product, ProductCreate, ProductUpdate

router = APIRouter()


# Product schema
class ProductOut(BaseModel):
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
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


# Create a product
@router.post("/products", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# Get all products
@router.get("/products", response_model=List[ProductOut])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products


# Get a single product
@router.get("/products/{product_id}", response_model=ProductOut)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# Update a product
@router.put("/products/{product_id}", response_model=ProductOut)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for var, value in vars(product).items():
        if value is not None:
            setattr(db_product, var, value)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# Delete a product
@router.delete("/products/{product_id}", response_model=ProductOut)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return product
