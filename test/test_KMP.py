from Pypeline.Pypes.StringSearch.KMP import *
import unittest

class KMPTest(unittest.TestCase):
	"""
	Tests for functions in the KMP module.
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

	def test_KMPSearch(self):
		pattern1 = "txt1"
		txt1 = "tfsdafsadasdtxt1sadsa"
		pattern2 = " "
		pattern3 = "sad"
		txt2 = " "
		self.assertEqual(KMPSearch(pattern1,txt1),12)
		self.assertEqual(KMPSearch(pattern2,txt1),None)
		self.assertEqual(KMPSearch(pattern3,txt1),6)
		self.assertEqual(KMPSearch(pattern1,txt2),None)
		


