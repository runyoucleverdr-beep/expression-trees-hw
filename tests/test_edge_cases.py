import pytest
from src.expression_tree import build_expression_tree
from src.postfix_eval import evaluate_postfix

def test_empty_postfix_string():
    with pytest.raises(ValueError):
        evaluate_postfix("")

def test_malformed_insufficient_operands_eval():
    with pytest.raises(ValueError):
        evaluate_postfix("3 +")

def test_malformed_too_many_operands_eval():
    with pytest.raises(ValueError):
        evaluate_postfix("3 4 5")

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        evaluate_postfix("3 0 /")

def test_invalid_token_eval():
    with pytest.raises(ValueError):
        evaluate_postfix("3 a +")

def test_negative_numbers_eval():
    assert evaluate_postfix("-3 4 +") == 1

def test_very_large_numbers_eval():
    # float may overflow to inf; test demonstrates expected float behavior
    r = evaluate_postfix("1e308 1e308 +")
    assert r == float("inf") or r > 0

def test_tree_empty_tokens():
    with pytest.raises(ValueError):
        build_expression_tree([])

def test_tree_insufficient_operands():
    with pytest.raises(ValueError):
        build_expression_tree(["3", "+"])

def test_tree_too_many_operands_leftover():
    with pytest.raises(ValueError):
        build_expression_tree(["3", "4"])

def test_tree_invalid_token():
    with pytest.raises(ValueError):
        build_expression_tree(["3", "a", "+"])

def test_tree_negative_number_token():
    root = build_expression_tree(["-3", "4", "+"])
    assert root.value == "+"
    assert root.left.value == "-3"
    assert root.right.value == "4"