from Pypeline.Pypes.Sorting import Radixsort

import unittest

class RadixsortTest(unittest.TestCase):
	"""
	Tests for functions in the Radixsort module.
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

	def test_countingSort(self):
		arr = [3, 2, 2, 1, 4]
		Radixsort.countingSort(arr, 1)
		assert arr == [1, 2, 2, 3, 4]

	def test_radixSort(self):
		arr = [3, 2, 2, 1, 4]
		Radixsort.radixSort(arr)
		assert arr == [1, 2, 2, 3, 4]
