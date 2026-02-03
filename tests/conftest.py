import jsonschema
import pytest
import responses

# Mock data for testing
MOCK_PRODUCTS = [
    {
        "id": 1,
        "title": "Test Product 1",
        "price": 10.99,
        "category": "electronics",
        "image": "https://example.com/image1.jpg",
        "description": "Test description 1",
    },
    {
        "id": 2,
        "title": "Test Product 2",
        "price": 20.99,
        "category": "clothing",
        "image": "https://example.com/image2.jpg",
        "description": "Test description 2",
    },
]

MOCK_CARTS = [
    {
        "id": 1,
        "userId": 1,
        "date": "2023-01-01",
        "products": [{"productId": 1, "quantity": 2}],
    }
]

MOCK_USERS = [
    {
        "id": 1,
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpass",
        "name": {"firstname": "Test", "lastname": "User"},
        "address": {"street": "Test St", "city": "Test City"},
        "phone": "123-456-7890",
    }
]

# JSON Schemas for API response validation
PRODUCT_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "price": {"type": "number"},
        "category": {"type": "string"},
        "image": {"type": "string"},
        "description": {"type": "string"},
    },
    "required": ["id", "title", "price", "category", "image"],
}

CART_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "userId": {"type": "integer"},
        "date": {"type": "string"},
        "products": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "productId": {"type": "integer"},
                    "quantity": {"type": "integer"},
                },
                "required": ["productId", "quantity"],
            },
        },
    },
    "required": ["id", "userId", "date", "products"],
}

USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "email": {"type": "string"},
        "username": {"type": "string"},
        "password": {"type": "string"},
        "name": {
            "type": "object",
            "properties": {
                "firstname": {"type": "string"},
                "lastname": {"type": "string"},
            },
            "required": ["firstname", "lastname"],
        },
        "address": {"type": "object"},
        "phone": {"type": "string"},
    },
    "required": ["id", "email", "username", "password", "name", "phone"],
}


@pytest.fixture
def base_url():
    """Fixture providing the base URL for the API"""
    return "https://mock-api.com"


@pytest.fixture(autouse=True)
def mock_api_responses():
    """Mock API responses for all tests"""
    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        # Products endpoints
        rsps.add(
            responses.GET,
            "https://mock-api.com/products",
            json=MOCK_PRODUCTS,
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/products/1",
            json=MOCK_PRODUCTS[0],
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/products/2",
            json={**MOCK_PRODUCTS[0], "id": 2, "title": "Test Product 2"},
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/products/3",
            json={**MOCK_PRODUCTS[0], "id": 3, "title": "Test Product 3"},
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/products/5",
            json={**MOCK_PRODUCTS[0], "id": 5, "title": "Test Product 5"},
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/products/10",
            json={**MOCK_PRODUCTS[0], "id": 10, "title": "Test Product 10"},
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/products/categories",
            json=["electronics", "clothing"],
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/products/category/electronics",
            json=[MOCK_PRODUCTS[0]],
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/products/category/jewelery",
            json=[{**MOCK_PRODUCTS[0], "category": "jewelery"}],
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/products/category/men's clothing",
            json=[{**MOCK_PRODUCTS[0], "category": "men's clothing"}],
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/products/category/women's clothing",
            json=[{**MOCK_PRODUCTS[0], "category": "women's clothing"}],
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/products/category/clothing",
            json=[{**MOCK_PRODUCTS[0], "category": "clothing"}],
            status=200,
        )

        # Carts endpoints
        rsps.add(
            responses.GET, "https://mock-api.com/carts", json=MOCK_CARTS, status=200
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/carts/1",
            json=MOCK_CARTS[0],
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/carts/2",
            json={**MOCK_CARTS[0], "id": 2},
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/carts/3",
            json={**MOCK_CARTS[0], "id": 3},
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/carts/5",
            json={**MOCK_CARTS[0], "id": 5},
            status=200,
        )
        rsps.add(
            responses.POST,
            "https://mock-api.com/carts",
            json={
                "id": 2,
                "userId": 1,
                "date": "2020-03-02",
                "products": [
                    {"productId": 1, "quantity": 1},
                    {"productId": 2, "quantity": 2},
                ],
            },
            status=201,
        )
        rsps.add(
            responses.PUT,
            "https://mock-api.com/carts/1",
            json=MOCK_CARTS[0],
            status=200,
        )
        rsps.add(responses.DELETE, "https://mock-api.com/carts/1", status=200)

        # Users endpoints
        rsps.add(
            responses.GET, "https://mock-api.com/users", json=MOCK_USERS, status=200
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/users/1",
            json=MOCK_USERS[0],
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/users/2",
            json={**MOCK_USERS[0], "id": 2, "username": "testuser2"},
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/users/3",
            json={**MOCK_USERS[0], "id": 3, "username": "testuser3"},
            status=200,
        )
        rsps.add(
            responses.GET,
            "https://mock-api.com/users/5",
            json={**MOCK_USERS[0], "id": 5, "username": "testuser5"},
            status=200,
        )
        rsps.add(
            responses.POST,
            "https://mock-api.com/users",
            json={"id": 2, **MOCK_USERS[0]},
            status=201,
        )
        rsps.add(
            responses.PUT,
            "https://mock-api.com/users/1",
            json={
                "id": 1,
                "email": "updated@example.com",
                "username": "updateduser",
                "password": "updatedpass",
                "name": {"firstname": "Updated", "lastname": "User"},
                "address": {
                    "city": "Updated City",
                    "street": "Updated Street",
                    "number": 2,
                    "zipcode": "54321",
                    "geolocation": {"lat": "1", "long": "1"},
                },
                "phone": "987-654-3210",
            },
            status=200,
        )
        rsps.add(responses.DELETE, "https://mock-api.com/users/1", status=200)

        # 404 for non-existent resources
        rsps.add(
            responses.GET, "https://mock-api.com/products/999", json={}, status=200
        )
        rsps.add(responses.GET, "https://mock-api.com/products/0", json={}, status=200)
        rsps.add(responses.GET, "https://mock-api.com/products/-1", json={}, status=200)
        rsps.add(
            responses.GET, "https://mock-api.com/products/9999", json={}, status=200
        )
        rsps.add(responses.GET, "https://mock-api.com/carts/999", status=404)
        rsps.add(responses.GET, "https://mock-api.com/users/999", status=404)

        yield rsps


def validate_product_data(product):
    """Validate product data against JSON schema"""
    jsonschema.validate(instance=product, schema=PRODUCT_SCHEMA)


def validate_cart_data(cart):
    """Validate cart data against JSON schema"""
    jsonschema.validate(instance=cart, schema=CART_SCHEMA)


def validate_user_data(user):
    """Validate user data against JSON schema"""
    jsonschema.validate(instance=user, schema=USER_SCHEMA)
