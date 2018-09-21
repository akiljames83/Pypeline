## Implementation of the heap

class Heap(object):
	# Class constant variables can be assigned this way
	HEAP_SIZE = 10

	def __init__(self,size=10):
		Heap.HEAP_SIZE = size
		self.heap = [0]*Heap.HEAP_SIZE
		self.currentPosition = -1

	def insert(self,item):

		if self.isFull():
			print("Heap is full...")
			return

		else:
			self.currentPosition += 1
			self.heap[self.currentPosition] = item
			self.fixUp(self.currentPosition) # reheap the heap

	def fixUp(self, index):
		parentIndex = int((index-1)/2)

		while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
			temp = self.heap[parentIndex]
			self.heap[parentIndex] = self.heap[index]
			self.heap[index] = temp
			parentIndex = int((index-1)/2) # from current move up

	def heapSort(self):

		for i in range(self.currentPosition+1):
			temp = self.heap[0]
			print("%d" % temp)
			self.heap[0] = self.heap[self.currentPosition - i]
			self.heap[self.currentPosition] = temp
			# fix down 
			self.fixDown(0,self.currentPosition-i-1)

	def fixDown(self,index,upto):

		while index <= upto:
			leftChild = 2*index +1
			rightChild = 2*index +2

			if leftChild < upto:
				childToSwap = None

				if rightChild > upto:
					childToSwap = leftChild
				else:
					if self.heap[leftChild] > self.heap[rightChild]:
						childToSwap = leftChild
					else:
						childToSwap = rightChild
				if self.heap[index] < self.heap[childToSwap]:
					temp = self.heap[index]
					self.heap[index] = self.heap[childToSwap]
					self.heap[childToSwap] = temp
				else:
					break

				index = childToSwap
			else:
				break


	def isFull(self):
		if self.currentPosition == Heap.HEAP_SIZE:
			return True
		else:
			return False

if __name__ == "__main__":
	heap = Heap()
	heap.insert(10)
	heap.insert(-20)
	heap.insert(0)
	heap.insert(2)
	#heap.insert(30)

	heap.heapSort()