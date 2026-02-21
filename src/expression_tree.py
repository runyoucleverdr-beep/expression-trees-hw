from __future__ import annotations
from typing import List
from src.node import Node

# define the set of valid operators for this assignment
# Example: OPERATORS = {"+", "-", "*", "/"}
OPERATORS = set()


def is_number_token(token: str) -> bool:
    """
    Decide whether a token is a number (operand).

    TODO:
    - Implement a check for numeric tokens.
    - Return True if it parses, otherwise False.
    """
    return False


def build_expression_tree(postfix_tokens: List[str]) -> Node:
    """
    Build an expression tree from a postfix token list.
    Returns the root Node.

    Core idea (stack of nodes):
    - If token is an operand: create a leaf Node and push it.
    - If token is an operator:
        pop right subtree root
        pop left subtree root
        create a new Node(operator, left, right)
        push the new Node back
    - At the end: the stack must contain exactly one node (the root)

    TODO:
    - Validate input: empty list should raise an error.
    - Handle invalid expressions:
        operator appears but stack has < 2 nodes
        leftover nodes in stack after processing
        token is neither operator nor number
    """
    # TODO: 1) handle empty input
    # if not postfix_tokens: raise ValueError(...)

    # TODO: 2) initialize stack (list[Node])
    stack: List[Node] = []

    # TODO: 3) iterate tokens in postfix_tokens
    for token in postfix_tokens:
        # TODO: normalize token (strip whitespace)
        # token = token.strip()

        # TODO: if token is operator
        # if token in OPERATORS:
        #     - ensure stack has at least 2 nodes else raise
        #     - pop right then left (order matters)
        #     - create operator node and push back
        # elif token is number:
        #     - create leaf node and push
        # else:
        #     - raise ValueError for invalid token
        pass

    # TODO: 4) after loop, stack must have exactly one node
    # if len(stack) != 1: raise ValueError(...)
    # return stack[0]

    # TODO: placeholder return (remove after implementing)
    return Node("TODO")