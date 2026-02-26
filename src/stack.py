from __future__ import annotations
from typing import Any, List


class Stack:
    """
    Stack ADT implemented using a Python list as underlying storage,
    but with an explicit 'top' index managed manually.
    """

    def __init__(self) -> None:
        self._data: List[Any] = []
        self._top: int = -1

    def is_empty(self) -> bool:
        return self._top == -1
    
    def push(self, item: Any) -> None:
        """
        Push item onto stack.

        TODO:
        - Add item to underlying list (append is allowed)
        - Update self._top accordingly
        """
        pass

    def pop(self) -> Any:
        """
        Pop and return top item.

        TODO:
        - If empty, raise IndexError (or a custom error)
        - Retrieve the top element
        - Remove it from underlying list
        - Update self._top
        - Return the element
        """
        pass

    def peek(self) -> Any:
        """
        Return top item without removing it.

        TODO:
        - If empty, raise IndexError
        - Return current top element
        """
        pass

    def size(self) -> int:
        return self._top + 1