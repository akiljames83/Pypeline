## Implementation of the AVL tree !!
'''
- still need to make pre order and post order traversal
'''
class Node(object):

	def __init__(self,data):
		self.data = data
		self.rightChild = None
		self.leftChild = None
		self.height = 0 # helps with checking if tree is balanced
		# Height of Node: length of longest path from it to leaf

class AVL(object):

	def __init__(self):
		self.root = None

	def calcHeight(self, node):
		if not node: # if the node is None
			return -1
		else:
			return node.height

	# if return value > 1, it means left heavy situations -> right rotation
	# if return value < -1, it means right heavy situations -> left rotation
	# if between -1 and 1, it is balanced

	def calcBalance(self, node):
		if not node:
			return 0
		else: 
			return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

	# Rotations to the right and the left are symmetrical operations
	# Rotation operations are quite fast as it it just updating references O(1) time complexity
	def rotateRight(self,node):
		#print("Rotating to the right on node %d" % node.data)
		tempLeft = node.leftChild
		t = tempLeft.rightChild

		tempLeft.rightChild = node
		node.leftChild = t

		# update node's height by checking left and right sub tree
		node.height = max(self.calcHeight(node.leftChild),self.calcHeight(node.rightChild)) + 1
		tempLeft.height = max(self.calcHeight(tempLeft.leftChild),self.calcHeight(tempLeft.rightChild)) + 1

		# return the new root node
		return tempLeft

	def rotateLeft(self,node):
		#print("Rotating to the left on node %d" % node.data)
		tempRight = node.rightChild
		t = tempRight.leftChild

		tempRight.leftChild = node
		node.rightChild = t

		# update node's height by checking left and right sub tree
		node.height = max(self.calcHeight(node.leftChild),self.calcHeight(node.rightChild)) + 1
		tempRight.height = max(self.calcHeight(tempRight.leftChild),self.calcHeight(tempRight.rightChild)) + 1

		# return the new root node
		return tempRight

	# Inserting data into AVL tree
	# need to check if we violated the AVL property
	def insert(self,data):
		self.root = self.insertNode(data,self.root)

	def insertNode(self,data,node):
		if not node: # base case so plug in the value
			return Node(data)
		else:
			if data < node.data: # call recursively on left subtree to insert
				node.leftChild = self.insertNode(data, node.leftChild)
			else: # call recursively on right subtree
				node.rightChild = self.insertNode(data,node.rightChild)

			# update height parameter
			node.height =  max(self.calcHeight(node.leftChild),self.calcHeight(node.rightChild)) + 1

			# fixes any errors in the balance of the tree
			return self.settleViolation(data,node)

	def settleViolation(self,data,node):
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

	def traverse(self):
		if self.root:
			self.inOrderTraversal(self.root)
	
	def inOrderTraversal(self, node):
		if node.leftChild:
			self.inOrderTraversal(node.leftChild)

		print("%s" % node.data)

		if node.rightChild:
			self.inOrderTraversal(node.rightChild)

	# Removing data:
	def remove(self,data):
		if self.root: # if the root exists -> there are nodes
			self.root = self.removeData(data,self.root)

	# Using the predecessor method of removing data
	def removeData(self,data,node):
		if not node: # this is the base case my guy duuhh
			return node

		if data < node.data: # if smaller
			node.leftChild =  self.removeData(data,node.leftChild)
		elif data > node.data:
			node.rightChild = self.removeData(data,node.rightChild)
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
				predecessor = self.getPredecessor(node.leftChild)
				node.data = predecessor.data
				node.leftChild = self.removeData(predecessor.data,node.leftChild)

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

	def getPredecessor(self,node): # get largest value in left subtree
		if not node.rightChild:
			return node
		return self.getPredecessor(node.rightChild)

if __name__ == "__main__":
	avl = AVL()
	avl.insert(10)
	avl.insert(20)
	avl.insert(5)
	avl.insert(6)
	avl.insert(15)


	avl.traverse()
	avl.remove(15)
	avl.remove(20)
	avl.traverse()
