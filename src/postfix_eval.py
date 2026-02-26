from __future__ import annotations
from typing import Set
from src.stack import Stack
import math


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

    # Evaluate a postfix expression using a stack

    if postfix_expr is None:
        raise ValueError("postfix_expr is None")
    
    tokens = postfix_expr.split()
    if len(tokens) == 0:
        raise ValueError("postfix_expr is empty")
    
    stack = Stack()
    for token in tokens:
        if token in OPERATORS:
            # need two operands
            if stack.size() < 2:
                raise ValueError(f"Invalid postfix expression: not enough operands for '{token}'")

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.push(left + right)
            elif token == "-":
                stack.push(left - right)
            elif token == "*":
                stack.push(left * right)
            else:  # token == "/"
                if right == 0:
                    raise ZeroDivisionError("division by zero")
                stack.push(left / right)

        elif is_number_token(token):
            stack.push(float(token))
        else:
            raise ValueError(f"Invalid token '{token}'")
        
    if stack.size() != 1:
        raise ValueError("Invalid postfix expression: leftover operands after evaluation")

    result = stack.pop()

    if not math.isfinite(result):
        return result

    if abs(result - round(result)) < 1e-9:
        return int(round(result))

    return result