from Pypeline.Pypes.LinkedList import LinkedList, Node
import numpy as np
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


class LinkedListTest(unittest.TestCase):
	"""
	Tests for methods in the LinkedList class.
	"""

	@classmethod
	def setUpClass(cls):
		cls.vals = [12, 3, 78, 5]

	@classmethod
	def tearDownClass(cls):
		pass #TODO

	def setUp(self):
		self.ll = LinkedList()

		# linkedlist.traverseList()
		# print("Size of the linked list is {}.".format(linkedlist.getSize()))

		# linkedlist.remove(5)
		# linkedlist.remove(12)
		# linkedlist.remove(3)
		# print("Items deleted from list.")
		# linkedlist.traverseList()
		# linkedlist.remove(78)
		# linkedlist.traverseList()
		# print("Size of linkedlist now is %d." % linkedlist.getSize())

	def tearDown(self):
		self.ll = None

	def test_insert(self):
		[self.ll.insert(x) for x in self.vals[:-1]]
		assert self.ll.size == len(self.vals) - 1 

	def test_insertEnd(self):
		[self.ll.insert(x) for x in self.vals[:-1]]
		self.ll.insertEnd(self.vals[-1])
		node = self.ll.head
		while node.nextNode:
			node = node.nextNode
		assert node.data == self.vals[-1]

	def test_getSize(self):
		[self.ll.insert(x) for x in self.vals]
		assert self.ll.getSize() == len(self.vals)

	def test_getSize2(self):
		[self.ll.insert(x) for x in self.vals]
		assert self.ll.getSize2() == len(self.vals)

	def test_remove(self):
		[self.ll.insert(x) for x in self.vals]
		self.ll.remove(78)
		self.ll.remove(12)
		assert self.ll.head.data == 5
		assert self.ll.size == 2


	def test_to_array(self):
		[self.ll.insert(x) for x in self.vals]
		arr = self.ll.to_array()
		assert type(arr) == np.ndarray
		assert (np.array(self.vals) == arr).all()

	def test_to_list(self):
		[self.ll.insert(x) for x in self.vals]
		arr = self.ll.to_list()
		assert type(arr) == list
		assert self.vals == arr