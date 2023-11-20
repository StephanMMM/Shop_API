import pytest
import time

from starlette.testclient import TestClient
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm.session import close_all_sessions
from sqlalchemy_utils import database_exists, drop_database

from .testdata import add_user_test_data, add_product_test_data, add_test_order_data
from ...src import main, models, database

test_client = TestClient(main.app)

@pytest.fixture(scope="function")
def temp_test_db():
    if database_exists(database.SQLALCHEMY_DATABASE_URL):
        DeleteSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=database.engine)
        db = DeleteSessionLocal()
        db.query(models.Orders).delete()
        db.query(models.Products).delete()
        db.query(models.Users).delete()
        db.commit()
        close_all_sessions()
    database.Base.metadata.create_all(bind=database.engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=database.engine)
    db = TestingSessionLocal()

    def get_db_for_testing():
        add_user_test_data(db)
        add_product_test_data(db)
        add_test_order_data(db)
        try:
            yield db
            db.commit()
        except SQLAlchemyError as e:
            assert e is not None
            db.rollback()

    main.app.dependency_overrides[main.get_db] = get_db_for_testing
    yield db
    db.rollback()
    close_all_sessions()
    database.engine.dispose()

@pytest.fixture
def users_create_data():
    data = {
        "email": "test@example.com",
        "password_plain": "testword123",
        "shipping_address": "Dokoka in Japan, 000-1234"
    }
    return data

@pytest.fixture
def products_create_data():
    data = {
        "title": "Awesome Product",
        "description": "This is a truly amazing product.",
        "price": 123,
        "owner_id": 1
    }
    return data


@pytest.fixture
def products_update_data():
    data = {
        "product_id": 1,
        "title": "Updated Product",
        "description": "This product has been improved.",
        "price": 199,
        "owner_id": 1
    }
    return data


@pytest.fixture
def order_data():
    data = {
        "buyer_id": 2,
        "seller_id": 1,
        "product_id": 1,
        "quantity": 2
    }
    return data
