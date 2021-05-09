from Pypeline.Pypes.Sorting import Mergesort
import unittest

class MergesortTest(unittest.TestCase):
	"""
	Tests for functions in the Mergesort module.
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

	def test_merge(self):
		arr = [1, 4, 2, 8, 7]
		Mergesort.merge(arr, 0, 1, 2, order='ascend')
		assert arr == [1, 2, 4, 8, 7]

	def test_mergeSort(self):
		arr = [1, 4, 2, 8, 7]
		Mergesort.mergeSort(arr, 0, 4)
		assert arr == [1, 2, 4, 7, 8]
