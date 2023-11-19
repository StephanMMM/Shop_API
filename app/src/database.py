import os
import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

_USERNAME = os.environ["MYSQL_USER"]
_PASSWORD = os.environ["MYSQL_PASSWORD"]
_DATABASE = os.environ["MYSQL_DATABASE"]
_HOST = os.environ["MYSQL_HOSTNAME"]
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{_USERNAME}:{_PASSWORD}@{_DATABASE}:3306/{_HOST}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
