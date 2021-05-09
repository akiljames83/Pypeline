from Pypeline.Pypes.Stack import Stack
import numpy as np
import unittest

class StackTest(unittest.TestCase):
	"""
	Tests for methods in the Stack class.
	"""

	@classmethod
	def setUpClass(cls):
		pass #TODO

	@classmethod
	def tearDownClass(cls):
		pass #TODO

	def setUp(self):
		self.s = Stack()
		pass #TODO

	def tearDown(self):
		self.s = None
		pass #TODO

	def test_isEmpty(self):
		assert self.s.isEmpty()

	def test_sizeStack(self):
		self.s.push(2)
		assert self.s.sizeStack() == 1

	def test_push(self):
		for i in range(100):
			self.s.push(i)
		assert self.s.sizeStack() == 100

	def test_pop(self):
		[self.s.push(x) for x in range(100, 0, -1)]
		assert(all([(self.s.pop() == (i+1)) for i in range(self.s.sizeStack())]))
		assert self.s.sizeStack() == 0

	def test_peek(self):
		self.s.push(20)
		assert self.s.peek() == 20

	def test_to_array(self):
		ref = []
		for x in range(10):
			self.s.push(x) 
			ref.append(x)

		assert self.s.to_list() == ref

	def test_to_list(self):
		ref = np.zeros(10, dtype=int)
		for x in range(10):
			self.s.push(x) 
			ref[x] = x

		assert (self.s.to_array() == ref).all()
