import pytest
import requests

BASE_URL = "https://fakestoreapi.com"


def validate_user_data(user):
    """Helper function to validate user data types and required fields"""
    assert isinstance(user["id"], int)
    assert isinstance(user["email"], str)
    assert isinstance(user["username"], str)
    assert isinstance(user["password"], str)
    assert isinstance(user["name"], dict)
    assert "firstname" in user["name"]
    assert "lastname" in user["name"]
    assert isinstance(user["phone"], str)
    assert isinstance(user["address"], dict)


def test_get_all_users():
    """Test retrieving all users from Fake Store API"""
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0
    # Check first 3 users
    for user in users[:3]:
        validate_user_data(user)


@pytest.mark.parametrize("user_id", [1, 2, 3, 5])
def test_get_single_user(user_id):
    """Test retrieving a single user"""
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id
    validate_user_data(user)


def test_create_user():
    """Test creating a new user"""
    new_user = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "password",
        "name": {"firstname": "Test", "lastname": "User"},
        "address": {
            "city": "Test City",
            "street": "Test Street",
            "number": 1,
            "zipcode": "12345",
            "geolocation": {"lat": "0", "long": "0"},
        },
        "phone": "123-456-7890",
    }
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    assert response.status_code == 201
    user = response.json()
    assert "id" in user
    assert isinstance(user["id"], int)


def test_update_user():
    """Test updating an existing user"""
    user_id = 1
    update_data = {
        "email": "updated@example.com",
        "username": "updateduser",
        "password": "newpassword",
        "name": {"firstname": "Updated", "lastname": "User"},
        "address": {
            "city": "Updated City",
            "street": "Updated Street",
            "number": 2,
            "zipcode": "54321",
            "geolocation": {"lat": "1", "long": "1"},
        },
        "phone": "987-654-3210",
    }
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=update_data)
    assert response.status_code == 200
    user = response.json()
    assert user["email"] == update_data["email"]
    assert user["username"] == update_data["username"]


def test_delete_user():
    """Test deleting a user"""
    user_id = 1
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
