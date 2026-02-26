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
        #Push item onto stack.

        self._data.append(item)
        self._top += 1

    def pop(self) -> Any:
        #Pop and return top item.

        item = self._data[self._top]
        # remove the top element from underlying storage
        self._data.pop()
        self._top -= 1
        return item

    def peek(self) -> Any:
        #Return top item without removing it.

        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[self._top]

    def size(self) -> int:
        return self._top + 1