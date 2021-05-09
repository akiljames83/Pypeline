"""
Implementation of the Stack Data Structure

N.B:
    - Array representation -> LIFO Structure

"""

from typing import Any, List, Optional

import numpy as np

class Stack:
    """
    Implementation of the Stack Data Structure (https://en.wikipedia.org/wiki/Stack_(abstract_data_type))

    An abstract data type that serves as a collection of elements, with two main principal operations: push and pop
    from the top of the list (most recent values).
    """

    def __init__(self) -> None:
        self.stack: List[Any] = []

    def isEmpty(self) -> bool:
        return self.stack == []

    def sizeStack(self) -> int:
        return len(self.stack)

    # 3 main methods in a stack! Push, Pop and Peek
    def push(self, data: Any) -> None:
        self.stack.append(data)

    def pop(self) -> Any:
        data = self.stack[-1]
        #self.stack = self.stack[:-1]
        del self.stack[-1]
        return data

    def peek(self) -> Any:
        return self.stack[-1]

    def to_array(self) -> Any:
        return np.array(self.stack)

    def to_list(self) -> List[Any]:
        return self.stack

