from __future__ import annotations
from typing import List, Optional
from src.node import Node


def to_prefix_list(root: Optional[Node]) -> List[str]:
    """
    Prefix (pre-order): root, left, right
    Empty tree -> []

    """
    if root is None:
        return []
    result: List[str] = [root.value]
    result.extend(to_prefix_list(root.left))
    result.extend(to_prefix_list(root.right))
    return result


def to_postfix_list(root: Optional[Node]) -> List[str]:
    """
    Postfix (post-order): left, right, root
    Empty tree -> []
    """
    if root is None:
        return []
    result: List[str] = []
    result.extend(to_postfix_list(root.left))
    result.extend(to_postfix_list(root.right))
    result.append(root.value)
    return result


def to_infix_list(root: Optional[Node]) -> List[str]:
    """
    Infix (in-order): left, root, right + parentheses.
    """
    if root is None:
        return []
    
    # Leaf node: just the operand itself (no parentheses here)
    if root.left is None and root.right is None:
        return [root.value]
    
    # Internal node (operator): wrap the whole sub-expression
    result: List[str] = ["("]
    result.extend(to_infix_list(root.left))
    result.append(root.value)
    result.extend(to_infix_list(root.right))
    result.append(")")
    return result