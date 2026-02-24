from __future__ import annotations
from typing import List, Optional
from src.node import Node


def to_prefix_list(root: Optional[Node]) -> List[str]:
    """
    Return prefix notation as a list using pre-order traversal (root, left, right).

    """
    # TODO:
    # - If root is None: return []
    # - Otherwise:
    #     1) start with [root.value]
    #     2) extend with prefix of left subtree
    #     3) extend with prefix of right subtree
    return []


def to_postfix_list(root: Optional[Node]) -> List[str]:
    """
    Return postfix notation as a list using post-order traversal (left, right, root).

    """
    # TODO:
    # - If root is None: return []
    # - Otherwise:
    #     1) postfix of left
    #     2) postfix of right
    #     3) append root.value at the end
    return []


def to_infix_list(root: Optional[Node]) -> List[str]:
    """
    Return infix notation as a list using in-order traversal (left, root, right).

    """
    # TODO:
    # - If root is None: return []
    # - For a leaf node: return [root.value]
    # - For an internal node (operator):
    #       return ["("] + infix(left) + [root.value] + infix(right) + [")"]
    return []