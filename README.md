# REST API Automation Project

A Python-based REST API automation test suite built with `requests` and `pytest`.

## Overview

This project automates testing of REST API endpoints using Python. It covers common CRUD operations and validates both HTTP response status codes and response data.

## Technologies

* Python
* pytest
* requests
* pytest-html
* Git
* GitHub

## API Operations Tested

* GET — retrieve users
* POST — create users
* PUT — update users
* DELETE — delete users

## Test Coverage

The test suite includes:

* Parameterized GET tests for multiple user IDs
* Positive API response validation
* Negative testing for invalid user IDs
* Response body validation
* Reusable pytest fixtures
* Centralized fixtures using `conftest.py`
* API request logging
* HTML test reporting

## Project Structure

```text
API_Automation_Project/
│
├── api/
│   ├── api_client.py
│   └── users_api.py
│
├── tests/
│   ├── conftest.py
│   └── test_users.py
│
├── config.py
├── main.py
├── .gitignore
└── README.md
```

## Running the Tests

### 1. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Run the test suite

```powershell
python -m pytest -v
```

### 3. Generate an HTML test report

```powershell
python -m pytest -v --html=report.html
```

## Example Result

```text
7 passed in 0.66s
```

## API

The project currently uses JSONPlaceholder as a practice REST API.

## Future Improvements

* Add more positive and negative API test cases
* Expand authentication and header testing
* Improve logging configuration
* Add CI/CD with GitHub Actions
* Expand the automation framework structure
