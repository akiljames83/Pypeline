

class Node:
    """ 
    This is a custom node class for the Red Black BST
      
    Attributes:\n
        key: the key used for comparison
        size: the size of the tree
        color: True indicates Red and False indicate a black link
        val: the data stored in the node
        left: Left node child
        right: Right node child
    """

    def __init__(self, key, val, size, color):
        self.key = key
        self.val = val
        self.N = size
        self.color = color
        self.left = None
        self.right = None


def isRed(x):
    """ 
    A helper function to determine if the link is red or not

    Parameters:\n
        x: a node in the tree
    """
    if x is None:
        return False
    return x.color == True


def size(root):
    """ 
    A helper function to determine the size of tree

    Parameters:\n
        root: a root in the tree
    """
    if root == None:
        return 0
    return root.N


def rotateLeft(h):
    """ 
    A helper function to restore the red-black tree order by changing the color of each node and added their sizes together

    Parameters:\n
        h: a node in the tree
    """
    x = h.right
    h.right = x.left
    x.left = h
    x.color = h.color
    h.color = True
    x.N = h.N
    h.N = 1 + size(h.left) + size(h.right)
    return x


def rotateRight(h):
    """ 
    A helper function to restore the red-black tree order by changing the color of each node and added their sizes together

    Parameters:\n
        h: a node in the tree
    """
    x = h.left
    h.left = x.right
    x.right = h
    x.color = h.color
    h.color = True
    x.N = h.N
    h.N = 1 + size(h.left) + size(h.right)
    return x

def flipColors(h):
    """ 
    A helper function to flip the colors of the tree by changing the color of each node

    Parameters:\n
        h: a node in the tree
    """
    h.color = True
    h.left.color = False
    h.left.color = False


def cmp(v1, v2):
    """ 
    A helper function to compare the two values

    Parameters:\n
        v1: first value
        v2: second value
    """
    if v1 < v2:
        return -1
    elif v1 == v2:
        return 0
    else:
        return 1


class redBlackBST:
    """
    Implementation of the Red Black BST

    Attributes:\n
        root: value is set to None first unless Put is called
    """

    ## @brief constructor for the redBlackBST
    #  @details root value is set to None first unless Put is called
    #  @param self the self parameter
    def __init__(self):
        self.root = None

    ## @brief A method that puts the node into the BST
    #  @details calling another helper method to finish the heavy lifting work
    #  @param key the key used for comparison
    #  @param val the value of the node being put
    def put(self, key, val):
        """ 
        A method that puts the node into the BST calling another helper method to finish the heavy lifting work

        Parameters:\n
            key: the key used for comparison
            val: the value of the node being put
        """
        self.root = self.actualPut(self.root, key, val)
        self.root.color = False

    ## @brief A method that puts the node into the BST
    #  @details calling different helper function to ensures the Red black order is preserved
    #  @param key the key used for comparison
    #  @param val the value of the node being put
    #  @param h the node we want to put at

    def actualPut(self, h, key, val) -> Node:
        """ 
        A method that puts the node into the BST calling different helper function to ensures the Red black order is preserved

        Parameters:\n
            key: the key used for comparison
            val: the value of the node being put
            h: the node we want to put at
        """
        if h is None:
            return Node(key, val, 1, True)
        compare = cmp(key, h.key)
        if compare < 0:
            h.left = self.actualPut(h.left, key, val)
        elif compare > 0:
            h.right = self.actualPut(h.right, key, val)
        else:
            h.val = val
        if isRed(h.right) and not isRed(h.left):
            h = rotateLeft(h)
        if isRed(h.left) and isRed(h.left.left):
            h = rotateRight(h)
        if isRed(h.left) and isRed(h.right):
            flipColors(h)
        h.N = size(h.left) + size(h.right) + 1
        return h

    ## @brief A getter for the BST
    #  @details Comparing the key values in logarithmic time to find the node
    #  @param key the key used for comparison

    def get(self, key):
            cur = self.root
            while cur is not None:
                if cur.key == key:
                    return cur
                elif cmp(key, cur.key) < 0:
                    cur = cur.left
                else:
                    cur = cur.right
            return None
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)