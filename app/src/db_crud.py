import sqlalchemy
import logging
import sys
import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from . import models, encrypt, schemas

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))

def create_user(user: schemas.UserCreate, db: Session):
    try:
        if not user.email or not user.password_plain:
            raise ValueError("Email and Password are required for registration.")
        if db.query(models.Users).filter(models.Users.email == user.email).count() > 0:
            raise ValueError("Email duplicates are not allowed.")
    except ValueError as e:
        logger.error(e)
    starting_points = 10000
    password_hash = encrypt.encrypt_password(user.password_plain)
    new_user = models.Users(email=user.email,
                           password_hash=password_hash,
                           shipping_address=user.shipping_address,
                           points=starting_points)
    db.add(new_user)
    try:
        db.flush()
        db.commit()
    except IntegrityError as e:
        logger.error(e)
        db.rollback()
    db.refresh(new_user)
    return new_user

def create_product(product: schemas.ProductCreate, db: Session):
    try:
        if not product.title:
            raise ValueError("Title is required for products.")
        if not product.price:
            raise ValueError("Price is required for products.")
        if not product.owner_id:
            raise ValueError("Owner(User) is required for products.")
        user = db.query(models.Users).get(product.owner_id)
        if user is None:
            raise KeyError("Owner ID does not exist.")
    except ValueError as e:
        logger.error(e)
    except KeyError as e:
        logger.error(e)
    new_product = models.Products(title=product.title,
                                  description=product.description,
                                  price=product.price,
                                  owner_id=product.owner_id)
    db.add(new_product)
    try:
        db.flush()
        db.commit()
    except IntegrityError as e:
        logger.error(e)
        db.rollback()
    db.refresh(new_product)
    return new_product

def update_product(product: schemas.ProductUpdate, db: Session):
    try:
        existing_product = db.query(models.Products).get(product.product_id)
        if existing_product is None:
            raise KeyError("Product does not exist.")
    except KeyError as e:
        logger.error(e)
    for field in product.__dict__:
        if product.__dict__[field] is not None:
            setattr(existing_product, field, product.__dict__[field])
    try:
        db.flush()
        db.commit()
    except IntegrityError as e:
        logger.error(e)
        db.rollback()
    db.refresh(existing_product)
    return existing_product

def delete_product(product_id: int, db: Session):
    try:
        deletion_product = db.query(models.Products).get(product_id)
        if deletion_product is None:
            raise KeyError("Product does not exist.")
        db.delete(deletion_product)
        db.flush()
        db.commit()
    except KeyError as e:
        logger.error(e)
    except IntegrityError as e:
        logger.error(e)
        db.rollback()
    return deletion_product

def create_order(order: schemas.OrderCreate, db: Session):
    try:
        seller = db.query(models.Users).get(order.seller_id)
        if seller is None:
            raise ValueError("Seller does not exist.")
        buyer = db.query(models.Users).get(order.buyer_id)
        if buyer is None:
            raise ValueError("Buyer does not exist.")
        product = db.query(models.Products).get(order.product_id)
        if product is None:
            raise ValueError("Product does not exist.")
        if product.owner_id != order.seller_id:
            raise ValueError("Product does not belong to the seller.")
        if buyer.points - product.price * order.quantity < 0:
            raise ValueError("Buyer does not have enough points.")

    except ValueError as e:
        logger.error(e)
    new_order = models.Orders(seller_id=order.seller_id,
                              buyer_id=order.buyer_id,
                              product_id=order.product_id,
                              quantity=order.quantity,
                              date=datetime.datetime.now())
    updated_buyer = update_user(models.Users(user_id=buyer.user_id,
                                             points=(buyer.points-(order.quantity*product.price))),
                                db)
    updated_seller = update_user(models.Users(user_id=seller.user_id,
                                              points=(seller.points + (order.quantity * product.price))),
                                 db)
    db.add(new_order,
           updated_buyer,
           updated_seller)
    try:
        db.flush()
        db.commit()
    except IntegrityError as e:
        logger.error(e)
        db.rollback()
    db.refresh(new_order)
    return new_order

def update_user(user: schemas.UserUpdate, db: Session):
    try:
        existing_user = db.query(models.Users).get(user.user_id)
        if existing_user is None:
            raise KeyError("Product does not exist.")
    except KeyError as e:
        logger.error(e)
    for field in user.__dict__:
        if user.__dict__[field] is not None:
            setattr(existing_user, field, user.__dict__[field])
    try:
        db.flush()
        db.commit()
    except IntegrityError as e:
        logger.error(e)
        db.rollback()
    db.refresh(existing_user)
    return existing_user
