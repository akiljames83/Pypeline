from Pypeline.Pypes.MaxHeap import MaxHeap
import numpy as np
import unittest

class MaxHeapTest(unittest.TestCase):
	"""
	Tests for methods in the MaxHeap class.
	"""

	@classmethod
	def setUpClass(cls):
		cls.li = [2, 4 , 10, 8, 90, 65, 18]
		cls.li2 = [4, 5, 10, 1]

	@classmethod
	def tearDownClass(cls):
		pass #TODO

	def setUp(self):
		self.heap = MaxHeap()
		# heap.heapify(li)
		# a = heap.heappop()
		# print(a, type(a))
		# arr = heap.to_array()
		# print(arr, type(arr))
		# heap.merge(li2)
		# print(heap)
		# heap.heappop()
		# print(heap)

	def tearDown(self):
		self.heap = None


	def test_heapify(self):
		self.heap.heapify(self.li)
		assert self.heap.MaxHeap

	def test_heappop(self):
		self.heap.heapify(self.li)
		x = self.heap.heappop()
		assert x == 2

	def test_heappush(self):
		self.heap.heapify(self.li)
		self.heap.heappush(12)
		assert self.heap.MaxHeap[-1] == 12
		[self.heap.heappop() for _ in range(3)]
		assert self.heap.heappop() == 12

	def test_to_array(self):
		self.heap.heapify(self.li)
		arr = self.heap.to_array()
		assert type(arr) == np.ndarray
		assert list(arr) == self.li

	def test_merge(self):
		self.heap.heapify(self.li)
		self.heap.merge(self.li2)
		assert len(self.li) + len(self.li2) == len(self.heap.MaxHeap)
