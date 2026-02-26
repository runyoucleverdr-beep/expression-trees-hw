from __future__ import annotations
from typing import Set
from src.stack import Stack

OPERATORS: Set[str] = {"+", "-", "*", "/"}


def is_number_token(token: str) -> bool:
    """
    Decide if token is numeric.
    """
    try:
        float(token)
        return True
    except ValueError:
        return False


def evaluate_postfix(postfix_expr: str) -> float:
    """
    Evaluate a postfix expression (space-separated tokens) using a stack,
    WITHOUT constructing an expression tree.

    TODO (algorithm):
      - Split postfix_expr by whitespace into tokens
      - For each token:
          * If number: push it (as float) onto the stack
          * If operator:
              - pop right operand
              - pop left operand
              - apply operator (left op right)
              - push result back
          * Else: raise ValueError for invalid token
      - At end: stack must contain exactly one value -> return it
      - If tokens empty or leftover values -> raise ValueError
    """
    return 0.0