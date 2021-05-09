"""
Implementation of the Doubly Linked List

@author Chenghao Gong gongc12
"""

class Node:
    """ 
    This is a custom node class for the Doubly Linked List
      
    Attributes:\n
        data: The data to be stored in the node
        next: The next node in the linked list
        prev: The previous node in the linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """ 
    The constructor for the doubly linked list
      
    Attributes:\n
        head: The head node in the linked list
    """
    def __init__(self):
        self.head = None
        self.size = 0

    """ 
    Given a reference to the head of a list and an integer, inserts a new node on the front of list

    Parameters:\n
        new_data: a new value being inserted to the list
    """
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        self.size += 1

    """ 
    Given a reference to the head of a list and an integer, inserts a new node on the front of list

    Parameters:\n
        new_data: a new value being inserted to the list
        prev_node: the node being inserted after
    """
    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("the given previous node cannot be NULL")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
        self.size += 1

    """ 
    Given a reference to the head of DLL and integer,appends a new node at the end

    Parameters:\n
        new_data: a new value being inserted to the list
    """
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        self.size += 1
        return

    """ 
    This function prints contents of linked list starting from the given node

    Parameters:\n
        node: the starting node for a given linkedlist
    """
    ## @brief a accessor for the module
    #  @details 
    #  @param self reference to the object
    #  @param 
    def printList(self, node):
        print("\nTraversal in forward direction")
        while node:
            print(" % d" % (node.data))
            last = node
            node = node.next

    ##  @brief A getter method for the linkedlist
    #   @details Return the state variable head
    #   @param self reference to the object
    #   @return the first element in the linked list

    def getFirst(self):
        return self.head

    ##  @brief A getter method for the linkedlist
    #   @details Return the state variable
    #   @param self reference to the object
    #   @return the last element in the linked list
    def getLast(self):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        return cur
    ##  @brief Check if element already present in the linked list
    #   @details if the node contains object, __eq__ method must be overwritten in the class
    #   @param self reference to the object
    #   @return boolean value indicate the result
    def contains(self,element):
        cur = self.head
        while cur is not None:
            if cur.data == element:
                return True
            cur = cur.next
        return False

    ##  @brief A getter method for the linkedlist
    #   @details Return the state variable size
    #   @param self reference to the object
    #   @return the size of the current linkedlist

    def sizeOf(self):
        return self.size

    ##  @brief A getter method for the linked list
    #   @details Return the node
    #   @param self reference to the object
    #   @param index an index specified the position
    #   @return the node in the givein index

    def get(self,index):
        if index >= self.size or index < 0:
            raise Exception("Not retriveable")
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur

    ##  @brief A setter used to change the linked list state
    #   @details remove the element in the given index
    #   @param self reference to the object
    #   @param index an index specified the position
    def remove(self, index):
        if index >= self.size or index < 0:
            raise Exception("Not retriveable")
        cur = self.head
        for i in range(index):
            cur = cur.next
        if cur != self.head:
            prev = cur.prev
            prev.next = cur.next
        else:
            self.head = cur.next










