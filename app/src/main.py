from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import db_crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

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

@app.post("/users/exhibits/create", response_model=schemas.User)
async def create_exhibit(user_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return {}

@app.put("/users/exhibits/update", response_model=schemas.User)
async def update_exhibit(user_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    return {}

@app.delete("/users/exhibits/delete", response_model=schemas.User)
async def delete_exhibit(user_id: int, product_id: int, db: Session = Depends(get_db)):
    return {}

@app.post("/transaction", response_model=schemas.Order)
async def create_transaction(seller_id: int, buyer_id: int, product_id: int, quantity: int, db: Session = Depends(get_db)):
    return {}
