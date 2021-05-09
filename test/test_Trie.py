from Pypeline.Pypes.Trie import Trie
import pytest
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


class TrieTest(unittest.TestCase):
	"""
	Tests for methods in the Trie class.
	"""

	@classmethod
	def setUpClass(cls):
		pass #TODO

	@classmethod
	def tearDownClass(cls):
		pass #TODO

	def setUp(self):
		self.tree = Trie()

	def tearDown(self):
		self.tree = None

	def test_insert(self):
		self.tree.insert('test')
		assert self.tree.search("test")

	def test_search(self):

		self.tree.insert('hack')
		assert self.tree.search("hack")

		self.tree.insert('hackathon')
		assert self.tree.search("hackathon")

		self.tree.insert('hac')
		assert self.tree.search("hac")

		assert self.tree.search("ha") == False
		assert self.tree.search("h") == False

		with pytest.raises(TypeError):
			self.tree.insert()
			self.tree.insert(12)
			self.tree.insert(['test'])