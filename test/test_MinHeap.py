from Pypeline.Pypes import MinHeap

import unittest

import numpy as np

class MinHeapTest(unittest.TestCase):
	"""
	Tests for methods in the MinHeap class.
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

	def test_heapify(self):
		li = [2, 4 , 10, 8, 90, 65, 18]
		heap = MinHeap.MinHeap()
		heap.heapify(li)
		assert len(heap.MinHeap) == 7
		assert heap.MinHeap == [90, 8, 65, 2, 4, 10, 18]

	def test_heappop(self):
		li = [2, 4 , 10, 8, 90, 65, 18]
		heap = MinHeap.MinHeap()
		heap.heapify(li)
		assert len(heap.MinHeap) == 7
		assert heap.heappop() == 90

	def test_heappush(self):
		li = [2, 4, 10, 90, 65, 18]
		heap = MinHeap.MinHeap()
		heap.heapify(li)
		assert len(heap.MinHeap) == 6
		heap.heappush(8)
		assert len(heap.MinHeap) == 7
		assert heap.MinHeap == [90, 65, 18, 4, 2, 10, 8]

	def test_to_array(self):
		li = [2, 4 , 10, 8, 90, 65, 18]
		heap = MinHeap.MinHeap()
		heap.heapify(li)
		assert (heap.to_array() == np.array([90, 8, 65, 2, 4, 10, 18])).all()

	def test_to_list(self):
		li = [2, 4 , 10, 8, 90, 65, 18]
		heap = MinHeap.MinHeap()
		heap.heapify(li)
		assert heap.to_list() == [90, 8, 65, 2, 4, 10, 18]

	def test_merge(self):
		li = [2, 4 , 10]
		li2 = [8, 90, 65, 18]
		heap = MinHeap.MinHeap()
		heap.heapify(li)
		assert len(heap.MinHeap) == 3
		heap.merge(li2)
		assert len(heap.MinHeap) == 7
		assert heap.MinHeap == [90, 10, 65, 8, 4, 2, 18]


class BackwardsTest(unittest.TestCase):
	"""
	Tests for methods in the Backwards class.
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


class RestoreTest(unittest.TestCase):
	"""
	Tests for methods in the Restore class.
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

