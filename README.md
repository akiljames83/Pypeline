# Pypeline
This is a python library for easy implementation of Data Structures and Algorithms. In future iterations, this library will include plugins for Data Analysis and Machine Learning, specifically for data collection and manipulation.

## Future Work
On next iteration of pypeline, we plan on making an easy way to pass python data structures to files to be read for R reading and graphing.

## Installation
Install Pypeline v0.3.2 using [pip](https://pip.pypa.io/en/stable/quickstart/):

`<pip install python-pypeline>`

If version installed is <=0.3.1 then you need to upgrade the version Pypeline:

`<pip install python-pypeline --upgrade>`

To test install, run the following line of code:

`import Pypeline`

## Data Structures Implemented
*   [AVL Tree](#avl-tree)
*   [Binary Search Tree](#binary-search-tree)
*   Max Heap
*   Min Heap
*   Node
*   Linked List
*   Queue
*   Stack
*   Trie
*   Ternary Search Tree
----------------------
## A Simple Exam

### AVL Tree
```python
from Pypeline.Pypes.AVLTree import AVL

# Instantiate AVL Tree
avl = AVL()

# Add Nodes to the Tree; the tree will automatically balance itself
for i in range(10):
  avl.insert(i)

# Display the AVL Tree using an In Order Traversal
avl.traverse() # will display numbers 1 - 10

# Remove nodes from the Tree
avl.remove(5)
```

### Binary Search Tree
```python
from Pypeline.Pypes.BinarySearchTree import BST

# Instantiate Binary Search Tree
bst = BST()

# Add Nodes to the Tree; the tree will automatically balance itself
for i in range(10):
  bst.insert(i)

# Get size of the Tree
bst_size = bst.getSize()

# Display the BST using an In Order Traversal; can also use preOrderTraversal and postOrderTraversal
bst.inOrderTraversal() # will display numbers 1 - 10

# Remove nodes from the Tree
bst.remove(5)

# Get min value and max value
bst_min, bst_max = bst.getMinValue(), bst.getMaxValue()
```
