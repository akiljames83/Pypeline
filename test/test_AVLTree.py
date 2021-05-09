from Pypeline.Pypes.AVLTree import AVL, Node
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


class AVLTest(unittest.TestCase):
	"""
	Tests for methods in the AVL class.
	"""

	@classmethod
	def setUpClass(cls):
		pass #TODO

	@classmethod
	def tearDownClass(cls):
		pass #TODO

	def setUp(self):
		self.avl = AVL()

		# self.avl.traverse()
		# self.avl.remove(15)
		# self.avl.remove(20)
		# self.avl.traverse()
		pass #TODO

	def tearDown(self):
		self.avl = None

	def test_AVL_rebalance(self):
		# This test will check for both left and right rotations with a simple 3-node tree
		# TODO: LL and RR rotations
		self.avl.insert(20)
		assert not(self.avl.root.leftChild and self.avl.root.rightChild)
		self.avl.insert(4)
		assert self.avl.root.leftChild.data == 4
		self.avl.insert(15)
		assert self.avl.root.data == 15 and self.avl.root.rightChild.data == 20
		self.avl.remove(15)
		assert self.avl.root.data == 4 and self.avl.root.rightChild.data == 20
		self.avl.remove(4)
		self.avl.insert(4)
		assert self.avl.root.data == 20 and self.avl.root.leftChild.data == 4
		self.avl.insert(8)
		assert self.avl.root.data == 8 and self.avl.root.leftChild.data == 4
