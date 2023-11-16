import os
import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_USERNAME = os.environ["MYSQL_USER"]
_PASSWORD = os.environ["MYSQL_PASSWORD"]
_DATABASE = os.environ["MYSQL_DATABASE"]
_HOST = os.environ["MYSQL_HOSTNAME"]
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{_USERNAME}:{_PASSWORD}@{_DATABASE}:3306/{_HOST}"
time.sleep(15)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
