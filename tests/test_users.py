import pytest

from api.users_api import (
    get_user,
    create_user,
    update_user,
    delete_user
)


# -------------------------
# GET user tests
# -------------------------

@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        (1, 200),
        (2, 200),
        (3, 200),
        (999, 404)
    ]
)
def test_get_user(user_id, expected_status):

    response = get_user(user_id)

    assert response.status_code == expected_status

    if expected_status == 200:
        data = response.json()

        assert "username" in data
        assert data["id"] == user_id


# -------------------------
# POST user tests
# -------------------------

def test_create_user(new_user):

    response = create_user(new_user)

    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "Wilson"
    assert data["username"] == "wilson123"
    assert data["email"] == "wilson@test.com"


# -------------------------
# PUT user tests
# -------------------------

def test_update_user(updated_user):

    response = update_user(1, updated_user)

    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Wilson Updated"
    assert data["username"] == "wilson456"
    assert data["email"] == "new@test.com"


# -------------------------
# DELETE user tests
# -------------------------

def test_delete_user():

    response = delete_user(1)

    assert response.status_code in [200, 204]