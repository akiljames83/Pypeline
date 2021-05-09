# Pypeline
This is a python library for easy implementation of Data Structures and Algorithms. In future iterations, this library will include plugins for Data Analysis and Machine Learning, specifically for data collection and manipulation.

## Future Work
On the next iteration of Pypeline, we will release a method to pass Python Data Structures to files for seamless integration with R graphing plugins.

## Installation
Install Pypeline v1.0.1 using [pip](https://pip.pypa.io/en/stable/quickstart/):

```bash
$ pip install python-pypeline
```

If version installed is <= v1.0.1 then you need to upgrade to the latest version of Pypeline:

```bash
$ pip install python-pypeline --upgrade
```

To test install, run the following line of code:

```python
>>> import Pypeline
```

## Development
Run all scripts from within the `Pypeline` folder as follows:

```bash
$ ./scripts/run_tests.sh
```

## Data Structures Implemented
*   [AVL Tree](#avl-tree)
*   [Binary Search Tree](#binary-search-tree)
*   [Max Heap](#max-heap)
*   [Min Heap](#min-heap)
*   [Node](#node)
*   [Linked List](#linked-list)
*   [Queue](#queue)
*   [Stack](#stack)
*   [Trie](#trie)
*   [Ternary Search Tree](#ternary-serach-tree)
----------------------
## Sample Implementations

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

# Add Nodes to the Tree; the tree will NOT balance itself
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
### Node
```python
from Pypeline.Pypes.Node import Node

# Instantiation; However, this is meant to be a super class not a stand alone object
node = Node()

# Set Node value; This can be passed into object instantiation as well
node.setVal(10)

# Get value of the Node
_ = node.getVal()

# Set/Swap Visisted (if needed); default is false
node.setVisited() # visted -> true
node.swapVisited() # visited -> false

# Check if Node is Visited
_ = node.isVisited()
```
### Linked List
```python
from Pypeline.Pypes.LinkedList import LinkedList

# Instantiation
linked = LinkedList()

# Insert Value to list (dtype -> any); T.C -> O(1)
for i in range(10):
	linked.insert(i)

# Delete node from the linkedlist T.C -> O(N)
linked.remove(5)

# Get Size of the linkedlist
_ = linked.getSize()

# Traverse List: print all values in linkedlist; T.C -> O(N)
linked.traverseList()

# Convert linkedlist to numpy array; returns the converted array
nplinked = linked.to_array()

# Convert linkedlist to python list; return the converted list
regular_list = linked.to_list()

# Can print linked list and it will display the corresponding python list
print(linked)
```
### Queue
```python
from Pypeline.Pypes.Queue import Queue

# Instantiation of Queue; maxlen property specifies largest size for array
queue = Queue(maxlen=1e9)

# Enqueue data to the queue
for i in range(10):
	queue.enqueue(i)

# Dequeue data from the queue; FIFO
_ = queue.dequeue()

# Peek the front of the queue; returns the value without removing
front = queue.peek()

# Get the size of the queue
size = queue.sizeQueue()

# Check if queue is empty; returns -> type bool
_ = queue.isEmpty()

# Convert queue to numpy array
npqueue = queue.to_array()

# Convert queue to python list
list_queue = queue.to_list()
```
### Stack
```python
from Pypeline.Pypes.Stack import Stack

# Instantiation of Stack; maxlen property specifies largest size for array
stack = Stack(maxlen=1e9)

# Enqueue data to the stack
for i in range(10):
	stack.push(i)

# Dequeue data from the stack; LIFO
_ = stack.pop()

# Peek the top of the stack; returns the value without removing
front = stack.peek()

# Get the size of the queue
size = stack.sizeStack()

# Check if stack is empty; returns -> type bool
_ = stack.isEmpty()

# Convert stack to numpy array
npstack = stack.to_array()

# Convert queue to python list
list_stack = stack.to_list()
```
### Trie
```python
from Pypeline.Pypes.Trie import Trie

# Instantiation
tree = Trie()

# Insert word into the tree
tree.insert('word')
tree.insert('data structure')

# Search for a word in the tree
_ = tree.search('word') # -> returns true if word in tree
_ = tree.search('data') # -> returns false if word not in tree
```
### Ternary Search Tree
```python
from Pypeline.Pypes.TernarySearchTree import TST

# Instantiation
tst = TST()

# Put Key and value into the tree
tst.put("cat",5)
tst.put("dog",10)

# Get the value from the key of the tree
_ = tst.get('cat') # -> returns 5
_ = tst.get("bird") # -> returns -1 if key not in tree
```