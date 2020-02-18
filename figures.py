import os
from abc import abstractmethod
import math

# import sys
# # Подключаем модули QApplication и QLabel
# from PySide2.QtWidgets import QApplication, QWidget
# from PySide2.QtGui import QPainter, QBrush
# from PySide2.QtCore import Qt, QPoint


class Figure:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    @abstractmethod
    def perimeter(self):
        return 0.0

    @property
    @abstractmethod
    def square(self):
        return 0.0

    @property
    @abstractmethod
    def width(self):
        return 0.0

    @property
    @abstractmethod
    def height(self):
        return 0.0

    
class Rectangle(Figure):
    def __init__(self, x=0, y=0, w=0, h=0):
        self.__x = x
        self.__y = y
        self.w = w
        self.h = h

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def perimeter(self):
        return 2*(self.w+self.h)
    
    def square(self):
        return self.w*self.h
    
    def width(self):
        return self.w
    
    def height(self):
        return self.h


class Ellipse(Figure):
    def __init__(self, x=0, y=0, w=0, h=0):
        self.__x = x
        self.__y = y
        self.w = w
        self.h = h

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def perimeter(self):
        per = 4 * ((3.14 * (self.w / 2) * (self.h / 2) + ((self.w / 2) - (self.h / 2)) ** 2) / ((self.w / 2) + (self.h / 2)))
        return per

    def square(self):
        pl = 3.14 * (self.w / 2) * (self.h / 2)
        return pl

    def width(self):
        return self.w

    def height(self):
        return self.h


class CloseFigure(Figure):
    def __init__(self, *args):
        self.point = []
        for i in range(0, len(args) - 1, 2):
            self.point.append({'x': args[i], 'y': args[i+1]})

    def perimeter(self):
        per = 0
        for i in range(len(self.point) - 1):
            per += math.sqrt(((self.point[i+1]['x'] - self.point[i]['x']) ** 2)
                             + ((self.point[i+1]['y'] - self.point[i]['y']) ** 2))
        per += math.sqrt(((self.point[0]['x'] - self.point[-1]['x']) ** 2)
                         + ((self.point[0]['y'] - self.point[-1]['y']) ** 2))
        return per

    def square(self):
        sum1 = 0
        sum2 = 0
        for i in range(len(self.point) - 1):
            sum1 += self.point[i]['x'] * self.point[i+1]['y']
            sum2 -= self.point[i+1]['x'] * self.point[i]['y']
        sum1 += self.point[-1]['x'] * self.point[0]['y']
        sum2 -= self.point[0]['x'] * self.point[-1]['y']
        res = math.fabs(sum1+sum2) / 2
        return res

    def width(self):
        my_my_max = self.point[0]['x']
        my_min = self.point[0]['x']
        for i in range(len(self.point)):
            if self.point[i]['x'] > my_max:
                my_max = self.point[i]['x']
            if self.point[i]['x'] < my_min:
                my_min = self.point[i]['x']
        result = my_max - my_min
        return result

    def height(self):
        my_max = self.point[0]['y']
        my_min = self.point[0]['y']
        for i in range(len(self.point)):
            if self.point[i]['y'] > my_max:
                my_max = self.point[i]['y']
            if self.point[i]['y'] < my_min:
                my_min = self.point[i]['y']
        result = my_max - my_min
        return result

                                                     
if __name__ == '__main__':
    pass