"""
Implementation of the Queue Data Stucture

# FIFO Structure -> First in First Out

"""

from typing import Any, Optional, List

import numpy as np

class Queue:
    def __init__(self, maxlen: int=1e9):
        self.queue: List[Any] = []
        self.maxlen: int = maxlen

    def isEmpty(self) -> bool:
        return self.queue == []

    def sizeQueue(self) -> int:
        return len(self.queue)

    # # Main Methods: Enqueue Dequeue Peel
    def enqueue(self, data: Any) -> None:
        if self.sizeQueue() < self.maxlen: 
            self.queue.append(data)
        else:
            _ = self.dequeue()
            del _
            self.queue.append(data)

    def dequeue(self) -> Any:
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self) -> Any:
        return self.queue[0]

    def to_array(self) -> Any:
        return np.array(self.queue)

    def to_list(self) -> List[int]:
        return self.queue
