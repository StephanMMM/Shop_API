import json

from pytest
from sqlalchemy import text
from Shop_API.app.src import database

database.Base.metadata.create_all(bind=database.engine)
@pytest.fixture
def db_fixture(db):
    db = database.SessionLocal()
    session = db()

    users_data = [
        (1, "johndoe@example.com", "password123", "123 Main Street, Anytown, CA 94538", 0),
        (2, "janedoe@example.com", "password456", "456 Elm Street, Anytown, CA 94538", 0),
        (3, "peterjones@example.com", "password789", "789 Oak Street, Anytown, CA 94538", 0),
        (4, "marygreen@example.com", "password101", "101 Maple Street, Anytown, CA 94538", 0),
        (5, "alexsmith@example.com", "password12345", "12345 Pine Street, Anytown, CA 94538", 0),
    ]

    insert_users_stmt = text("""
    INSERT INTO users (user_id, email, password_hash, shipping_address, points)
    VALUES (:user_id, :email, :password_hash, :shipping_address, :points)
    """)

    session.execute(insert_users_stmt, users_data)

    # Insert data into Products table
    products_data = [
        (1, "Laptop",
         "A powerful laptop for all your needs, featuring a sleek design, long-lasting battery, and cutting-edge technology.",
         1200, 1),
        (2, "Smartphone",
         "A sleek and stylish smartphone with a high-resolution display, powerful processor, and advanced camera system.",
         600, 2),
        (3, "TV",
         "A large and vibrant TV for your home theater experience, offering stunning 4K resolution, immersive sound, and smart features.",
         800, 3),
        (4, "Headphones",
         "Noise-canceling headphones for immersive listening, providing exceptional sound quality, comfortable fit, and long-lasting battery life.",
         200, 4),
        (5, "Books",
         "A collection of classic novels, including The Great Gatsby, To Kill a Mockingbird, and Pride and Prejudice.",
         50, 5),
    ]

    insert_products_stmt = text("""
    INSERT INTO products (product_id, title, description, price, owner_id)
    VALUES (:product_id, :title, :description, :price, :owner_id)
    """)

    session.execute(insert_products_stmt, products_data)

    # Insert data into Orders table
    orders_data = [
        (1, 1, 2, 1, 1, "2023-11-15"),
        (2, 2, 3, 2, 1, "2023-11-16"),
        (3, 3, 4, 3, 1, "2023-11-17"),
        (4, 4, 5, 4, 1, "2023-11-16"),
        (5, 5, 1, 5, 1, "2023-11-17"),
    ]

    insert_orders_stmt = text("""
    INSERT INTO orders (order_id, buyer_id, seller_id, product_id, quantity, date)
    VALUES (:order_id, :buyer_id, :seller_id, :product_id, :quantity, :date)
    """)

    session.execute(insert_orders_stmt, orders_data)
    session.flush()
    session.commit()
    session.refresh()
    try:
        yield session
    finally:
        session.rollback()
        session.close()

@pytest.fixture
def users_create_data():
    data = {
        "email": "test@example.com",
        "password_plain": "testword123",
        "shipping_address": "Dokoka in Japan, 000-1234"
    }
    return json.dumps(data)

@pytest.fixture
def products_create_data():
    data = {
        "title": "Awesome Product",
        "description": "This is a truly amazing product.",
        "price": 123,
        "owner_id": 1
    }
    return json.dumps(data)

@pytest.fixture
def products_update_data():
    data = {
        "product_id": 6,
        "title": "Updated Product",
        "description": "This product has been improved.",
        "price": 199,
        "owner_id": 1
    }
    return json.dumps(data)

@pytest.fixture
def order_data():
    data = {
        "buyer_id": 1,
        "seller_id": 2,
        "product_id": 6,
        "quantity": 2
    }
    return json.dumps(data)