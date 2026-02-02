# FakeStore API Tests

This project contains automated tests for the FakeStore API (https://fakestoreapi.com/) using Python, requests, and pytest. It covers comprehensive testing of products, carts, and users endpoints with full CRUD operations where applicable.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate  # On macOS/Linux
   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

Run the tests with pytest:
```bash
pytest
```

Run specific test suites:
```bash
pytest -m smoke      # Basic functionality tests (17 tests)
pytest -m regression # Comprehensive tests (29 tests)
```

## Project Structure

- `tests/test_products.py`: Test cases for product-related API endpoints (13 tests) - Read operations with parametrization and data validation
- `tests/test_carts.py`: Test cases for cart-related API endpoints (8 tests) - Full CRUD operations
- `tests/test_users.py`: Test cases for user-related API endpoints (8 tests) - Full CRUD operations
- `tests/conftest.py`: Pytest configuration with fixtures (base_url fixture for API endpoint)
- `pytest.ini`: Pytest configuration file with markers and settings
- `requirements.txt`: Python dependencies

## Test Coverage

- **Products**: GET all, GET by ID (parametrized), GET by category (parametrized), data type validation
- **Carts**: Full CRUD (Create, Read, Update, Delete) with data validation
- **Users**: Full CRUD (Create, Read, Update, Delete) with data validation

Total: 29 automated tests demonstrating best practices in API testing, parametrization, and data validation.