import pytest
import requests

BASE_URL = "https://fakestoreapi.com"


def validate_product_data(product):
    """Helper function to validate product data types and required fields"""
    assert isinstance(product["id"], int)
    assert isinstance(product["title"], str)
    assert isinstance(product["price"], (int, float))
    assert isinstance(product["category"], str)
    assert isinstance(product["image"], str)
    if "description" in product:
        assert isinstance(product["description"], str)


def test_get_all_products():
    """Test retrieving all products from Fake Store API"""
    response = requests.get(f"{BASE_URL}/products")
    assert response.status_code == 200
    products = response.json()
    assert isinstance(products, list)
    assert len(products) > 0
    # Check that each product has required fields
    for product in products[:5]:  # Check first 5
        assert "id" in product
        assert "title" in product
        assert "price" in product
        # Data type validation
        validate_product_data(product)


def test_get_all_products_not_empty():
    response = requests.get(f"{BASE_URL}/products")
    products = response.json()

    assert len(products) > 0
    assert products[-1]["id"] is not None


@pytest.mark.parametrize("product_id", [1, 2, 3, 5, 10])
def test_get_single_product(product_id):
    """Test retrieving a single product"""
    response = requests.get(f"{BASE_URL}/products/{product_id}")
    assert response.status_code == 200
    product = response.json()
    assert product["id"] == product_id
    assert "title" in product
    assert "description" in product
    assert "price" in product
    # Data type validation
    validate_product_data(product)


def test_get_product_categories():
    """Test retrieving product categories"""
    response = requests.get(f"{BASE_URL}/products/categories")
    assert response.status_code == 200
    categories = response.json()
    assert isinstance(categories, list)
    assert len(categories) > 0


@pytest.mark.parametrize(
    "category", ["electronics", "jewelery", "men's clothing", "women's clothing"]
)
def test_get_products_by_category(category):
    """Test retrieving products by category"""
    response = requests.get(f"{BASE_URL}/products/category/{category}")
    assert response.status_code == 200
    products = response.json()
    assert isinstance(products, list)
    for product in products:
        assert product["category"] == category
        # Data type validation
        validate_product_data(product)


def test_last_product_in_each_category():
    """Test that the last product in each category has the correct category"""
    # Get all categories
    response = requests.get(f"{BASE_URL}/products/categories")
    assert response.status_code == 200
    categories = response.json()

    # For each category, get products and check the last one
    for category in categories:
        response = requests.get(f"{BASE_URL}/products/category/{category}")
        assert response.status_code == 200
        products = response.json()
        assert isinstance(products, list)
        if products:  # If there are products in the category
            last_product = products[-1]
            assert last_product["category"] == category
            assert "id" in last_product
            assert "title" in last_product
            # Data type validation
            validate_product_data(last_product)


@pytest.mark.parametrize("product_id", [9999, 0, -1])
def test_nonexistent_product(product_id):
    response = requests.get(f"{BASE_URL}/products/{product_id}")
    assert (
        response.status_code == 200
    )  # Fake Store API always returns 200 for these IDs

    if response.text:
        product = response.json()
        assert product["id"] != product_id  # Ensure the product does not exist
    else:
        # If response is empty, consider it as non-existent product
        assert True
