import pytest

@pytest.fixture
def base_url():
    """Fixture providing the base URL for the FakeStore API"""
    return "https://fakestoreapi.com"