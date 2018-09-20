## Implementation of the binary search tree
class Node(object):

	def __init__(self,data):
		assert (isinstance(data, int) or isinstance(data,float))
		self.data = data
		self.leftChild = None
		self.rightChild = None

class BST(object):

	# All items on the left are smaller than given node &
	# all on the right are larger than the given node
	def __init__(self):
		self.root = None
		self.size = 0

	def getSize(self):
		return self.size

	def insert(self,data):
		# if root node isnt cyrrently defined
		assert (isinstance(data, int) or isinstance(data,float))
		if not self.root:
			self.root = Node(data) # instantiate the root of BTS
			self.size += 1
		else:
			self.insertNode(data,self.root)

	# Running time complexity of O (logN) -> Only if tree is balanced
	def insertNode(self,data,node):
		assert (isinstance(data, int) or isinstance(data,float))
		if data < node.data:
			if node.leftChild: # if the node has a left child
				# recursive call 
				self.insertNode(data,node.leftChild)
			else:
				node.leftChild = Node(data)
				self.size += 1
		else:
			if node.rightChild: # if the node has a right child
				self.insertNode(data,node.rightChild)
			else:
				node.rightChild = Node(data)
				self.size +=1


	def remove(self,data):
		assert (isinstance(data, int) or isinstance(data,float))
		if self.root: # if the root exists -> are there nodes
			self.root = self.removeData(data,self.root)

	# Using the predecessor method of removing data
	def removeData(self,data,node):
		assert (isinstance(data, int) or isinstance(data,float))
		if not node: # this is the base case my guy duuhh
			return node

		if data < node.data: # if smaller
			node.leftChild =  self.removeData(data,node.leftChild)
		elif data > node.data:
			node.rightChild = self.removeData(data,node.rightChild)
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
				predecessor = self.getPredecessor(node.leftChild)
				node.data = predecessor.data
				# then get rid of the predecessor starting from left child
				# have to call remove node recursively because we will end up with
				# one of the two previous situations
				node.leftChild = self.removeData(predecessor.data,node.leftChild)
		return node 				

	def getPredecessor(self,node): # get largest value in left subtree
		if not node.rightChild:
			return node
		return self.getPredecessor(node.rightChild)

	def getMinValue(self):
		if self.root: # if there are nodes in the BST
			return self.getMin(self.root)
		else:
			return None

	def getMin(self,node):
		if node.leftChild: # if the left child node exists
			return self.getMin(node.leftChild) # recursively call min
		else:
			return node.data

	def getMaxValue(self):
		if self.root:
			return self.getMax(self.root)
		else:
			return None

	def getMax(self,node):
		if node.rightChild: # again if the right node exists
			return self.getMax(node.rightChild) #recursively call func
		else:
			return node.data

	def inOrderTraversal(self):
		if self.root: # if the root node exists
			self.inOrder(self.root)

	def inOrder(self,node):
		if node.leftChild: # if the left child exists
			self.inOrder(node.leftChild) # will evetually print it, if it exists
		
		print("%d" % node.data)

		if node.rightChild:
			self.inOrder(node.rightChild) # same thing

	def PeOrderTraversal(self):
		if self.root: # if the root node exists
			self.PreOrder(self.root)

	def PreOrder(self,node):
		print("%d" % node.data)

		if node.leftChild: # if the left child exists
			self.PreOrder(node.leftChild) # will evetually print it, if it exists

		if node.rightChild:
			self.PreOrder(node.rightChild) # same thing

	def PostOrderTraversal(self):
		if self.root: # if the root node exists
			self.PostOrder(self.root)

	def PostOrder(self,node):
		if node.leftChild: # if the left child exists
			self.PostOrder(node.leftChild) # will evetually print it, if it exists

		if node.rightChild:
			self.PostOrder(node.rightChild) # same thing

		print("%d" % node.data)

if __name__ == "__main__":
	bst = BST()
	# Also works with Characters, strings, doubles etc
	bst.insert(10)
	bst.insert(3)
	bst.insert(20)
	bst.insert(12)
	bst.insert(1)
	bst.insert(5)
	bst.insert(30)
	bst.insert(21)

	print("Min Value: {}".format(bst.getMinValue()))
	print("Max Value: {}".format(bst.getMaxValue()))
	bst.inOrderTraversal()

	bst.remove(30)
	bst.remove(21)
	bst.remove(1)
	bst.remove(10)
	bst.inOrderTraversal()

