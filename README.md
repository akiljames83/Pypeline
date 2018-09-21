# Pypeline
This is a python library for easy implementation of Data Structures and Algorithms. In future iterations, this library will include plugins for Data Analysis and Machine Learning, specifically for data collection and manipulation.

## Future Work
On the next iteration of Pypeline, we will release a method to pass Python Data Structures to files seamless integration with R graphing plugins.

## Installation
Install Pypeline v0.3.2 using [pip](https://pip.pypa.io/en/stable/quickstart/):

`pip install python-pypeline`

If version installed is <=0.3.1 then you need to upgrade to the latest version of Pypeline:

`pip install python-pypeline --upgrade`

To test install, run the following line of code:

`import Pypeline`

## Data Structures Implemented
*   [AVL Tree](#avl-tree)
*   [Binary Search Tree](#binary-search-tree)
*   [Max Heap](#max-heap)
*   [Min Heap](#min-heap)
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

### Max Heap
```python
from Pypeline.Pypes.MaxHeap import MaxHeap

# Instantiate the Max Heap; the list can be passed in on instantiation or with a builtin method
maxheap = MaxHeap()

# Convert list to MaxHeap
maxheap.heapify([2, 4 , 10, 8])

# Merge heap with another list
maxheap.merge([1, 5, 3, 7])

# Pop largest value from the heap
_ = maxheap.heappop()

# Insert value (type int or float) into the Heap
maxheap.heappush(20)

# Convert heap into numpy array
np_maxheap = maxheap.to_array()

# Print the Max Heap Contents; Currently the Data Structure is not iterable
print(maxheap)
```
### Min Heap
```python
from Pypeline.Pypes.MinHeap import MinHeap

# Instantiate the Min Heap; the list can be passed in on instantiation or with a builtin method
minheap = MinHeap()

# Convert list to MinHeap
minheap.heapify([2, 4 , 10, 8])

# Merge heap with another list
minheap.merge([1, 5, 3, 7])

# Pop smallest value from the heap
_ = minheap.heappop()

# Insert value (type int or float) into the Heap
minheap.heappush(20)

# Convert heap into numpy array
np_minheap = minheap.to_array()

# Print the Min Heap Contents; Currently the Data Structure is not iterable
print(minheap)
```
