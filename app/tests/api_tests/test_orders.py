from fastapi import status
from ..fixtures.fixtures import (test_client,
                                 order_data,
                                 temp_test_db)
from ...src.schemas import OrderCreate

def test_create_order(order_data: OrderCreate, temp_test_db):
    response = test_client.post("/order", json=order_data)
    response_data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_data["buyer_id"] == order_data["buyer_id"]
    assert response_data["seller_id"] == order_data["seller_id"]
    assert response_data["product_id"] == order_data["product_id"]
    assert response_data["quantity"] == order_data["quantity"]
    assert response_data["order_id"] == order_data["order_id"]
    assert response_data["date"] == order_data["date"]
