import random

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from .models.product import Product
from .schemas.product import ProductsQuery, ProductOut, ProductCreate, ProductUpdate


def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    return product


def get_products(query: ProductsQuery, db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.image_url != None).offset(query.skip).limit(query.limit).all()

    output = [dict(ProductOut.from_orm(product)) for product in products]

    for product in output:
        product['price'] = random.randint(1, 100)

    return output


def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(product)
    db.commit()
    db.refresh(db_product)

    return db_product


def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()

    for var, value in vars(product).items():
        if value is not None:
            setattr(db_product, var, value)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

# TODO: complete method
# def archive_product(product_id, db: Session = Depends(get_db)):
#     db_product = Product(**product.dict())
#     db.add(product)
#     db.commit()
#     db.refresh(db_product)
#     return db_product
