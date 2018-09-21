# Implementing a linked list
import numpy as np

class Node(object): # inherits from object

	def __init__(self,data): # instantiates data in the node
		self.data = data
		self.nextNode = None # reference to the next node

class LinkedList(object):

	def __init__(self):
		self.head = None # identiify head of the list
		self.size = 0 # initialize length to be zero
		self.linkedlist = []

	def __str__(self):
		return str(self.linkedlist)

	def __repr__(self):
		return str(self.linkedlist)

	def insert(self, data):
		self.size += 1
		#instantiate a new node
		newNode = Node(data)

		# if head of ll not defined, set it
		if not self.head:
			self.head = newNode
		# if it is, this new node becomes head of ll
		else: # essentially just updating pointers
			newNode.nextNode = self.head
			self.head = newNode
		self.linkedlist.append(data)

	# insert item to the end of the list; O(N) time complexity
	def insertEnd(self, data):
		self.size +=1
		newNode = Node(data)
		#print(newNode,newNode.nextNode)
		actualNode = self.head
		#print(actualNode,actualNode.nextNode)

		# while the following node is not None (not the end of ll)
		while actualNode.nextNode is not None:
			#print(actualNode.nextNode)
			actualNode = actualNode.nextNode # increment
			# brings us to last item

		actualNode.nextNode = newNode
		self.linkedlist.append(data)

	# checks size of the ll; O(1) time complexity
	def getSize(self): 
		return self.size

	# calculates the size of the ll O(N) time complexity; not very efficient
	def getSize2(self):
		actualNode = self.head
		size = 0

		while actualNode is not None:
			# increment the size, and shift to next node in the ll
			size +=1
			actualNode = actualNode.nextNode
		return size

	def traverseList(self):
		actualNode = self.head

		while actualNode is not None:
			# print current data
			print("%d " % actualNode.data)
			# go to he next node in ll
			actualNode = actualNode.nextNode

	# define remove method for particular data O(N) time complexity
	def remove(self,data):
		# if there is no head in the list, then cant create a list
		if self.head is None:
			return
		self.size -= 1

		currentNode = self.head
		previousNode = None

		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.nextNode

		# at this point, we are at the node we want to get rid of
		if previousNode is None: # if we are at the head
			self.head = currentNode.nextNode

		else: # if not at the head
			# change the pointer
			previousNode.nextNode = currentNode.nextNode

		self.linkedlist.pop(self.linkedlist.index(data))

	def to_array(self):
		return np.array(self.linkedlist)

	def to_list(self):
		return self.linkedlist

if __name__ == "__main__":
	# Testing our linkedList

	linkedlist = LinkedList()
	#linkedlist.head = Node(5)
	linkedlist.insert(12)
	linkedlist.insert(3)
	linkedlist.insert(78)
	linkedlist.insertEnd(5)

	linkedlist.traverseList()
	print("Size of the linked list is {}.".format(linkedlist.getSize()))

	linkedlist.remove(5)
	linkedlist.remove(12)
	linkedlist.remove(3)
	print("Items deleted from list.")
	linkedlist.traverseList()
	linkedlist.remove(78)
	linkedlist.traverseList()
	print("Size of linkedlist now is %d." % linkedlist.getSize())






