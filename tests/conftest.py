import pytest

from api.users_api import get_user


@pytest.fixture
def user_data():

    response = get_user(1)

    return response.json()


@pytest.fixture
def new_user():

    return {
        "name": "Wilson",
        "username": "wilson123",
        "email": "wilson@test.com"
    }


@pytest.fixture
def updated_user():

    return {
        "name": "Wilson Updated",
        "username": "wilson456",
        "email": "new@test.com"
    }