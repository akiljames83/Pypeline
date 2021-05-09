from Pypeline.Pypes.DoublyLinkedList import DoublyLinkedList, Node
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


class DoublyLinkedListTest(unittest.TestCase):
	"""
	Tests for methods in the DoublyLinkedList class.
	"""

	@classmethod
	def setUpClass(cls):
		pass #TODO

	@classmethod
	def tearDownClass(cls):
		pass #TODO

	def setUp(self):
		self.dll = DoublyLinkedList()

	def tearDown(self):
		self.dll = None

	def test_push(self):
		self.dll.push(0)
		assert self.dll.head.data == 0
		[self.dll.push(x) for x in range(1, 10)]
		node = self.dll.head
		i = 9
		while node:
			print(node.data)
			assert(node.data == i)
			i -= 1
			node = node.next

	def test_insertAfter(self):
		self.dll.push(1)
		self.dll.push(3)
		self.dll.insertAfter(self.dll.head, 2)
		node = self.dll.head
		i = 3
		while node:
			print(node.data)
			assert(node.data == i)
			i-=1
			node = node.next


	def test_append(self):
		self.dll.push(3)
		self.dll.push(1)
		self.dll.insertAfter(self.dll.head, 2)
		self.dll.append(4)
		node = self.dll.head
		i = 1
		while node:
			print(node.data)
			assert(node.data == i)
			i+=1
			node = node.next
