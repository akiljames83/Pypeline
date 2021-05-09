from Pypeline.Pypes.StringSearch.BoyerMoore import *
import unittest

class BoyerMooreTest(unittest.TestCase):
	"""
	Tests for functions in the BoyerMoore module.
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

	def test_search(self):
		txt = "fjkasjejaw; lcfjaxkiwaopedask;lcas;ld"
		pat = ";lcas"
		pat1 = ";"
		pat2 = "@"
		pat3 = " "
		self.assertEqual(search(txt, pat),29)
		self.assertEqual(search(txt, pat1),10)
		self.assertEqual(search(txt, pat2),None)
		self.assertEqual(search(txt, pat3),11)
