# 💉 Blue Syringe: Fixture Factory
# Use this structure as inspiration!

import pytest

@pytest.fixture
def valid_user():
    return {"username": "bob", "password": "123"}

@pytest.fixture
def user_db(valid_user):
    return {"users": [valid_user]}