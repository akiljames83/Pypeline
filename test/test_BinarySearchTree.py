from Pypeline.Pypes.BinarySearchTree import BST 
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
		pass #TODO

	def tearDown(self):
		pass #TODO


class BSTTest(unittest.TestCase):
	"""
	Tests for methods in the BST class.
	"""

	@classmethod
	def setUpClass(cls):
		cls.vals = [10.1, 3, 20, 12, 9, 5, 30, 21]

	@classmethod
	def tearDownClass(cls):
		pass #TODO

	def setUp(self):
		self.bst = BST()

	def tearDown(self):
		self.bst = None

	def test_getSize(self):
		self.bst.insert(1)
		assert self.bst.getSize() == 1

	def test_insert(self):
		[self.bst.insert(x) for x in self.vals]
		assert self.bst.getSize() == 8

	def test_remove(self):
		[self.bst.insert(x) for x in self.vals]
		[self.bst.remove(x) for x in self.vals]
		assert not(self.bst.inOrderTraversal())

	def test_getMinValue(self):
		self.bst.insert(2)
		self.bst.insert(200)
		assert self.bst.getMinValue() == 2

	def test_getMaxValue(self):
		self.bst.insert(100)
		self.bst.insert(2)
		assert self.bst.getMaxValue() == 100

	def test_inOrderTraversal(self):
		# print(self.vals)
		# [self.bst.insert(x) for x in self.vals]
		# lst = self.bst.inOrderTraversal() 
		# assert lst == sorted(self.vals)
		pass # Can't really test this or the following as they interact with the console output.

	def test_preOrderTraversal(self):
		print(self.bst.preOrderTraversal())
		pass
		# raise NotImplementedError() #TODO: test preOrderTraversal

	def test_postOrderTraversal(self):
		print(self.bst.postOrderTraversal())
		pass
		# raise NotImplementedError() #TODO: test postOrderTraversal
