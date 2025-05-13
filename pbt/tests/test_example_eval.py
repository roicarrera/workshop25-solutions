import pytest
from Task5.evaluator import eval_expr

def test_basic_operations():
    # Basic single operations
    assert eval_expr("4") == 4
    assert eval_expr("2+2") == 4
    assert eval_expr("3*5") == 15

def test_multiple_same_operator():
    # Multiple same operators (addition or multiplication) - associative operations
    assert eval_expr("2+3+4") == 9      # (2+3)+4 = 9, same as 2+(3+4)
    assert eval_expr("2*3*4") == 24     # (2*3)*4 = 24, same as 2*(3*4)

def test_parentheses_usage():
    # Expressions with parentheses
    assert eval_expr("(1+2)*3") == 9    # parentheses should override normal precedence
    assert eval_expr("1+(2*3)+4") == 11 # combine parentheses with other ops
    assert eval_expr("((2+3)*2)+1") == 11  # nested parentheses
    print("eval:", eval("4+4+4+4*7*7+4"))
    print("eval_expr:", eval_expr("4+4+4+4*7*7+4"))
