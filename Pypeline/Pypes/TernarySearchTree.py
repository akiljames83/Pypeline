"""
Implementation of the Ternay Search Tree

"""

from typing import Any, Optional

class Node(object):
    """ 
    This is a custom node class for the Doubly Linked List
      
    Attributes:\n
        char: The char to be stored
        leftNode: The left node child
        rightNode: The right node child
        middleNode: The middle node child
        value: The value associated with the char
    """
    def __init__(self, char: str):
        self.char: str = char
        self.leftNode: Optional[Any] = None
        self.rightNode: Optional[Any] = None
        self.middleNode: Optional[Node] = None
        self.value: int = 0

class TST(object):
    """
    Implementation of the Ternay Search Tree (https://en.wikipedia.org/wiki/Ternary_search_tree)

    A type of trie (sometimes called a prefix tree) where nodes are arranged in a manner similar to a binary search tree,
    but with up to three children rather than the binary tree's limit of two.

    """
    def __init__(self) -> None:
        self.rootNode = None

    def put(self, key: str, value: int):
        assert (isinstance(key, str))
        self.rootNode = self.putItem(self.rootNode, key, value, 0)

    def putItem(self, node: Optional[Node], key: int, value: Any, index: int) -> Node: # key -> the string; index -> index of string
        c = key[index]

        if node == None:
            node = Node(c) # update the given node

        if c < node.char:
            # dont increment index yet, as in the example, it still has to be considered
            node.leftNode = self.putItem(node.leftNode, key,value,index)

        elif c > node.char:
            # dont increment index yet, as in the example, it still has to be considered
            node.rightNode = self.putItem(node.rightNode, key,value,index)

        elif index < len(key) -1: # and not and the end of the string
            # increment cause we will be going to the middle child through the node list
            index += 1
            node.middleNode = self.putItem(node.middleNode, key, value, index)
        else: # now we are at the last index of the string so we can update the value
            node.value = value

        return node

    def get(self, key: int) -> int:

        node = self.getItem(self.rootNode, key, 0) 

        if node == None:
            return -1 # the key is not in the tree

        return node.value

    def getItem(self,node: Optional[Node], key: str, index: int) -> Optional[Node]:
        if node == None:
            return node

        c = key[index]

        # recursive implementation
        if c < node.char: # go left
            return self.getItem(node.leftNode, key, index)
        elif c > node.char: # go right
            return self.getItem(node.rightNode, key, index)
        elif index < len(key) -1: # if we are not at the strings lengt
            index += 1
            return self.getItem(node.middleNode, key, index)
        else: # we would be at the last node at this point
            return node
        
if __name__ == "__main__":
    tst = TST()

    tst.put("cat",5)
    tst.put("dog",30)
    tst.put("jack",19)
    tst.put("robby",12)

    print("The value of cat is: {}".format(tst.get("cat")))
    print("The value of robby is: {}".format(tst.get("robby")))

    print("Updating...")
    tst.put("robby",27)
    print("The value of cat is: {}".format(tst.get("roby")))
