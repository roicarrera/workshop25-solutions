# 🧪 Patient #2 - "Ms. Hardcoded Data"
# ----------------------------
# SYMPTOM:
# Test uses hardcoded, brittle test data that's hard to extend.
# ----------------------------
# TREATMENT: 💉 Yellow Syringe (Test Data Builder)
# Use a builder to generate readable, reusable test data.
# Check /treatments/yellow_syringe_data_builder.py for inspiration.

def test_total_price_single_item():
    cart = [{"name": "apple", "price": 1.0, "qty": 3}]
    assert total_price(cart) == 3.0

def test_total_price_multiple_items():
    cart = [
        {"name": "apple", "price": 1.0, "qty": 3},
        {"name": "banana", "price": 2.0, "qty": 1},
    ]
    assert total_price(cart) == 5.0

def total_price(cart):
    return sum(item["price"] * item["qty"] for item in cart)