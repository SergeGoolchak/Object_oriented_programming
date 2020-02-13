from weakref import ref
# -*- coding: utf-8
# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Гульчак С.В.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class Glass:
    def __init__(self, capacity_volume, occupied_volume):
        if not isinstance(capacity_volume, int) or not isinstance(occupied_volume, int):
            raise TypeError("Arguments must be int")
        if capacity_volume <= 0 or occupied_volume < 0:
            raise ValueError("Arguments must be positive")
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def __str__(self):
        return f"capacity_volume: {self.capacity_volume}, occupied_volume: {self.occupied_volume}"


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.

g2_1 = Glass(500, 0)
g2_2 = Glass(350, 0)
g2_1.capacity_volume += 200
g2_2.occupied_volume = 100
# print(str(g2_2), str(g2_1))


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class GlassDefaultArg:
    def __init__(self, occupied_volume=0):
        if not isinstance(occupied_volume, int):
            raise TypeError("Arguments must be int")
        if occupied_volume < 0:
            raise ValueError("Arguments must be positive")
        self.occupied_volume = occupied_volume


g3_1 = GlassDefaultArg()
g3_2 = GlassDefaultArg(200)
# print(g3_1.occupied_volume, g3_2.occupied_volume)


# 4. Создайте класс GlassDefaultListArg (нужен только __init__)
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?

class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume=[]):
        if not isinstance(capacity_volume, int):
            raise TypeError("Arguments must be int")
        if capacity_volume <= 0:
            raise ValueError("Arguments must be positive")
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)


g4_1 = GlassDefaultListArg(100)
g4_2 = GlassDefaultListArg(200)
# print(g4_1.occupied_volume, g4_2.occupied_volume)
#Оба объекта будут ссылаться на одну ячейку памяти атрибута occupied_volume, при каждом новом append будет расширяться
#список для всех объектов класса.


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.

class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume):
        if not isinstance(capacity_volume, (int, float)) or not isinstance(occupied_volume, (int, float)):
            raise TypeError("Arguments must be int or float")
        if capacity_volume <= 0 or occupied_volume < 0:
            raise ValueError("Arguments must be positive")
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def add_water(self, water):
        if not isinstance(water, (int, float)):
            raise TypeError("Argument must be int or float")
        elif water <= 0:
            raise ValueError("Argument must be positive")
        empty_volume = self.capacity_volume - self.occupied_volume
        ostatok = water - empty_volume
        if ostatok > 0:
            self.occupied_volume = water - ostatok
            return ostatok
        else:
            self.occupied_volume += water

    def remove_water(self, water):
        if not isinstance(water, (int, float)):
            raise TypeError("Argument must be int or float")
        elif water <= 0:
            raise ValueError("Argument must be positive")
        if water > self.occupied_volume:
            raise Exception(f"Can`t remove, {self.occupied_volume} ml water in the glass")
        else:
            self.occupied_volume -= water

g5_1 = GlassAddRemove(300, 100)
g5_2 = GlassAddRemove(250, 0)
g5_3 = GlassAddRemove(500, 500)
g5_1.add_water(200)
# print(g5_1.occupied_volume)
g5_1.remove_water(100)
# print(g5_1.occupied_volume)

# 6. Создайте три объекта типа GlassAddRemove,
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.

g6_1 = GlassAddRemove(300, 100)
g6_2 = GlassAddRemove(250, 0)
g6_3 = GlassAddRemove(500, 500)
# print(g6_1.__dir__())
# print(g6_2.__dir__())
# print(dir(GlassAddRemove))
# print(type(g6_1))
# print(type(g6_2))
# print(type(GlassAddRemove))


# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.

class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume):
        print(self.__dict__)
        print(self.__dir__())
        if not isinstance(capacity_volume, (int, float)) or not isinstance(occupied_volume, (int, float)):
            raise TypeError("Arguments must be int or float")
        if capacity_volume <= 0 or occupied_volume < 0:
            raise ValueError("Arguments must be positive")
        self.capacity_volume = capacity_volume
        print(self.__dict__)
        print(self.__dir__())
        self.occupied_volume = occupied_volume
        print(self.__dict__)
        print(self.__dir__())

# g7_1 = GlassAddRemove(100, 50)


# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.
g8_1 = Glass(100, 10)
g8_2 = Glass(200, 20)
g8_3 = Glass(200, 20)
# print(hex(id(g8_1)))
# print(hex(id(g8_2)))
# print(hex(id(g8_3)))


# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.

class d:
    def __init__(f, a=2):
        f.a = a

    def print_me(p):
        print(p.a)


# d.print_me(d())
#С точки зрения интерпретатора Python код корректный, он будет выполнен без каких-либо Excepsions.
#С точки зрения соглашения, код не корректен, класс объявляется заглавной буквой,
# в __init__ и внутренние методы первым аргументов подается self.


# 10. Исправьте
class A:
    def __init__(self, a):
        if 10 < a < 50:
            self.a = a


# Объясните так реализовывать __init__ нельзя?
#Нельзя, так как при создании объекта с аргументами от 10 до 50, атрибут а не будет создан

# 11. Циклическая зависимость (стр. 39-44)


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
