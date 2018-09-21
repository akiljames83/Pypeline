'''
Implementation of the node object
'''
class Node(object):

	def __init__(self,val=None):
		'''
		Base for node object containing node value and visited state.
		val -> Any data type
		visited -> bool
		'''
		self.val = val
		self.visited = False

	def setVisited(self):
		self.visited = True

	def swapVisited(self):
		self.visited = not self.visited

	def isVisited(self):
		return self.visited

	def setVal(self,val):
		self.val = val

	def getVal(self):
		return self.val