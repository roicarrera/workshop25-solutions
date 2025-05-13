import pytest
from classifier import classify_grade

# TASKS:
# 1. Identify equivalence classes:
#    - A+: 101–110
#    - A: 90–100
#    - B: 80–89
#    - C: 70–79
#    - D: 60–69
#    - F: 0–59
# 2. Identify and test boundaries (e.g., 89/90/100/101/110).
# 3. Validate inputs:
#    - Type errors (float, str, None)
#    - Value errors (<0 or >110)

# EXAMPLE TEST:
def test_classify_grade_typical_a():
    assert classify_grade(95) == "A"

# TODO 1: Add one test for each equivalence class (B, C, D, F, A+)

def test_classify_grade_typical_b():
    assert classify_grade(85) == "B"

def test_classify_grade_typical_c():
    assert classify_grade(75) == "C"

def test_classify_grade_typical_d():
    assert classify_grade(65) == "D"

def test_classify_grade_typical_f():
    assert classify_grade(55) == "E"

def test_classify_grade_typical_aplus():
    assert classify_grade(105) == "F"

# TODO 2: Write tests for out-of-bounds values (e.g., -1, 111)
def test_classify_grade_value_errors():
    with pytest.raises(ValueError):
        classify_grade(-1)

# TODO 3: Write tests for invalid types (e.g., float, str, None)
def test_classify_grade_type_errors():
    with pytest.raises(TypeError):
        classify_grade("1")

# TODO 4: Write boundary tests (e.g. score == 89, 90, 100, 101, etc.)
def test_classify_grade_boundary_between_b_and_a():
    assert classify_grade(89) == "B"
    assert classify_grade(90) == "A"
    assert classify_grade(91) == "A"

def test_classify_grade_boundary_between_a_and_aplus():
    assert classify_grade(99) == "A"
    assert classify_grade(100) == "A"
    assert classify_grade(101) == "A+"

def test_classify_grade_boundary_between_b_and_c():
    assert classify_grade(79) == "C"
    assert classify_grade(80) == "B"
    assert classify_grade(81) == "B"

def test_classify_grade_boundary_between_c_and_d():
    assert classify_grade(69) == "D"
    assert classify_grade(70) == "C"
    assert classify_grade(71) == "C"

def test_classify_grade_boundary_between_D_and_F():
    assert classify_grade(59) == "F"
    assert classify_grade(60) == "D"
    assert classify_grade(61) == "D"

def test_classify_grade_boundary_value_error_low():
    classify_grade(0)

def test_classify_grade_boundary_value_error_high():
    classify_grade(110)

# BONUS:
# - Use pytest.mark.parametrize to rewrite the above tests once completed.
# - Discuss: what are the advantages of parameterized tests vs. individual ones?
