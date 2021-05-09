from Pypeline.Pypes.Heap import Heap
import unittest

class HeapTest(unittest.TestCase):
	"""
	Tests for methods in the Heap class.
	"""

	@classmethod
	def setUpClass(cls):
		cls.vals = [10, 0, 2, 40, 70, -20]

	@classmethod
	def tearDownClass(cls):
		pass #TODO

	def setUp(self):
		self.heap = Heap(5)

	def tearDown(self):
		self.heap = None

	def test_insert(self):
		[self.heap.insert(x) for x in self.vals[:3]]
		assert not self.heap.isFull()

	def test_heapSort(self):
		[self.heap.insert(x) for x in self.vals[:-1]]
		self.heap.heapSort()
		assert self.heap.heap

	def test_isFull(self):
		[self.heap.insert(x) for x in self.vals]
		assert self.heap.isFull()
