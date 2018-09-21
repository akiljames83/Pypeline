## Queue Implementation
import numpy as np
# FIFO Structure -> First in First Out
class Queue:
	def __init__(self,maxlen=1e9):
		self.queue = []
		self.maxlen = maxlen

	def isEmpty(self):
		return self.queue == []

	def sizeQueue(self):
		return len(self.queue)

	# # Main Methods: Enqueue Dequeue Peel
	def enqueue(self,data):
		if self.sizeQueue() < self.maxlen: 
			self.queue.append(data)
		else:
			self.dequeue()
			self.queue.append(data)

	def dequeue(self):
		data = self.queue[0]
		del self.queue[0]
		return data

	def peek(self):
		return self.queue[0]

	def to_array(self):
		return np.array(self.queue)

if __name__ == "__main__":
	queue = Queue()
	queue.enqueue(10)
	queue.enqueue(330)
	queue.enqueue(20)
	queue.enqueue(40)
	print("Size of the Queue is %d." % queue.sizeQueue())
	print("Dequeue: %d" % queue.dequeue())
	print("Dequeue: %d" % queue.dequeue())
	print("Size of the Queue is %d." % queue.sizeQueue())
