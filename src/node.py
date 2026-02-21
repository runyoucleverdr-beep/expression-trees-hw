from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    """
    Expression tree node
    value:
        - If this node is a leaf, stores an operant token
        - If this node is an internal node, stores an operator token
    left/right:
        - Child nodes 
        - None: leaf nodes
    """
    value: str
    left: Optional["Node"]=None
    right: Optional["Node"]=None

    def is_leaf(self) -> bool:
        """
        Return True if this node has no children.

        TODO:
        - Decide the exact rule you want to use:
          Typically: leaf means left is None AND right is None.
        - Implement the boolean check and return it.
        """
        return False
    
    def __str__(self) -> str:
        """
        Human-friendly string representation.

        TODO:
        - Decide what you want to show when printing a node:
          e.g., return self.value
        - Implement and return the string.
        """
        return "<Node>"