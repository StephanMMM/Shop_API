import pytest
from fastapi import status, FastAPI
from starlette.testclient import TestClient
from Shop_API.app.tests.fixtures.fixtures import (db_fixture,
                                                  order_data)
app = FastAPI()
test_client = TestClient(app)


@pytest.mark.usefixtures("db_fixture", "order_data")
def test_create_transaction():
    with db_fixture as db:
        response = test_client.post("/order",
                                    json=order_data,
        )
        assert response.status_code == status.HTTP_200_OK
        response_data = response.json()
        assert response_data["buyer_id"] == order_data["buyer_id"]
        assert response_data["seller_id"] == order_data["seller_id"]
        assert response_data["product_id"] == order_data["product_id"]
        assert response_data["quantity"] == order_data["quantity"]
        assert response_data["order_id"] == order_data["order_id"]
        assert response_data["date"] == order_data["date"]
