#!/usr/bin/env python
# coding: utf-8
# Слушатель (ФИО): Гульчак С.В.



# Разработка класса данных
# Примеры:
# date = Date(2018, 11, 23)
# print(date) # 23.11.2018
# repr(date)  # Date(2018, 11, 23)

# date = Date(2018, 11, 31)

# date.date = '31.11.2018'
# print(date.date) # '31.11.2018'

# date.day   = 31 # Запрет
# date.month = 50 # 
# date.month = 11 # 02 -> 01.03
# date.year       # на след. месяц
import datetime

class Date:
    """
    This is a class that creates a date.
    """
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # стандартный год
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  # високосный год

    def __init__(self, *args):
        """
        Examples:
            Format: year.month.day 2020.2.29
            d1 = Date(2020, 2, 15)  # 15.02.2020
            d2 = Date('2.02.2020')  # 02.02.2020
            d3 = Date()     # Current date
        Exceptions:
            ValueError('Invalid date format, example: 20.01.2020')
            or TypeError('year, month and day must be int')
        """
        if args and isinstance(args[0], str):
            self.date = args[0]
        else:
            d = datetime.date.today()
            if not args:
                self.is_valid_date(d.year, d.month, d.day)
                self.__year = d.year
                self.__month = d.month
                self.__day = d.day
            else:
                self.is_valid_date(args[0], args[1], args[2])
                self.__year = args[0]
                self.__month = args[1]
                self.__day = args[2]

    def __str__(self):
        return self.date

    def __repr__(self):
        return f'Date({self.__year!r}, {self.__month!r}, {self.__day!r})'

    @staticmethod
    def is_leap_year(year):
        """
        Examples:
            year: 2020 #True
            year: 2019 #False
        """
        if year % 4 == 0 and year % 100 != 0:
            return True
        if year % 400 == 0:
            return True
        return False

    @classmethod
    def get_max_day(cls, year, month):
        """
        Examples:
            January: 31 days
            February: 28 or 29(leap year) days
        """
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month - 1]

    @property
    def date(self):
        if self.__month < 10 and self.__day < 10:
            return f'0{self.__day}.0{self.__month}.{self.__year}'
        elif self.__day < 10:
            return f'0{self.__day}.{self.__month}.{self.__year}'
        elif self.__month < 10:
            return f'{self.__day}.0{self.__month}.{self.__year}'
        else:
            return f'{self.__day}.{self.__month}.{self.__year}'

    @classmethod
    def is_valid_date(cls, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(day, int):
            raise TypeError('day must be int')
        if not 0 < month <= 12:
            raise ValueError('month must be 0 < month <= 12')
        if not 0 < day <= cls.get_max_day(year, month):
            raise ValueError('invalid day for this month and year')

    @date.setter
    def date(self, value):
        """
        Examples:
            d1.date = "20.03.2010" #20.03.2020
            d1.date = "25.03.2010" #25.03.2020
        Exceptions:
            TypeError('Date must be str')
            ValueError('Invalid date format, example: 23.1.2020')
        """
        if not isinstance(value, str):
            raise TypeError('Date must be str')
        value = value.split('.')
        if len(value) != 3:
            raise ValueError('Invalid date format, example: 23.1.2020')
        try:
            day = int(value[0])
            month = int(value[1])
            year = int(value[2])
            self.is_valid_date(year, month, day)
        except:
            raise ValueError('Invalid date format')
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        """
        Examples:
            d1          #20.03.2020
            d1.day = 25 #25.03.2020
        """
        value = int(value)
        self.is_valid_date(self.__year, self.__month, value)
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        """
                Examples:
                    d1           #20.03.2020
                    d1.month = 2 #20.02.2020
                """
        value = int(value)
        self.is_valid_date(self.__year, value, self.__day)
        self.__month = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        """
        Examples:
            d1              #20.03.2020
            d1.year = 2010  #20.03.2010
        """
        value = int(value)
        self.is_valid_date(value, self.__month, self.__day)
        self.__year = value
    
    def add_day(self, day):
        """
        Examples:
            d1              #20.03.2020
            d1.add_day = 5  #25.03.2020
            d1.add_day = 8  #02.04.2020
        """
        if not isinstance(day, int):
            raise TypeError('day must be int')
        while day > 0:
            if day + self.__day > self.get_max_day(self.__year, self.__month):
                day -= (self.get_max_day(self.__year, self.__month) - self.day + 1)
                self.__day = 1
                if self.__month != 12:
                    self.__month += 1
                else:
                    self.__year += 1
                    self.__month = 1
            else:
                self.__day += day
                day = 0

    
    def add_month(self, month):
        """
        Examples:
            d1                  #20.03.2020
            d1.add_month = 5    #20.08.2020
            d1.add_month = 8    #20.04.2021
        """
        if not isinstance(month, int):
            raise TypeError('month must be int')
        year = month // 12
        self.__year += year
        self.__month += month % 12
        if self.__day == 29 and self.__month == 2 and not self.is_leap_year(year):
            self.__day = 1
            self.__month = 3

        
    def add_year(self, year):
        """
        Examples:
            d1                  #20.03.2020
            d1.add_year = 5     #20.08.2025
        """
        if not isinstance(year, int):
            raise TypeError('year must be int')
        self.__year += year

    def days_of_date(self):
        """
        Examples:
            d1                   #29.02.2020
            d1.days_of_date()    #738235 days
        """
        count = 0
        for i in range(self.__year + 1):
            if self.is_leap_year(i):
                count += 366
            else:
                count += 365
        if self.is_leap_year(self.__year):
            for i in range(1, self.__month + 1):
                count += self.DAY_OF_MONTH[1][i]
        else:
            for i in range(0, self.__month + 1):
                count += self.DAY_OF_MONTH[1][i]
        count += self.__day
        return count

    @staticmethod
    def date2_date1(date_2, date_1):
        """
        Examples:
            d1                   #29.02.2020
            d2                   #03.03.2020
            date2_date1(d2,d1    #3 days
        """
        return date_2.days_of_date() - date_1.days_of_date()

    def __lt__(self, other):
        if not isinstance(other, Date):
            raise TypeError('other must be Date')
        return self.days_of_date() < other.days_of_date()

    def __le__(self, other):
        if not isinstance(other, Date):
            raise TypeError('other must be Date')
        return self.days_of_date() <= other.days_of_date()

    def __eq__(self, other):
        if not isinstance(other, Date):
            raise TypeError('other must be Date')
        return self.days_of_date() == other.days_of_date()

    def __ne__(self, other):
        if not isinstance(other, Date):
            raise TypeError('other must be Date')
        return self.days_of_date() != other.days_of_date()

    def __gt__(self, other):
        if not isinstance(other, Date):
            raise TypeError('other must be Date')
        return self.days_of_date() > other.days_of_date()

    def __ge__(self, other):
        if not isinstance(other, Date):
            raise TypeError('other must be Date')
        return self.days_of_date() >= other.days_of_date()

    def __add__(self, other: int):
        return self.days_of_date() + other

    def __sub__(self, other):
        if not isinstance(other, Date):
            raise TypeError('other must be Date')
        return self.days_of_date() - other.days_of_date()

    def __radd__(self, other):
        return other + self.days_of_date()

    def __rsub__(self, other):
        return other.days_of_date() - self.days_of_date()

    def __iadd__(self, other: int):
        if not isinstance(other, int):
            raise TypeError('other must be int')
        while other > 0:
            if other + self.__day > self.get_max_day(self.__year, self.__month):
                other -= (self.get_max_day(self.__year, self.__month) - self.day + 1)
                self.__day = 1
                if self.__month != 12:
                    self.__month += 1
                else:
                    self.__year += 1
                    self.__month = 1
            else:
                self.__day += other
                other = 0
        return self

    def __isub__(self, other):
        if not isinstance(other, int):
            raise TypeError('other must be int')
        while other > 0:
            if other > self.__day:
                other -= self.__day
                if self.__month == 1:
                    self.__year -= 1
                    self.__month = 12
                else:
                    self.__month -= 1
                    self.__day = self.get_max_day(self.__year, self.__month)
            else:
                self.__day -= other
                other = 0
        return self
    def __int__(self):
        return self.days_of_date()




if __name__ == '__main__':
    g = Date(2020, 2, 29)
    t = Date("2.02.2020")
    s = Date()
    # g.add_day(813)
    # g.add_month(12)
    # g.add_year(203)
    print(g <= s)
    print(55 + g)
    print(g)
    print(s - g)
    g -= 30
    g += 20
    print(int(g))
    print(t)
