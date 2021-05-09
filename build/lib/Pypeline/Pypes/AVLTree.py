"""
Implementation of the AVL tree !!

"""

from typing import Any, Optional

class Node(object):
    """ 
    This is a custom node class for the AVL Tree

    Attributes:\n
        data: The data to be stored in the node
        rightChild: The right child of the current node
        leftChild: The left child of the current node
        height: The length of longest path from current not to lead. Used to check if the tree is balanced. 
    """

    def __init__(self, data: Any) -> None:
        """ 
        Constructor of the Node class

        Parameters:\n
            data: the data to be stored in the Node 
        """
        self.data: Any = data
        self.rightChild: Optional[Node] = None
        self.leftChild: Optional[Node] = None
        self.height: int = 0
        

class AVL(object):
    """ 
    Implementation of the AVL Tree (https://en.wikipedia.org/wiki/AVL_tree)
    
    Attributes:\n
        root: The root node of the AVL Tree
    """

    def __init__(self) -> None:
        """ 
        Constructor of the AVL class
        """
        self.root: Optional[Node] = None

    def calcHeight(self, node: Optional[Node]) -> int:
        """ 
        Method used to determine the height of a particular node

        Parameters:\n
            node: the node for which the height is to be calculated
        """
        if not node: # if the node is None
            return -1
        else:
            return node.height

    # if return value > 1, it means left heavy situations -> right rotation
    # if return value < -1, it means right heavy situations -> left rotation
    # if between -1 and 1, it is balanced

    def calcBalance(self, node: Optional[Node]) -> int:
        """ 
        Method used to determine whether a particular node is balanced

        if return value > 1, it means left heavy situations -> right rotation\n
        if return value < -1, it means right heavy situations -> left rotation\n
        otherwise it is balanced\n

        Parameters:\n
            node: the node that will have its level of balance calculated
        """
        if not node:
            return 0
        else: 
            return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def rotateRight(self, node: Node) -> Node:
        """ 
        Method used to perform a right rotation from a particular node.


        Rotations to the right and the left are symmetrical operations. Rotation
        operations are quite fast as it it just updating references O(1) time complexity.

        Parameters:\n
            node: the node that will be reference rotatation point
        """
        tempLeft = node.leftChild
        t = tempLeft.rightChild

        tempLeft.rightChild = node
        node.leftChild = t

        # update node's height by checking left and right sub tree
        node.height = max(self.calcHeight(node.leftChild),self.calcHeight(node.rightChild)) + 1
        tempLeft.height = max(self.calcHeight(tempLeft.leftChild),self.calcHeight(tempLeft.rightChild)) + 1

        # return the new root node
        return tempLeft

    def rotateLeft(self, node: Node) -> Node:
        """ 
        Method used to perform a left rotation from a particular node.

        Rotations to the right and the left are symmetrical operations. Rotation
        operations are quite fast as it it just updating references O(1) time complexity.

        Parameters:\n
            node: the node that will be reference rotatation point
        """
        tempRight = node.rightChild
        t = tempRight.leftChild

        tempRight.leftChild = node
        node.rightChild = t

        # update node's height by checking left and right sub tree
        node.height = max(self.calcHeight(node.leftChild),self.calcHeight(node.rightChild)) + 1
        tempRight.height = max(self.calcHeight(tempRight.leftChild),self.calcHeight(tempRight.rightChild)) + 1

        # return the new root node
        return tempRight

    def insert(self, data: Any) -> None:
        """ 
        Public method used to insert data into the AVL tree

        A check is necessary to ensure the AVL property is not violated. This
        check is performed within the associated helper method `__insertNode`

        Parameters:\n
            data: the data to be added to the tree
        """
        self.root = self.__insertNode(data, self.root)

    def __insertNode(self, data: Any, node: Optional[Node]) -> Node:
        """ 
        Private method used to insert data into the AVL tree as well as
        check if the AVL property has been violated.

        Parameters:\n
            data: the data to be added to the tree
            node: the root node of the tree
        """
        if not node: # base case so plug in the value
            return Node(data)
        else:
            if data < node.data: # call recursively on left subtree to insert
                node.leftChild = self.__insertNode(data, node.leftChild)
            else: # call recursively on right subtree
                node.rightChild = self.__insertNode(data, node.rightChild)

            # update height parameter
            node.height =  max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

            # fixes any errors in the balance of the tree
            return self.__settleViolation(data,node)

    def __settleViolation(self, data: Any, node: Node) -> Node:
        """ 
        Method used to settle AVL violations as they arrise.

        Parameters:\n
            data: the data to be added to the tree
            node: the root node of the tree
        """
        balance = self.calcBalance(node)
        # Case 1: Greater than 1 -> left left heavy -> & current data is smaller than left child so -> simple right rotation
        if balance > 1 and data < node.leftChild.data:
            #print("Doubly left heavy situation...")
            return self.rotateRight(node)

        # Case 2: Less than -1 -> right right heavy -> & current data is smaller than right child  so -> simple left rotation
        elif balance < -1 and data > node.rightChild.data:
            #print("Doubly right heavy situation...")
            return self.rotateLeft(node)
        # Case 3: Left right
        elif balance > 1 and data > node.leftChild.data: # current data is greater than left (so its on right)
            #print("Left-right heavy situation...")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        # Case 4: Right Left
        elif balance < -1 and data < node.rightChild.data:
            #print("Right-left heavy situation...")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

    def traverse(self) -> None:
        """ 
        Method used to perform an inOrderTraversal
        """
        if self.root:
            self.__inOrderTraversal(self.root)
    
    def __inOrderTraversal(self, node: Node) -> None:
        """ 
        Method used to perform an inOrderTraversal

        Parameters:\n
            node: the root node of the tree
        """
        if node.leftChild:
            self.__inOrderTraversal(node.leftChild)

        print("%s" % node.data)

        if node.rightChild:
            self.__inOrderTraversal(node.rightChild)

    def remove(self, data: Any) -> None:
        """ 
        Public method used to remove some piece of data from the tree

        Parameters:\n
            data: the data to be removed to the tree
        """
        if self.root: # if the root exists -> there are nodes
            self.root = self.__removeData(data, self.root)

    def __removeData(self, data: Any, node: Optional[Node]) -> Optional[Node]:
        """ 
        Private method used to remove some piece of data from the tree.

        The predecessor method of removing data is used.

        Parameters:\n
            data: the data to be removed to the tree
            node: the root node of the tree
        """
        if not node: # this is the base case my guy duuhh
            return node

        if data < node.data: # if smaller
            node.leftChild =  self.__removeData(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.__removeData(data, node.rightChild)
        else:
            # 1: if there are no children -> Leaf Node
            if not node.leftChild and not node.rightChild:
                #print("Removing leaf node...")
                del node
                return None
            elif not node.leftChild: # no left but would have right ^
                #print("Removing node with right child...")
                rightChild = node.rightChild
                del node
                return rightChild
            elif not node.rightChild: # no right child
                #print("Removing node with left child...")
                leftChild = node.leftChild
                del node
                return leftChild
            else:
                #print("Removing node with two children...")
                predecessor = self.__getPredecessor(node.leftChild)
                node.data = predecessor.data
                node.leftChild = self.__removeData(predecessor.data, node.leftChild)

        if not node:
            return node

        node.height = max(self.calcHeight(node.leftChild),self.calcHeight(node.rightChild)) + 1
        
        balance = self.calcBalance(node)

        # Case 1: Greater than 1 -> left left heavy -> & current data is smaller than left child so -> simple right rotation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            #print("Doubly left heavy situation...")
            return self.rotateRight(node)

        # Case 2: Less than -1 -> right right heavy -> & current data is smaller than right child  so -> simple left rotation
        elif balance < -1 and self.calcBalance(node.rightChild) <= 0:
            #print("Doubly right heavy situation...")
            return self.rotateLeft(node)
        # Case 3: Left right
        elif balance > 1 and self.calcBalance(node.leftChild) < 0: # current data is greater than left (so its on right)
            #print("Left-right heavy situation...")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        # Case 4: Right Left
        elif balance < -1 and self.calcBalance(node.rightChild) > 0:
            #print("Right-left heavy situation...")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node                 

    def __getPredecessor(self, node: Node) -> Node:
        """ 
        Private method to get the largest value in a subtree

        Parameters:\n
            node: the reference node used to find largest value in its subtree
        """
        if not node.rightChild:
            return node
        return self.__getPredecessor(node.rightChild)