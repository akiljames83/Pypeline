from Pypeline.Pypes.Node import Node
import unittest

class NodeTest(unittest.TestCase):
	"""
	Tests for methods in the Node class.
	"""

	@classmethod
	def setUpClass(cls):
		pass #TODO

	@classmethod
	def tearDownClass(cls):
		pass #TODO

	def setUp(self):
		self.node = Node()

	def tearDown(self):
		self.node = None

	def test_setVisited(self):
		self.node.setVal(10)
		self.node.setVisited()
		assert self.node.isVisited() == True

	def test_swapVisited(self):
		self.node.swapVisited()
		assert self.node.isVisited()
		self.node.setVal(10)
		self.node.setVisited()
		self.node.swapVisited()
		assert self.node.isVisited() == False

	def test_isVisited(self):
		assert self.node.isVisited() == False

	def test_setVal(self):
		self.node.setVal(10)
		assert self.node.getVal() == 10

	def test_getVal(self):
		assert self.node.getVal() == None
		self.node.setVal(10)
		assert self.node.getVal() == 10
