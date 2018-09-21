import heapq
import numpy as np

class MaxHeap():
	def __init__(self, li=[]):
		self.MaxHeap = []
		assert isinstance(li, list)
		if li:
			self.heapify(li)

	def __repr__(self):
		return str(self.MaxHeap)

	def __str__(self):
		return str(self.MaxHeap)

	def heapify(self,li):
		assert isinstance(li, list)
		if self.MaxHeap:
			self.merge(li)
		else:
			self.MaxHeap = li
			heapq.heapify(self.MaxHeap)

	def heappop(self):
		if not self.MaxHeap:
			exception = "Index Error: Length of Heap is 0."
			raise Exception(exception)
		return heapq.heappop(self.MaxHeap)

	def heappush(self,val):
		assert (isinstance(val, float) or isinstance(val, int))
		heapq.heappush(self.MaxHeap,val)

	def to_array(self):
		return np.array(self.MaxHeap)

	def merge(self,li):
		assert isinstance(li, list)
		self.MaxHeap = self.MaxHeap + li
		heapq.heapify(self.MaxHeap)


if __name__ == "__main__":
	li = [2, 4 , 10, 8, 90, 65, 18]
	li2 = [4, 5, 10, 1]
	heap = MaxHeap()
	heap.heapify(li)
	a = heap.heappop()
	print(a, type(a))
	arr = heap.to_array()
	print(arr, type(arr))
	heap.merge(li2)
	print(heap)
	heap.heappop()
	print(heap)


	