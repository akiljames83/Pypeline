# essentially checks if string is in a list
class Node(object):

	def __init__(self,char):
		self.char = char
		self.children = {}
		self.word_finished = False
		self.counter = 0

class Trie(object):

	def __init__(self):
		self.root = Node('*')

	def insert(self,word):
		current = self.root
		for char in word:
			if char in current.children: # essentially counting char occurences
				current = current.children[char]
				current.counter += 1
			else: # if not already defined, generate a new node
				new_node = Node(char)
				current.children[char] = new_node
				current = new_node
				current.counter += 1
		current.word_finished = True # when finished flag!! 

	def search(self,word):
		if not self.root.children: # if there are no children of the root, no words to search
			return False
		current = self.root
		for char in word:
			if char in current.children:
				current = current.children[char]
			else:
				return False
		if current.word_finished:
			return True
		return False


if __name__ == "__main__":
	tree = Trie()
	tree.insert('bat')
	tree.insert('hack')
	tree.insert('hackathon')
	tree.insert('hac')

	print(tree.search("hac"))
	print(tree.search("ha"))
	print(tree.search("hackathon"))
	print(tree.search("bat"))
	print(tree.search("h"))
	print(tree.search("hack"))

		