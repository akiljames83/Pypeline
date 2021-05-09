"""
Implementation of the Max Heap

"""

import heapq
from typing import Any, List, Optional, Union

import numpy as np

class MaxHeap():
    """
    Implementation of the Max Heap (https://en.wikipedia.org/wiki/Min-max_heap)

    For any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C

    """
    def __init__(self, li: List[Union[float, int]]=[]) -> None:
        self.MaxHeap = []
        assert isinstance(li, list)
        self.heapify(li)
            

    def __repr__(self) -> str:
        return str(self.MaxHeap)

    def __str__(self) -> str:
        return str(self.MaxHeap)

    def heapify(self, li: List[Union[float, int]]) -> None:
        assert isinstance(li, list)
        if self.MaxHeap:
            self.merge(li)
        else:
            self.MaxHeap = li
            heapq.heapify(self.MaxHeap)

    def heappop(self) -> Any:
        if not self.MaxHeap:
            exception = "Index Error: Length of Heap is 0."
            raise Exception(exception)
        return heapq.heappop(self.MaxHeap)

    def heappush(self, val: Union[float, int]) -> None:
        assert (isinstance(val, float) or isinstance(val, int))
        heapq.heappush(self.MaxHeap,val)

    def to_array(self) -> Any:
        return np.array(self.MaxHeap)

    def merge(self, li: List[Union[float, int]]) -> None:
        assert isinstance(li, list)
        self.MaxHeap = self.MaxHeap + li
        heapq.heapify(self.MaxHeap)

    