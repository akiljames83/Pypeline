## Stack Implementation
## Array representation -> LIFO Structure
import numpy as np

class Stack:

	def __init__(self):
		self.stack = []

	def isEmpty(self):
		return self.stack == []

	def sizeStack(self):
		return len(self.stack)

	# 3 main methods in a stack! Push, Pop and Seek
	def push(self,data):
		self.stack.append(data)

	def pop(self):
		data = self.stack[-1]
		#self.stack = self.stack[:-1]
		del self.stack[-1]
		return data

	def peek(self):
		return self.stack[-1]

	def to_array(self):
		return np.array(self.stack)

	def to_list(self):
		return self.stack

if __name__ == "__main__":
	stack = Stack()
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(5)
	print("Size of the stack is:",stack.sizeStack())
	print("Popped:",stack.pop())
	print("Popped:",stack.pop())
	print("Size of the stack is:",stack.sizeStack())
	print("Peek:",stack.peek())
	print("Size of the stack is:",stack.sizeStack())


