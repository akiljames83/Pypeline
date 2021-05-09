"""
Implementation of the Trie Data Structure

"""

from typing import Dict

class Node(object):
    """ 
    This is a custom node class for the Trie
      
    Attributes:\n
        char: The char to be stored
        children: Dictionary of the nodes children
        word_finished: Inidicate whether the word is finished at this node
        counter: number of word occurences using this node
    """

    def __init__(self,char) -> None:
        self.char: str = char
        self.children: Dict[str, Node] = {}
        self.word_finished: bool = False
        self.counter: int = 0

class Trie(object):
    """
    Implementation of the Trie Data Structure (https://en.wikipedia.org/wiki/Trie)

    A type of search tree, a tree data structure used for locating specific keys from within a set

    """

    def __init__(self) -> None:
        self.root: Node = Node('*')

    def insert(self, word: str) -> None:
        if type(word) != str:
            raise TypeError(f"Object of type {type(word)} cannot be inserted into trie since only str is supported")

        current = self.root
        for char in word:
            if char in current.children: # essentially counting char occurences
                current = current.children[char]
                current.counter += 1
            else: # if not already defined, generate a new node
                new_node = Node(char)
                current.children[char] = new_node
                current = new_node
                current.counter += 1
        current.word_finished = True # when finished flag!! 

    def search(self, word: str) -> bool:
        if not self.root.children: # if there are no children of the root, no words to search
            return False
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        if current.word_finished:
            return True
        return False
