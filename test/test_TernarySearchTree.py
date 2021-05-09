from Pypeline.Pypes import TernarySearchTree
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


class TSTTest(unittest.TestCase):
	"""
	Tests for methods in the TST class.
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
		tree = TernarySearchTree.TST()
		tree.put('a', 5)
		assert tree.rootNode.char == 'a'
		assert tree.rootNode.value == 5

	def test_putItem(self):
		tree = TernarySearchTree.TST()
		n = tree.putItem(tree.rootNode, 'a', 5, 0)
		assert n.char == 'a'
		assert n.value == 5

	def test_get(self):
		tree = TernarySearchTree.TST()
		tree.put('a', 5)
		assert tree.get('a') == 5

	def test_getItem(self):
		tree = TernarySearchTree.TST()
		tree.put('a', 5)
		n = tree.getItem(tree.rootNode, 'a', 0)
		assert n.char == 'a'
		assert n.value == 5
