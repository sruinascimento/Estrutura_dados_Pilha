from node4 import Node 

class Stack(object):

	def __init__(self):
		self.top = None
		self._len = 0

	def noEmpty(self) -> bool:
		# Retorna bool para a condição
		return self._len > 0

	def push(self, element):
		# 1º método: Inserção de elements na pilha
		node = Node(element)
		node.next = self.top
		self.top = node
		self._len += 1
		return node.data

	def pop(self):
		# 2º método: Remoção de elementos na pilha
		if self.noEmpty():
			node = self.top
			self.top = self.top.next
			self._len -= 1
			return node.data
		raise IndexError('The stack is empty')

	def peek(self):
		# 3º método: Retorna o ultimo elemento inserido
		if self.noEmpty():
			return self.top.data 
		raise IndexError('The stack is empty')

	def lenStack(self):
		# 4º método: Retorna o tamanho da nossa pilha
		return self._len

	def __repr__(self):
		# Reprensentação de todos dados da nossa pilha
		if self.noEmpty():
			data = ''
			pointer = self.top
			while pointer:
				data += '[ ---' + str(pointer.data) + '---]' + '\n'
				pointer = pointer.next
			return data
		return 'The stack is empty'

	def __str__(self):
		return self.__repr__()