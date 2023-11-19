from fastapi import status
from ..fixtures.fixtures import (test_client,
                                 users_create_data,
                                 temp_test_db)

def test_users_create_valid(users_create_data, temp_test_db):
    response = test_client.post("/users/create", json=users_create_data)
    response_data = response.json()
    assert response_data["user_id"] == 6
    assert response.status_code == status.HTTP_200_OK
    assert response_data["email"] == users_create_data["email"]
    assert response_data["points"] == 10000
    assert response_data["shipping_address"] == users_create_data["shipping_address"]


