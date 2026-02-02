# FakeStore API Tests

This project contains automated tests for the FakeStore API (https://fakestoreapi.com/) using Python, requests, and pytest. It covers comprehensive testing of products, carts, and users endpoints with full CRUD operations where applicable.

## CI/CD

Tests are automatically run on every push and pull request via GitHub Actions.
The workflow includes:
- Running all tests
- Running smoke tests
- Running regression tests
- Generating HTML reports (pytest-html)
- Generating Allure reports for detailed visualization

Reports are available as artifacts in GitHub Actions after each run.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/dkovtun-arch/fakestore-api-tests.git
   cd fakestore-api-tests
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # On macOS/Linux
   # On Windows: .venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

Run the tests with pytest:

```bash
# All tests
pytest

# Smoke tests (basic functionality)
pytest -m smoke

# Regression tests (comprehensive)
pytest -m regression

# With HTML report
pytest --html=report.html --self-contained-html

# With Allure results (for report generation)
pytest --alluredir=allure-results
```

## Reports

### HTML Reports
Generated automatically in CI and locally with `--html` flag. Open `report.html` in browser for detailed test results.

### Allure Reports
For detailed, interactive reports:
1. Run tests with `--alluredir=allure-results`
2. Install Allure CLI: `brew install allure` (macOS) or download from https://docs.qameta.io/allure/
3. Generate report: `allure generate allure-results --clean`
4. Open report: `allure open allure-report`

## Project Structure

- `.github/workflows/api-tests.yml`: GitHub Actions workflow for CI/CD with report generation
- `tests/test_products.py`: Test cases for product-related API endpoints (13 tests) - Read operations with parametrization and data validation
- `tests/test_carts.py`: Test cases for cart-related API endpoints (8 tests) - Full CRUD operations
- `tests/test_users.py`: Test cases for user-related API endpoints (8 tests) - Full CRUD operations
- `tests/conftest.py`: Pytest configuration with fixtures, JSON schemas, and validation functions
- `pytest.ini`: Pytest configuration file with custom markers and settings
- `requirements.txt`: Python dependencies (requests, pytest, jsonschema, pytest-html, allure-pytest)

## Test Coverage

- **Products**: GET all, GET by ID (parametrized), GET by category (parametrized), data type validation, schema validation
- **Carts**: Full CRUD (Create, Read, Update, Delete) with data validation and schema validation
- **Users**: Full CRUD (Create, Read, Update, Delete) with data validation and schema validation

Total: 32 automated tests demonstrating:
- API testing best practices
- Parametrization for data-driven testing
- JSON schema validation
- Custom markers for test organization
- Fixtures for reusable test data
- Comprehensive error handling

## Technologies Used

- **Python 3.13**: Core language
- **pytest**: Testing framework with parametrization, fixtures, and markers
- **requests**: HTTP client for API calls
- **jsonschema**: JSON structure validation
- **pytest-html**: HTML report generation
- **allure-pytest**: Allure report integration
- **GitHub Actions**: CI/CD automation

## Security Note

This repository has been cleaned of any sensitive data. SSH keys or other credentials are not present in the codebase or commit history.

## Usage in Portfolio

This project demonstrates professional API testing skills suitable for software testing portfolios. It showcases:
- Complete test automation setup
- CI/CD integration
- Report generation
- Best practices in test organization and validation
- Real-world API testing scenarios