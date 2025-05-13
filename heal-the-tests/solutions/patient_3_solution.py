from treatments.green_syringe_assertion_helper import assert_valid_profile

def test_user_profile():
    user = {
        "username": "test",
        "email": "test@example.com",
        "address": {"city": "Galway", "zip": "12345"}
    }
    assert_valid_profile(user)
