"""
Implementation of the heap

"""

from typing import ClassVar, List

class Heap(object):
    """ 
    Implementation of a Heap (https://en.wikipedia.org/wiki/Heap_(data_structure))
      
    Attributes:\n
        heap: the underlying list data sturcture for the heap
        currentPosition: used to keep track of the index in the heap
    """

    # Class constant variables can be assigned this way
    HEAP_SIZE: ClassVar[int] = 10

    def __init__(self, size: int=10) -> None:
        """ 
        Constructor of the Heap class

        Parameters:\n
            size: desired size of the Heap
        """
        Heap.HEAP_SIZE = size
        self.heap: List[int] = [0]*Heap.HEAP_SIZE
        self.currentPosition: int = -1

    def insert(self, item: int) -> None:
        """ 
        Public method used to insert an item into the Heap

        Parameters:\n
            item: the data to be added to the heap
        """
        if self.isFull():
            print("Heap is full...")
            return

        else:
            self.currentPosition += 1
            self.heap[self.currentPosition] = item
            self.__fixUp(self.currentPosition) # reheap the heap

    def heapSort(self) -> None:
        """ 
        Public method used to sort the heap
        """
        for i in range(self.currentPosition+1):
            temp = self.heap[0]
            print("%d" % temp)
            self.heap[0] = self.heap[self.currentPosition - i]
            self.heap[self.currentPosition] = temp
            # fix down 
            self.__fixDown(0,self.currentPosition-i-1)

    def isFull(self) -> bool:
        """ 
        Public method used to determine if the heap is full
        """
        if self.currentPosition + 1 == Heap.HEAP_SIZE:
            return True
        else:
            return False

    def __fixUp(self, index: int) -> None:
        """ 
        Private method used to reheap the heap during insertion

        Parameters:\n
            index: the index of the newly added data
        """
        parentIndex = int((index-1)/2)

        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
            temp = self.heap[parentIndex]
            self.heap[parentIndex] = self.heap[index]
            self.heap[index] = temp
            parentIndex = int((index-1)/2) # from current move up

    def __fixDown(self, index: int, upto: int) -> None:
        """ 
        Private method used to reheap the heap during heap sort

        Parameters:\n
            index: the index of the newly added data
            upto: end index for the heap down operation
        """
        while index <= upto:
            leftChild = 2*index +1
            rightChild = 2*index +2

            if leftChild < upto:
                childToSwap = None

                if rightChild > upto:
                    childToSwap = leftChild
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        childToSwap = leftChild
                    else:
                        childToSwap = rightChild
                if self.heap[index] < self.heap[childToSwap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break

                index = childToSwap
            else:
                break
