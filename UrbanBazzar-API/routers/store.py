from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.store import crud, schemas
from models.database import get_db
from fastapi import Request
from app.store import models 
from app.store.models import *
from typing import List

router = APIRouter()


# --------- Product Category Routes ----------

@router.post("/categories/", response_model=schemas.ProductCategoryResponse)
def create_category(category: schemas.ProductCategoryCreate, db: Session = Depends(get_db)):
    return crud.create_product_category(db=db, category=category)


@router.get("/categories/", response_model=list[schemas.ProductCategoryResponse])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_product_categories(db=db, skip=skip, limit=limit)


@router.get("/categories/{category_id}", response_model=schemas.ProductCategoryResponse)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_product_category(db=db, category_id=category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


# --------- Product Routes ----------

@router.post("/products/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@router.get("/products/", response_model=List[schemas.ProductResponse])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), request: Request = None):
    products = db.query(Product).offset(skip).limit(limit).all()

    response = []
    for product in products:
        product_images = [
            schemas.ProductImageResponse(
                id=image.id,
                product_id=image.product_id,
                image=image.image,
                url = str(request.base_url) + "media/" + image.image.lstrip("/")
            )
            for image in product.product_images
        ]

        product_data = schemas.ProductResponse(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            brand_name=product.brand_name,
            category_id=product.product_category_id, 
            stock=product.stock,
            created_at=product.created_at,
            updated_at=product.updated_at,
            product_images=product_images
        )
        response.append(product_data)

    return response

@router.get("/products/{product_id}", response_model=schemas.ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db=db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


# --------- Product Image Routes ----------

@router.post("/products/{product_id}/images/", response_model=schemas.ProductImageResponse)
def add_image(product_id: int, image: schemas.ProductImageCreate, db: Session = Depends(get_db)):
    return crud.add_product_image(db=db, product_id=product_id, image=image)


# --------- TryOn Image Routes ----------

@router.post("/products/{product_id}/tryon-images/", response_model=schemas.TryOnImageResponse)
def add_tryon_image(product_id: int, image: schemas.TryOnImageCreate, db: Session = Depends(get_db)):
    return crud.add_tryon_image(db=db, product_id=product_id, image=image)
