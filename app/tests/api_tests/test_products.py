import pytest
from fastapi import status, FastAPI
from starlette.testclient import TestClient
from Shop_API.app.tests.fixtures.fixtures import (db_fixture,
                                                  products_create_data,
                                                  products_update_data)


app = FastAPI()
test_client = TestClient(app)


@pytest.mark.usefixtures("db_fixture", "products_create_data")
def test_products_create_valid():
    with db_fixture as db:
        response = test_client.post("/products/create",
                                    json=products_create_data
        )
        response_data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_data["product_id"] == 6
        assert response_data["title"] == products_create_data["title"]
        assert response_data["description"] == products_create_data["description"]
        assert response_data["price"] == products_create_data["price"]
        assert response_data["owner_id"] == products_create_data["owner_id"]


@pytest.mark.usefixtures("db_fixture", "products_update_data")
def test_products_update_valid():
    with db_fixture as db:
        response = test_client.put("/products/update",
                                   json=products_update_data
        )
        response_data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_data["product_id"] == 6
        assert response_data["title"] == products_update_data["title"]
        assert response_data["description"] == products_update_data["description"]
        assert response_data["price"] == products_update_data["price"]
        assert response_data["owner_id"] == products_update_data["owner_id"]


@pytest.mark.usefixtures("db_fixture", "products_create_data")
def test_products_delete_valid():
    with db_fixture as db:
        response = test_client.delete("/products/delete",
                                      json={products_create_data.product_id}
        )
        response_data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_data["product_id"] == 6
        assert response_data["title"] == products_create_data["title"]
        assert response_data["description"] == products_create_data["description"]
        assert response_data["price"] == products_create_data["price"]
        assert response_data["owner_id"] == products_create_data["owner_id"]
