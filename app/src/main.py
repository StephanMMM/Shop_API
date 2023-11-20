import time

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import db_crud, schemas, database

time.sleep(15)
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/create", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = db_crud.create_user(user, db)
    return new_user

@app.post("/products/create", response_model=schemas.Product)
async def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    new_product = db_crud.create_product(product, db)
    return new_product

@app.put("/products/update", response_model=schemas.Product)
async def update_product(product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    updated_product = db_crud.update_product(product, db)
    return updated_product

@app.delete("/products/delete", response_model=schemas.Product)
async def delete_product(product: schemas.ProductDelete, db: Session = Depends(get_db)):
    db_crud.delete_product(product, db)
    return

@app.post("/order", response_model=schemas.Order)
async def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    new_order = db_crud.create_order(order, db)
    return new_order
