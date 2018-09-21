# Implementing the TST

class Node(object):
	"""docstring for Node"""
	def __init__(self, char):
		self.char = char
		self.leftNode = None
		self.rightNode = None
		self.middleNode = None
		self.value = 0

class TST(object):
	"""docstring for TST"""
	def __init__(self):
		self.rootNode = None

	def put(self,key,value):
		assert (isinstance(key, basestring))
		self.rootNode = self.putItem(self.rootNode, key, value, 0)

	def putItem(self, node, key, value, index): # key -> the string; index -> index of string
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

	def get(self, key):

		node = self.getItem(self.rootNode, key, 0) 

		if node == None:
			return -1 # the key is not in the tree

		return node.value

	def getItem(self,node, key, index):
		if node == None:
			return None
		c = key[index]

		# recursive implementation
		if c < node.char: # go left
			return self.getItem(node.leftNode,key,index)
		elif c > node.char: # go right
			return self.getItem(node.rightNode,key,index)
		elif index < len(key) -1: # if we are not at the strings lengt
			index += 1
			return self.getItem(node.middleNode,key,index)
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
