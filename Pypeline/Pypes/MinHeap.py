import heapq
import numpy as np

class Backwards(int):
	def __lt__(self, other):
		return not int.__le__(self, other)
	def __le__(self, other):
		return not int.__lt__(self, other)
	def __gt__(self, other):
		return not int.__ge__(self, other)
	def __ge__(self, other):
		return not int.__gt__(self, other)

class Restore(int):
	def __lt__(self, other):
		return int.__le__(self, other)
	def __le__(self, other):
		return int.__lt__(self, other)
	def __gt__(self, other):
		return int.__ge__(self, other)
	def __ge__(self, other):
		return int.__gt__(self, other)

class MinHeap():
	def __init__(self, li=[]):
		self.MinHeap = []
		assert isinstance(li, list)
		if li:
			self.heapify(li)

	def __repr__(self):
		return str(self.MinHeap)

	def __str__(self):
		return str(self.MinHeap)

	def heapify(self,li):
		assert isinstance(li, list)
		if self.MinHeap:
			li2 = [Restore(i) for i in self.MinHeap]
			self.MinHeap = [Backwards(i) for i in li2 + li]
			heapq.heapify(self.MinHeap)
		else:
			self.MinHeap = [Backwards(i) for i in li]
			heapq.heapify(self.MinHeap)

	def heappop(self):
		if not self.MinHeap:
			exception = "Index Error: Length of Heap is 0."
			raise Exception(exception)
		popped = heapq.heappop(self.MinHeap)
		return float(Restore(popped))

	def heappush(self,val):
		assert (isinstance(val, float) or isinstance(val, int))
		heapq.heappush(self.MinHeap,Backwards(val))

	def to_array(self):
		return np.array([Restore(i) for i in self.MinHeap])

	def merge(self,li):
		assert isinstance(li, list)
		self.heapify(li)


if __name__ == "__main__":
	li = [2, 4 , 10, 8, 90, 65, 18]
	li2 = [4, 5, 10, 1]
	heap = MinHeap()
	heap.heapify(li)
	a = heap.heappop()
	print(a, type(a))
	arr = heap.to_array()
	print(arr, type(arr))
	heap.merge(li2)
	print(heap)
	heap.heappop()
	print(heap)


	