# 💉 Purple Syringe: Test Parametrized
# Provide sets of parameters to cover all scenarios

import pytest

@pytest.mark.parametrize(
    "value, is_int",
    [(1, True),
    ("a", False)]
)
def test_type(value, is_int):
    assert ("<class 'int'>" == str(type(value))) == is_int