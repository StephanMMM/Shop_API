import pytest
from fastapi import status, FastAPI
from starlette.testclient import TestClient
from Shop_API.app.tests.fixtures.fixtures import (db_fixture,
                                                  users_create_data)


app = FastAPI()
test_client = TestClient(app)

@pytest.mark.usefixtures("db_fixture", "users_create_data")
def test_users_create_valid():
    """Test creating a new user."""
    with db_fixture as db:
        response = test_client.post("/users/create", json=users_create_data)
        response_data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_data["user_id"] == 6
        assert response_data["email"] == users_create_data["email"]
        assert response_data["points"] == users_create_data["points"]
        assert response_data["shipping_address"] == users_create_data["shipping_address"]


