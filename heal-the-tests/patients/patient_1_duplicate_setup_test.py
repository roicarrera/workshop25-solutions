# 👨‍⚕️ Patient #1 - "Mr. Duplicate Setup"
# ----------------------------
# SYMPTOM:
# These tests repeat setup code in every function.
# ----------------------------
# TREATMENT: 💉 Blue Syringe (Fixture Factory)
# Use a pytest fixture to clean up the duplication.
# You'll find a sample in /treatments/blue_syringe_fixture_factory.py

def test_login_valid_user():
    db = {"users": [{"username": "bob", "password": "123"}]}
    user = {"username": "bob", "password": "123"}
    assert login(user, db)

def test_login_invalid_user():
    db = {"users": [{"username": "bob", "password": "123"}]}
    user = {"username": "bob", "password": "wrong"}
    assert not login(user, db)

def login(user, db):
    for u in db["users"]:
        if u["username"] == user["username"] and u["password"] == user["password"]:
            return True
    return False
