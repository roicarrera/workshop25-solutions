# 💉 Yellow Syringe: Test Data Builder
# Build structured test data clearly and incrementally

class ItemBuilder:
    def __init__(self):
        self._name = "item"
        self._price = 1.0
        self._qty = 1

    def with_name(self, name):
        self._name = name
        return self

    def with_price(self, price):
        self._price = price
        return self

    def with_qty(self, qty):
        self._qty = qty
        return self

    def build(self):
        return {"name": self._name, "price": self._price, "qty": self._qty}