from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.schemas import ApiResponse
from app.core.database import get_db
from app.modules.products import service as products_service
from app.modules.products.schemas.product import ProductsQuery
from app.schemas.product import ProductCreate, ProductUpdate

productsRouter = APIRouter()


# Create a product
@productsRouter.post("/products", response_model=ApiResponse)
def create_product_endpoint(product: ProductCreate, db: Session = Depends(get_db)):
    created_product = products_service.create_product(product, db)

    return {"success": True, "data": created_product}


# Get all products
@productsRouter.get("/products", response_model=ApiResponse)
def read_products_endpoint(query: ProductsQuery = Depends(), db: Session = Depends(get_db)):
    products = products_service.get_products(query, db)

    return {"success": True, "data": products}


# Get a single product
@productsRouter.get("/products/{product_id}", response_model=ApiResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = products_service.get_product(product_id, db)

    return {"success": True, "data": product}


# Update a product
@productsRouter.put("/products/{product_id}", response_model=ApiResponse)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    updated_product = products_service.update_product(product_id, product, db)

    return {"success": True, "data": updated_product}

# TODO: complete Delete a product
# @productsRouter.delete("/products/{product_id}", response_model=ProductOut)
# def delete_product(product_id: int, db: Session = Depends(get_db)):
#     product = db.query(Product).filter(Product.id == product_id).first()
#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found")
#     db.delete(product)
#     db.commit()
#     return product
