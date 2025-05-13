import pytest

@pytest.fixture
def valid_user():
    return {"username": "bob", "password": "123"}

@pytest.fixture
def user_db(valid_user):
    return {"users": [valid_user]}

def test_login_valid_user(valid_user, user_db):
    assert login(valid_user, user_db)

def test_login_invalid_user(user_db):
    user = {"username": "bob", "password": "wrong"}
    assert not login(user, user_db)

def login(user, db):
    for u in db["users"]:
        if u["username"] == user["username"] and u["password"] == user["password"]:
            return True
    return False
