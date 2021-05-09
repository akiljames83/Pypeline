"""
Implementation of the linked list

"""

from typing import Any, List, Optional

import numpy as np

class Node(object):
    """ 
    This is a custom node class for the Linked List
      
    Attributes:\n
        data: The data to be stored in the node
        nextNode: Reference to the next node
    """

    def __init__(self, data: Any) -> None: # instantiates data in the node
        self.data: None = data
        self.nextNode: Optional[Node] = None # reference to the next node

class LinkedList(object):
    """
    Implementation of the linked list (https://en.wikipedia.org/wiki/Linked_list)

    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None # identiify head of the list
        self.size: int = 0 # initialize length to be zero
        self.linkedlist: List[Any] = []

    def __str__(self) -> str:
        return str(self.linkedlist)

    def __repr__(self) -> str:
        return str(self.linkedlist)

    def insert(self, data: Any) -> None:
        self.size += 1
        #instantiate a new node
        newNode = Node(data)

        # if head of ll not defined, set it
        if not self.head:
            self.head = newNode
        # if it is, this new node becomes head of ll
        else: # essentially just updating pointers
            newNode.nextNode = self.head
            self.head = newNode
        self.linkedlist.append(data)

    # insert item to the end of the list; O(N) time complexity
    def insertEnd(self, data: Any) -> None:
        self.size +=1
        newNode = Node(data)
        #print(newNode,newNode.nextNode)
        actualNode = self.head
        #print(actualNode,actualNode.nextNode)

        # while the following node is not None (not the end of ll)
        while actualNode.nextNode is not None:
            #print(actualNode.nextNode)
            actualNode = actualNode.nextNode # increment
            # brings us to last item

        actualNode.nextNode = newNode
        self.linkedlist.append(data)

    # checks size of the ll; O(1) time complexity
    def getSize(self) -> int: 
        return self.size

    # calculates the size of the ll O(N) time complexity; not very efficient
    def getSize2(self) -> int:
        actualNode = self.head
        size = 0

        while actualNode is not None:
            # increment the size, and shift to next node in the ll
            size +=1
            actualNode = actualNode.nextNode
        return size

    def traverseList(self) -> None:
        actualNode = self.head

        while actualNode is not None:
            # print current data
            print("%d " % actualNode.data)
            # go to he next node in ll
            actualNode = actualNode.nextNode

    # define remove method for particular data O(N) time complexity
    def remove(self, data: Any) -> None:
        # if there is no head in the list, then cant create a list
        if self.head is None:
            return
        self.size -= 1

        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        # at this point, we are at the node we want to get rid of
        if previousNode is None: # if we are at the head
            self.head = currentNode.nextNode

        else: # if not at the head
            # change the pointer
            previousNode.nextNode = currentNode.nextNode

        self.linkedlist.pop(self.linkedlist.index(data))

    def to_array(self) -> Any:
        return np.array(self.linkedlist)

    def to_list(self) -> List[Any]:
        return self.linkedlist
