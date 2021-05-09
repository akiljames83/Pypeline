"""
Implementation of the Min Heap

"""

import heapq
from typing import Any, List, Optional

import numpy as np

class MinHeap():
    """
    Implementation of the Min Heap (https://en.wikipedia.org/wiki/Heap_(data_structure))

    For any given node C, if P is a parent node of C, the key of P is less than or equal to the key of C

    """
    def __init__(self, li: List[int]=[]):
        self.MinHeap: List[int] = []
        assert isinstance(li, list)
        self.heapify(li)

    def __repr__(self) -> str:
        return str(self.MinHeap)

    def __str__(self) -> str:
        return str(self.MinHeap)

    def heapify(self, li: List[int]) -> None:
        assert isinstance(li, list)
        if self.MinHeap:
            li2 = [Restore(i) for i in self.MinHeap]
            self.MinHeap = [Backwards(i) for i in li2 + li]
            heapq.heapify(self.MinHeap)
        else:
            self.MinHeap = [Backwards(i) for i in li]
            heapq.heapify(self.MinHeap)

    def heappop(self) -> float:
        if not self.MinHeap:
            exception = "Index Error: Length of Heap is 0."
            raise Exception(exception)
        popped = heapq.heappop(self.MinHeap)
        return float(Restore(popped))

    def heappush(self, val: int) -> None:
        assert (isinstance(val, int))
        heapq.heappush(self.MinHeap,Backwards(val))

    def to_array(self) -> Any:
        return np.array([Restore(i) for i in self.MinHeap])

    def to_list(self) -> List[int]:
        return self.MinHeap

    def merge(self, li: List[int]) -> None:
        assert isinstance(li, list)
        self.heapify(li)

class Backwards(int):
    def __lt__(self, other: int) -> bool:
        return not int.__le__(self, other)
    def __le__(self, other: int) -> bool:
        return not int.__lt__(self, other)
    def __gt__(self, other: int) -> bool:
        return not int.__ge__(self, other)
    def __ge__(self, other: int) -> bool:
        return not int.__gt__(self, other)

class Restore(int):
    def __lt__(self, other: int) -> bool:
        return int.__le__(self, other)
    def __le__(self, other: int) -> bool:
        return int.__lt__(self, other)
    def __gt__(self, other: int) -> bool:
        return int.__ge__(self, other)
    def __ge__(self, other: int) -> bool:
        return int.__gt__(self, other)

if __name__ == "__main__":
    li = [2, 4 , 10, 8, 90, 65, 18]
    li2 = [4, 5, 10, 1]
    heap = MinHeap()
    heap.heapify(li)
    a = heap.heappop()
    print(a, type(a))
    arr = heap.to_array()
    print(arr, type(arr))
    heap.merge(li2)
    print(heap)
    heap.heappop()
    print(heap)


    