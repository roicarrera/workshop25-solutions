# 💉 Green Syringe: Assertion Helper
# Isolate messy assertion logic into a readable function

def assert_valid_profile(user):
    assert user["username"] == "test"
    assert user["email"].endswith("@example.com")
    assert "city" in user["address"]
    assert len(user["address"]["zip"]) == 5