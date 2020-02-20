import json
import pickle
from weakref import ref


class IStructureDriver:
	def read(self):
		pass

	def write(self, d):
		pass


class JSONFileDriver(IStructureDriver):
	def __init__(self, filename):
		self.__filename = filename

	def read(self):
		with open(self.__filename, encoding='UTF-8') as f:
			return json.load(f)

	def write(self, d):
		with open(self.__filename, 'w', encoding='UTF-8') as f:
			json.dump(d, f, ensure_ascii=False)


class JSONStringDriver(IStructureDriver):
	def __init__(self, s='{}'):
		self.__s = s

	def get_string(self):
		return self.__s

	def read(self):
		return json.loads(self.__s)

	def write(self, d):
		self.__s = json.dumps(d, ensure_ascii=False)


class PickleDriver(IStructureDriver):
	def __init__(self, filename):
		self.__filename = filename

	def read(self):
		with open(self.__filename, 'rb') as f:
			return pickle.load(f)

	def write(self, d):
		with open(self.__filename, 'wb') as f:
			pickle.dump(d, f)



class SDBuilder:
	def build(self):
		return None


class JSONFileBuilder(SDBuilder):
	def build(self):
		filename = input('Enter filename (.json)>')
		return JSONFileDriver(filename)


class JSONStrBuilder(SDBuilder):
	def build(self):
		return JSONStringDriver()


class PickleBuilder(SDBuilder):
	def build(self):
		filename = input('Enter filename (.bin)>')
		return PickleDriver(filename)


class SDFabric:
	def get_sd_driver(self, driver_name):
		builders = {'json': JSONFileBuilder,
					'json_str': JSONStrBuilder,
					'pickle': PickleBuilder}
		try:
			return builders[driver_name]()
		except:
			return SDBuilder()


class Observer:
	def update(self, subject):
		pass


class WeakSubject:

	def __init__(self):
		self.__o = []

	def add_observer(self, o: Observer):
		for el in self.__o:
			if el() is o:
				return
		self.__o.append(ref(o))

	def remove_observer(self, o: Observer):
		ok = False
		for index, el in enumerate(self.__o):
			if el() is o:
				ok = True
				break
		if ok:
			del self.__o[index]

	def notify(self):
		for o in self.__o:
			o().update(self)

class Data(WeakSubject):
	def __init__(self, value):
		super().__init__()
		self.__value = value

	@property
	def data(self):
		return self.__value

	@data.setter
	def data(self, value):
		self.__value = value
		self.notify()

	def __str__(self):
		return f'{self.__value!s}'




class LinkedList(Observer):
	"""
	This is a class that creates a linked bidirectional list.
	Basic methods:
	next_node
	insert
	append
	clear
	find
	delete
	remove
	"""
	class Node:
		"""
		A class that creates a Node with a given value and references to the previous and next Node.
		If they exist, otherwise None.
		"""
		def __init__(self, value: WeakSubject = None, prev=None, next_=None):
			self.value = value
			self.__prev = prev
			self.__next = next_

		@property
		def next_(self):
			"""
			:return: Next Node
			"""
			return self.__next

		@next_.setter
		def next_(self, node):
			"""
			This method creates a link to the node to be sent, which will be next to the current one.
			:param node: node must be Node or None
			:return: a link to the new node to be sent
			"""
			if node is not None and not isinstance(node, type(self)):
				raise TypeError('node must be Node or None')
			self.__next = node

		@property
		def prev(self):
			"""
			:return: previous Node
			"""
			return self.__prev

		@prev.setter
		def prev(self, node):
			"""
			This method creates a link to the node to be sent, which will be previous to the current one.
			:param node: node must be Node or None
			:return: a link to the new node to be sent
			"""
			if node is not None and not isinstance(node, type(self)):
				raise TypeError('node must be Node or None')
			self.__prev = node

		def __str__(self):
			return f'{self.value!s}'

		def __repr__(self):
			return f"Node(value={self.value}, prev={self.prev}, next_={self.next_})"

	def __init__(self, structure_driver: IStructureDriver):
		self.structure_driver = structure_driver
		self.head = self.Node()
		self.tail = self.Node()
		self.tail.prev = self.head
		self.head.next_ = self.tail
		self.length = 0

	def update(self, subject):
		print(f'Update: {subject!s}')
		self.save()


	def next_node(self, current_node, value):
		"""
		Method for adding the next node.
		:param current_node: The node after which you want to insert a new node.
		:param value: Value of new created node.
		:return: Adding the next node.
		"""
		new_node = self.Node(value, current_node, current_node.next_)
		current_node.next_.prev = new_node
		current_node.next_ = new_node
		self.length += 1

	def insert(self, value: WeakSubject, index=0):
		"""
		Insert Node to any place of LinkedList
		:param value: Value of new created node.
		:param index: position of node
		:return: Adding the new node on index position.
		"""
		if not isinstance(index, int):
			raise TypeError('index must be int')
		if 0 > index > self.length:
			raise ValueError('Invalid index')
		current_node = self.head
		for _ in range(index):
			current_node = current_node.next_
		value.add_observer(self)
		self.next_node(current_node, value)

	def append(self, value: WeakSubject):
		'''
		Append Node to tail of LinkedList
		node - Node
		'''
		current_node = self.tail.prev
		value.add_observer(self)
		self.next_node(current_node, value)

	def clear(self):
		'''
		Clear LinkedList
		'''
		self.__init__()

	def find(self, value):
		"""
		Finds a node.
		:param value: The value of some node.
		:return: Node.
		"""
		if self.length == 0:
			return None
		current_node = self.head
		for i in range(self.length):
			current_node = current_node.next_
			if current_node.value == value:
				return current_node
		return None

	def remove(self, value: WeakSubject):
		"""
		The method removes the node from the list and returns it.
		:param value: The value of removed node.
		:return: Removed Node.
		"""
		current_node = self.find(value)
		if not current_node:
			raise Exception("Node with that value does not exist")
		value.remove_observer(self)
		current_node.prev.next_ = current_node.next_
		current_node.next_.prev = current_node.prev
		self.length -= 1
		self.save()
		return current_node

	def delete(self, index = 0):
		"""
		The method delete the link on the node and node.
		:param value: The value of deleted node.
		"""
		current_node = self.head
		for _ in range(index+1):
			current_node = current_node.next_
		if not current_node.prev:
			self.head.next_ = current_node.next_
			current_node.next_.prev = current_node.prev
			self.length -= 1
			self.save()
		else:
			current_node.prev.next_ = current_node.next_
			current_node.next_.prev = current_node.prev
			self.length -= 1
			self.save()

	def save(self):
		d = {}
		current_node = self.head
		for i in range(self.length):
			d[f'Node{i}'] = str(current_node.next_)
			current_node = current_node.next_
		self.structure_driver.write(d)

	def load(self):
		s = self.structure_driver.read()
		node = LinkedList(self.structure_driver)
		for i in range(len(s)):
			node.insert(s[f'Node{i}'], i)
		print(node.tail.prev)
		return node



if __name__ == '__main__':
	driver_name = input('Please enter driver name >')
	builder = SDFabric().get_sd_driver(driver_name)
	sd = builder.build()
	ll = LinkedList(sd)
	ll.insert(Data(7))
	d = Data(10)
	ll.insert(d)
	ll.save()

	d.data = 100
	print(ll.tail.prev)