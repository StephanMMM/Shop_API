from sqlalchemy.orm import Session
from . import models, encrypt, schemas


def create_user(user: schemas.UserCreate, db: Session):
    starting_points = 10000
    password_hash = encrypt.encrypt_password(user.password_plain)
    db_user = models.User(email=user.email,
                          password_hash=password_hash,
                          shipping_address=user.shipping_address,
                          points=starting_points)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

