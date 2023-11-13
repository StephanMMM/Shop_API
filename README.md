# Shop_API
Language: Python

Framework: FastAPI

Database: MySQL

## Requirements
- apt-get install docker
## How To
docker network create shop-network

docker compose up --build -d

API Documentation: http://127.0.0.1/docs

## Database 
### Classes and Attributes
- User (email_address, password_hash, shipping_address, points, exhibit(List(Products)))
- Product (id, title, description, price)
- PurchaseHistory (purchase_id, List(product, quantity, date))