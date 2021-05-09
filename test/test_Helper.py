from Pypeline.Pypes.Sorting import Helper
import unittest

class HelperTest(unittest.TestCase):
	"""
	Tests for functions in the Helper module.
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

	def test_less(self):
		assert Helper.less(5, 3) == False
		assert Helper.less(3, 3) == False
		assert Helper.less(1, 3) == True

	def test_swap(self):
		arr = [1, 2]
		Helper.swap(arr, 0, 1)
		assert arr == [2, 1]
		Helper.swap(arr, 1, 1)
		assert arr == [2, 1]