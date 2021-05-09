from Pypeline.Pypes.Queue import Queue
import numpy as np
import unittest

class QueueTest(unittest.TestCase):
	"""
	Tests for methods in the Queue class.
	"""

	@classmethod
	def setUpClass(cls):
		pass #TODO

	@classmethod
	def tearDownClass(cls):
		pass #TODO

	def setUp(self):
		self.q = Queue()

	def tearDown(self):
		self.q = None

	def test_isEmpty(self):
		assert self.q.isEmpty()

	def test_sizeQueue(self):
		assert self.q.sizeQueue() == 0

	def test_enqueue_deque(self):
		[self.q.enqueue(i) for i in range(100)]
		self.q.enqueue('TEST')
		self.q.enqueue(list(range(5)))
		assert all([self.q.dequeue() == i for i in range(100)])
		assert self.q.dequeue() == 'TEST'
		
		assert self.q.dequeue() == list(range(5))

	def test_peek(self):
		self.q.enqueue('TEST')
		assert self.q.peek() == 'TEST'

	def test_to_array(self):
		ref = np.zeros(10, dtype=int)
		for x in range(10):
			self.q.enqueue(x) 
			ref[x] = x
		assert (self.q.to_array() == ref).all()

	def test_to_list(self):
		ref = []
		for x in range(10):
			self.q.enqueue(x) 
			ref.append(x)

		assert self.q.to_list() == ref
