# 🤢 Patient #3 - "Mr. Spaghetti Assertion"
# ----------------------------
# SYMPTOM:
# Long and unclear assertions that mix multiple checks and logic.
# ----------------------------
# TREATMENT: 💉 Green Syringe (Assertion Helper)
# Use a helper function to encapsulate the logic and clarify intent.
# See /treatments/green_syringe_assertion_helper.py

def test_user_profile():
    user = {
        "username": "test",
        "email": "test@example.com",
        "address": {"city": "Galway", "zip": "12345"}
    }
    assert user["username"] == "test" and \
           user["email"].endswith("@example.com") and \
           "city" in user["address"] and \
           len(user["address"]["zip"]) == 5