# Shop API

This is a Python-based application using the FastAPI framework and MySQL as a database.
Language and Framework

    Language: Python
    Framework: FastAPI
    Database: MySQL

## Requirements

Before proceeding, ensure you have Docker installed on your system. If not, you can install it using the following command:

    apt-get install docker

## Usage

To use the application, first, create a Docker network:
(sudo is not required for the next commands but it enables a quick setup without worrying about permissions.)
    
    sudo docker network create shop_network

Then, start the application using Docker Compose:

    sudo docker compose up --build -d

Once the API container is running, you can access the interactive documentation at http://127.0.0.1/docs.

To run the test container using Docker Compose:

    sudo docker compose -f docker-compose.test.yml up --build -d

When running the tests above more than once, reset the database volume in between the runs like:

    sudo docker compose -f docker-compose.test.yml down
    sudo docker volume rm shop_api_shop-test-mysql
    sudo docker compose -f docker-compose.test.yml up --build -d
    
## Database

The application uses the following classes with their respective attributes:

    User: user_id, email, password_hash, shipping_address, points
    Product: product_id, title, description, price, owner_id
    Orders: order_id, buyer_id, seller_id, product_id, quantity, date

Each of these classes corresponds to a table in the MySQL database. The attributes of each class correspond to columns in the respective table.