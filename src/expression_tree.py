from __future__ import annotations
from typing import List
from src.node import Node

# define the set of valid operators
OPERATORS = {"+", "-", "*", "/"}


def is_number_token(token: str) -> bool:
    """
    Return True if token can be parsed as a number 
    (int/float, including negatives), otherwise False.
    """
    try:
        float(token)
        return True
    except ValueError:
        return False


def build_expression_tree(postfix_tokens: List[str]) -> Node:
    """
    Build an expression tree from a postfix token list and return the root Node.

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
    #1) handle empty input
    # if not postfix_tokens: raise ValueError(...)
    if not postfix_tokens:
        raise ValueError("postfix_tokens is empty")

    #2) initialize stack (list[Node])
    stack: List[Node] = []

    #3) iterate tokens in postfix_tokens
    for raw in postfix_tokens:
        #normalize token (strip whitespace)
        token = raw.strip()

        if token == "":
            # Ignore empty tokens if input accidentally contains them
            continue
        
        # if token in OPERATORS:
        #     - ensure stack has at least 2 nodes else raise
        if token in OPERATORS:
            if len(stack) < 2:
                raise ValueError(f"Invalid postfix expression: not enough operands for '{token}'")
        # - pop right then left (order matters)
            right = stack.pop()
            left = stack.pop()
        # - create operator node and push back
            stack.append(Node(token, left=left, right=right))
        # elif token is number:
        #     - create leaf node and push
        elif is_number_token(token):
            stack.append(Node(token))
        # else:
        #     - raise ValueError for invalid token
        else:
            raise ValueError(f"Invalid token '{token}': expected a number or one of {sorted(OPERATORS)}")
    
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression: leftover operands/operators after processing")

    return stack[0]

    # TODO: 4) after loop, stack must have exactly one node
    # if len(stack) != 1: raise ValueError(...)
    # return stack[0]

    # TODO: placeholder return (remove after implementing)
    return Node("TODO")