from typing import List
from pydantic import BaseModel
from datetime import datetime


### Product Models ###
class ProductBase(BaseModel):
    title: str
    description: str | None = None
    price: int
    owner_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    product_id: int

    class Config:
        orm_mode = True

class ProductUpdate(Product):
    pass

### User Models ###
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password_plain: str
    shipping_address: str | None = None

class User(UserBase):
    user_id: int
    points: int
    shipping_address: str | None = None
    exhibits: List[Product | None] = None

    class Config:
        orm_mode = True


### Order Models ###
class OrderBase(BaseModel):
    order_id: str
    buyer_id: int
    seller_id: int
    product_id: int
    quantity: int
    date: datetime

class Order(OrderBase):
    class Config:
        orm_mode = True