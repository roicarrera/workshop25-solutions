import pytest

@pytest.mark.parametrize(
    "value,response",
    [(1, True),
    (-1, False)]
)
def test_is_in_range(value, response):
    assert in_range(value) == response

def in_range(value):
    min=0
    max=10
    return value >= min and value <= max
