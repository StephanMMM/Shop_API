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

class ProductUpdate(BaseModel):
    product_id: int
    title: str | None = None
    description: str | None = None
    price: int | None = None
    owner_id: int | None = None

class ProductDelete(BaseModel):
    product_id: int

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

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    user_id: int
    email: str | None = None
    points: int | None = None
    shipping_address: str | None = None

### Order Models ###
class OrderBase(BaseModel):
    buyer_id: int
    seller_id: int
    product_id: int
    quantity: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    order_id: str
    date: datetime
    class Config:
        orm_mode = True