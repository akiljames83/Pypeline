from Pypeline.Pypes import RedBlackBST
import unittest

class RedBlackBSTTest(unittest.TestCase):
	"""
	Tests for functions in the RedBlackBST module.
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

	def test_isRed(self):
		node = RedBlackBST.Node(key=1, val=3, size=0, color=True)
		assert RedBlackBST.isRed(node) == True

	def test_size(self):
		node = RedBlackBST.Node(key=1, val=3, size=0, color=True)
		assert RedBlackBST.size(node) == 0

	def test_rotateLeft(self):
		pass

	def test_rotateRight(self):
		pass

	def test_flipColors(self):
		pass

	def test_cmp(self):
		pass

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


class redBlackBSTTest(unittest.TestCase):
	"""
	Tests for methods in the redBlackBST class.
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

	def test_put(self):
		tree = RedBlackBST.redBlackBST()
		tree.put(1, 3)
		assert tree.root.val == 3

	def test_actualPut(self):
		tree = RedBlackBST.redBlackBST()
		tree.root = tree.actualPut(tree.root, 1, 3)
		assert tree.root.val == 3
