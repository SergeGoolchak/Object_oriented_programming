from weakref import ref
# -*- coding: utf-8
# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Гульчак С.В.

# ---------------------------------------------------------------------------------------------

class LinkedList:
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
        def __init__(self, value=None, prev=None, next_=None):
            self.value = value
            self.__prev = prev
            self.__next = next_

        @property
        def next_(self):
            """
            :return: Next Node
            """
            return self.__next if self.__next is not None else None

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
            return self.__prev if self.__prev is not None else None

        @prev.setter
        def prev(self, node):
            """
            This method creates a link to the node to be sent, which will be previous to the current one.
            :param node: node must be Node or None
            :return: a link to the new node to be sent
            """
            if node is not None and not isinstance(node, type(self)):
                raise TypeError('node must be Node or None')
            self.__prev = node if node is not None else None

        def __str__(self):
            return f'{self.value}'

        def __repr__(self):
            return f"Node(value={self.value}, prev={self.prev}, next_={self.next_})"

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.tail.prev = self.head
        self.head.next_ = self.tail
        self.length = 0


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

    def insert(self, value, index=0):
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
        self.next_node(current_node, value)

    def append(self, value):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        current_node = self.tail.prev
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

    def remove(self, value):
        """
        The method removes the node from the list and returns it.
        :param value: The value of removed node.
        :return: Removed Node.
        """
        current_node = self.find(value)
        if current_node == None:
            raise Exception("Node with that value does not exist")
        current_node.prev.next_ = current_node.next_
        current_node.next_.prev = current_node.prev
        return current_node

    def delete(self, value):
        """
        The method delete the link on the node and node.
        :param value: The value of deleted node.
        """
        current_node = self.find(value)
        if current_node == None:
            raise Exception("Node with that value does not exist")
        current_node.prev.next_ = current_node.next_
        current_node.next_.prev = current_node.prev


if __name__ == '__main__':
    g = LinkedList()
    g.insert(7, 0)
    g.append(10)
    print(g.head.next_)
    print(g.head.next_.next_)
    g.insert("Hello", 2)
    print(g.length)
    print(g.tail.prev)
    print(g.find(10))
    print(repr(g.find(10)))
    g.delete(7)
    print(g.head.next_)
    print(g.find(7))
    g.clear()
    g.append("Yeeeeaaaah!!!")
    print(g.tail.prev)
