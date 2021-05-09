"""
Implementation of the binary search tree

"""

from typing import Optional, Union

class Node(object):
    """ 
    This is a custom node class for the Binary Search Tree
      
    Attributes:\n
        data: The data to be stored in the node
        rightChild: The right child of the current node
        leftChild: The left child of the current node 
    """

    def __init__(self, data: Union[int, float]) -> None:
        """ 
        Constructor of the Node class

        Parameters:\n
            data: the data to be stored in the Node 
        """
        assert (isinstance(data, int) or isinstance(data,float))
        self.data: Union[int, float] = data
        self.leftChild: Optional[Node] = None
        self.rightChild: Optional[Node] = None

class BST(object):
    """ 
    Implementation of the Binary Search Tree (https://en.wikipedia.org/wiki/Binary_search_tree)

    All items on the left are smaller than given node &
    all on the right are larger than the given node
      
    Attributes:\n
        root: The root node of the BST Tree
        size: counter for the number of items inside the tree
    """

    def __init__(self) -> None:
        """ 
        Constructor of the BST class
        """
        self.root: Optional[Union[int, float]] = None
        self.size: int = 0

    def getSize(self) -> int:
        """ 
        Method used to return the size of the BST
        """
        return self.size

    def insert(self, data: Union[int, float]) -> None:
        """ 
        Public method used to insert data into the BST tree

        Parameters:\n
            data: the data to be added to the tree
        """
        assert (isinstance(data, int) or isinstance(data,float))

        # if root node isnt currently defined
        if not self.root:
            self.root = Node(data) # instantiate the root of BTS
            self.size += 1
        else:
            self.__insertNode(data, self.root)

    # Running time complexity of O (logN) -> Only if tree is balanced
    def __insertNode(self, data: Union[int, float], node: Node) -> None:
        """ 
        Private method used to insert data into the BST tree

        Parameters:\n
            data: the data to be added to the tree
            node: the root node of the tree
        """
        assert (isinstance(data, int) or isinstance(data,float))

        if data < node.data:
            if node.leftChild: # if the node has a left child
                # recursive call 
                self.__insertNode(data,node.leftChild)
            else:
                node.leftChild = Node(data)
                self.size += 1
        else:
            if node.rightChild: # if the node has a right child
                self.__insertNode(data,node.rightChild)
            else:
                node.rightChild = Node(data)
                self.size +=1


    def remove(self, data: Union[int, float]) -> None:
        """ 
        Public method used to remove data from the BST tree

        Parameters:\n
            data: the data to be removed from the tree
        """
        assert (isinstance(data, int) or isinstance(data,float))
        if self.root: # if the root exists -> are there nodes
            self.root = self.__removeData(data,self.root)

    # Using the predecessor method of removing data
    def __removeData(self, data: Union[int, float], node: Optional[Node]) -> Optional[Node]:
        """ 
        Private method used to remove data from the BST tree

        Parameters:\n
            data: the data to be removed to the tree
            node: the root node of the tree
        """
        assert (isinstance(data, int) or isinstance(data,float))

        if not node: # this is the base case my guy duuhh
            return node

        if data < node.data: # if smaller
            node.leftChild =  self.__removeData(data,node.leftChild)
        elif data > node.data:
            node.rightChild = self.__removeData(data,node.rightChild)
        else:
            # This means we are at the node we want to remove
            # There are 3 cases for this

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
                # then get rid of the predecessor starting from left child
                # have to call remove node recursively because we will end up with
                # one of the two previous situations
                node.leftChild = self.__removeData(predecessor.data,node.leftChild)
        return node                 

    def __getPredecessor(self, node: Node) -> Node: # get largest value in left subtree
        """ 
        Private method to get the largest value in a subtree

        Parameters:\n
            node: the reference node used to find largest value in its subtree
        """
        if not node.rightChild:
            return node
        return self.__getPredecessor(node.rightChild)

    def getMinValue(self) -> Optional[Union[int, float]]:
        """ 
        Public method used to get the smallest value in the BST
        """
        if self.root: # if there are nodes in the BST
            return self.__getMin(self.root)
        else:
            return None

    def __getMin(self, node: Node) -> Union[int, float]:
        """ 
        Private method used to get the smallest value in the BST

        Parameters:\n
            node: the BST's root node
        """
        if node.leftChild: # if the left child node exists
            return self.__getMin(node.leftChild) # recursively call min
        else:
            return node.data

    def getMaxValue(self) -> Optional[Union[int, float]]:
        """ 
        Public method used to get the largest value in the BST
        """
        if self.root:
            return self.__getMax(self.root)
        else:
            return None

    def __getMax(self, node: Node) -> Union[int, float]:
        """ 
        Private method used to get the largest value in the BST

        Parameters:\n
            node: the BST's root node
        """
        if node.rightChild: # again if the right node exists
            return self.__getMax(node.rightChild) #recursively call func
        else:
            return node.data

    def inOrderTraversal(self) -> None:
        """ 
        Public method used to perform an inOrderTraversal
        """
        if self.root: # if the root node exists
            self.__inOrder(self.root)

    def __inOrder(self, node: None) -> None:
        """ 
        Private method used to perform an inOrderTraversal

        Parameters:\n
            node: the BST's root node
        """
        if node.leftChild: # if the left child exists
            self.__inOrder(node.leftChild) # will evetually print it, if it exists
        
        print("%d" % node.data)

        if node.rightChild:
            self.__inOrder(node.rightChild) # same thing

    def preOrderTraversal(self) -> None:
        """ 
        Public method used to perform an preOrderTraversal
        """
        if self.root: # if the root node exists
            self.__preOrder(self.root)

    def __preOrder(self, node: Node) -> None:
        """ 
        Private method used to perform an preOrderTraversal

        Parameters:\n
            node: the BST's root node
        """
        print("%d" % node.data)

        if node.leftChild: # if the left child exists
            self.__preOrder(node.leftChild) # will evetually print it, if it exists

        if node.rightChild:
            self.__preOrder(node.rightChild) # same thing

    def postOrderTraversal(self) -> None:
        """ 
        Public method used to perform an postOrderTraversal
        """
        if self.root: # if the root node exists
            self.__postOrder(self.root)

    def __postOrder(self, node: Node) -> None:
        """ 
        Private method used to perform an postOrderTraversal

        Parameters:\n
            node: the BST's root node
        """
        if node.leftChild: # if the left child exists
            self.__postOrder(node.leftChild) # will evetually print it, if it exists

        if node.rightChild:
            self.__postOrder(node.rightChild) # same thing

        print("%d" % node.data)
