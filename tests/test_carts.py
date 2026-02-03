import allure
import pytest
import requests


def validate_cart_data(cart):
    """Helper function to validate cart data types and required fields"""
    assert isinstance(cart["id"], int)
    assert isinstance(cart["userId"], int)
    assert "date" in cart
    assert isinstance(cart["products"], list)
    for item in cart["products"]:
        assert isinstance(item["productId"], int)
        assert isinstance(item["quantity"], int)


@pytest.mark.smoke
@allure.feature("Carts API")
@allure.story("Get all carts")
def test_get_all_carts(base_url):
    """Test retrieving all carts from Fake Store API"""
    response = requests.get(f"{base_url}/carts")
    assert response.status_code == 200
    carts = response.json()
    assert isinstance(carts, list)
    assert len(carts) > 0
    # Check first 3 carts
    for cart in carts[:3]:
        validate_cart_data(cart)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("cart_id", [1, 2, 3, 5])
@allure.feature("Carts API")
@allure.story("Get single cart")
def test_get_single_cart(base_url, cart_id):
    """Test retrieving a single cart"""
    response = requests.get(f"{base_url}/carts/{cart_id}")
    assert response.status_code == 200
    cart = response.json()
    assert cart["id"] == cart_id
    validate_cart_data(cart)


@pytest.mark.regression
@allure.feature("Carts API")
@allure.story("Create cart")
def test_create_cart(base_url):
    """Test creating a new cart"""
    new_cart = {
        "userId": 1,
        "date": "2020-03-02",
        "products": [{"productId": 1, "quantity": 1}, {"productId": 2, "quantity": 2}],
    }
    response = requests.post(f"{base_url}/carts", json=new_cart)
    assert response.status_code == 201
    cart = response.json()
    validate_cart_data(cart)
    assert cart["userId"] == new_cart["userId"]
    assert len(cart["products"]) == len(new_cart["products"])


@pytest.mark.regression
@allure.feature("Carts API")
@allure.story("Update cart")
def test_update_cart(base_url):
    """Test updating an existing cart"""
    cart_id = 1
    update_data = {
        "userId": 1,
        "date": "2020-03-02",
        "products": [{"productId": 1, "quantity": 5}],
    }
    response = requests.put(f"{base_url}/carts/{cart_id}", json=update_data)
    assert response.status_code == 200
    cart = response.json()
    validate_cart_data(cart)
    assert cart["id"] == cart_id


@pytest.mark.regression
@allure.feature("Carts API")
@allure.story("Delete cart")
def test_delete_cart(base_url):
    """Test deleting a cart"""
    cart_id = 1
    response = requests.delete(f"{base_url}/carts/{cart_id}")
    assert response.status_code == 200
