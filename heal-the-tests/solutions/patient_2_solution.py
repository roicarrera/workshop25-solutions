from treatments.yellow_syringe_data_builder import ItemBuilder

def test_total_price_single_item():
    item = ItemBuilder().with_name("apple").with_price(1.0).with_qty(3).build()
    cart = [item]
    assert total_price(cart) == 3.0

def test_total_price_multiple_items():
    apple = ItemBuilder().with_name("apple").with_price(1.0).with_qty(3).build()
    banana = ItemBuilder().with_name("banana").with_price(2.0).with_qty(1).build()
    cart = [apple, banana]
    assert total_price(cart) == 5.0

def total_price(cart):
    return sum(item["price"] * item["qty"] for item in cart)
