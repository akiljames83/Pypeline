from Pypeline.Pypes.Sorting.Shellsort import shellSort
import unittest

class ShellsortTest(unittest.TestCase):
	"""
	Tests for functions in the Shellsort module.
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

	def test_shellSort(self):
		arr1 = [1,4,6,-5,1]
		arr2 = [7,3,5,2,6,8,1,5,6,10]
		shellSort(arr1)
		shellSort(arr2)
		self.assertListEqual(arr1, [-5, 1, 1, 4, 6])
		self.assertListEqual(arr2, [1, 2, 3, 5, 5, 6, 6, 7, 8, 10])
