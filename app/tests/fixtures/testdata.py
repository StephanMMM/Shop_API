from ...src.models import Users, Products, Orders


def add_user_test_data(db):
    test_user_data = [
        Users(user_id=1, email="johndoe@example.com", password_hash="password123", shipping_address="123 Main Street, Anytown, CA 94538", points=10000),
        Users(user_id=2, email="janedoe@example.com", password_hash="password456", shipping_address="456 Elm Street, Anytown, CA 94538", points=10000),
        Users(user_id=3, email="peterjones@example.com", password_hash="password789", shipping_address="789 Oak Street, Anytown, CA 94538", points=10000),
        Users(user_id=4, email="marygreen@example.com", password_hash="password101", shipping_address="101 Maple Street, Anytown, CA 94538", points=10000),
        Users(user_id=5, email="alexsmith@example.com", password_hash="password12345", shipping_address="12345 Pine Street, Anytown, CA 94538", points=10000),
    ]
    db.bulk_save_objects(test_user_data)


def add_product_test_data(db):
    test_product_data = [
        Products(product_id=1, title="Laptop",
                 description="A powerful laptop for all your needs, featuring a sleek design, long-lasting battery, and cutting-edge technology.",
                 price=1200, owner_id=1),
        Products(product_id=2, title="Smartphone",
                 description="A sleek and stylish smartphone with a high-resolution display, powerful processor, and advanced camera system.",
                 price=600, owner_id=2),
        Products(product_id=3, title="TV",
                 description="A large and vibrant TV for your home theater experience, offering stunning 4K resolution, immersive sound, and smart features.",
                 price=800, owner_id=3),
        Products(product_id=4, title="Headphones",
                 description="Noise-canceling headphones for immersive listening, providing exceptional sound quality, comfortable fit, and long-lasting battery life.",
                 price=200, owner_id=4),
        Products(product_id=5, title="Books",
                 description="A collection of classic novels, including The Great Gatsby, To Kill a Mockingbird, and Pride and Prejudice.",
                 price=50, owner_id=5)
    ]
    db.bulk_save_objects(test_product_data)


def add_test_order_data(db):
    test_order_data = [
        Orders(order_id=1, buyer_id=1, seller_id=2, product_id=1, quantity=1, date="2023-11-15"),
        Orders(order_id=2, buyer_id=2, seller_id=3, product_id=2, quantity=1, date="2023-11-16"),
        Orders(order_id=3, buyer_id=3, seller_id=4, product_id=3, quantity=1, date="2023-11-17"),
        Orders(order_id=4, buyer_id=4, seller_id=5, product_id=4, quantity=1, date="2023-11-16"),
        Orders(order_id=5, buyer_id=5, seller_id=1, product_id=5, quantity=1, date="2023-11-17"),
    ]
    db.bulk_save_objects(test_order_data)
