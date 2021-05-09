"""
Implementation of the node object

"""

from typing import Any, Optional

class Node(object):

    def __init__(self, val: Any=None):
        '''
        Base for node object containing node value and visited state.
        val -> Any data type
        visited -> bool
        '''
        self.val: Any = val
        self.visited: bool = False

    def setVisited(self) -> None:
        self.visited = True

    def swapVisited(self) -> None:
        self.visited = not self.visited

    def isVisited(self) -> bool:
        return self.visited

    def setVal(self, val) -> None:
        self.val = val

    def getVal(self) -> Any:
        return self.val