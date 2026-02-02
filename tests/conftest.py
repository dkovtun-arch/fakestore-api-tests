import jsonschema
import pytest

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
    """Fixture providing the base URL for the FakeStore API"""
    return "https://fakestoreapi.com"


def validate_product_data(product):
    """Validate product data against JSON schema"""
    jsonschema.validate(instance=product, schema=PRODUCT_SCHEMA)


def validate_cart_data(cart):
    """Validate cart data against JSON schema"""
    jsonschema.validate(instance=cart, schema=CART_SCHEMA)


def validate_user_data(user):
    """Validate user data against JSON schema"""
    jsonschema.validate(instance=user, schema=USER_SCHEMA)
