# 🤢 Patient #4 - "Mr. Copy/Paste"
# ----------------------------
# SYMPTOM:
# Large codes that check same functionality in different scenarios.
# ----------------------------
# TREATMENT: 💉 Purple Syringe (Parameters Helper)
# Use a decorator function to parametrize test scenarios.
# See /treatments/purple_syringe_parameters_helper.py

def test_is_in_range():
    value = 1
    assert in_range(value)

def test_is_not_in_range():
    value = -1
    assert not in_range(value)

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
