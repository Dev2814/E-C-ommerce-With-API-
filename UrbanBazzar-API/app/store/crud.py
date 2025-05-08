from sqlalchemy.orm import Session
from app.store import models, schemas


# --------- Product Category CRUD ----------

# Create a new product category in the database
def create_product_category(db: Session, category: schemas.ProductCategoryCreate):
    db_category = models.ProductCategory(**category.dict())  # Convert schema to model instance
    db.add(db_category)     # Add to session
    db.commit()             # Commit transaction
    db.refresh(db_category) # Refresh instance with DB-generated values (e.g., id)
    return db_category

# Retrieve a list of product categories with optional pagination
def get_product_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProductCategory).offset(skip).limit(limit).all()

# Retrieve a single product category by its ID
def get_product_category(db: Session, category_id: int):
    return db.query(models.ProductCategory).filter(models.ProductCategory.id == category_id).first()


# --------- Product CRUD ----------

# Create a new product in the database
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())  # Convert schema to model instance
    db.add(db_product)     # Add to session
    db.commit()            # Commit transaction
    db.refresh(db_product) # Refresh instance with DB-generated values (e.g., id)
    return db_product

# Retrieve a list of products with optional pagination
def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

# Retrieve a single product by its ID
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


# --------- Product Image CRUD ----------

# Add a new image to an existing product
def add_product_image(db: Session, product_id: int, image: schemas.ProductImageCreate):
    db_image = models.ProductImage(product_id=product_id, **image.dict())  # Create image linked to product
    db.add(db_image)     # Add to session
    db.commit()          # Commit transaction
    db.refresh(db_image) # Refresh with DB-generated values
    return db_image


# --------- TryOn Image CRUD ----------

# Add a try-on image (e.g., for AR feature) to a product
def add_tryon_image(db: Session, product_id: int, image: schemas.TryOnImageCreate):
    db_image = models.TryOnImage(product_id=product_id, **image.dict())  # Create try-on image entry
    db.add(db_image)     # Add to session
    db.commit()          # Commit transaction
    db.refresh(db_image) # Refresh with DB-generated values
    return db_image
