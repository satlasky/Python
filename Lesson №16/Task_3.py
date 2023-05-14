from abc import ABC, abstractmethod


class Stationery(ABC):
    color = ''

    @classmethod
    def set_color(cls, color):
        cls.color = color

    @abstractmethod
    def draw(self):
        pass


class Pen(Stationery):
    color = 'blue'

    def draw(self):
        print('Ручка пишет')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует')


class Handle(Stationery):
    def draw(self):
        print('Маркер маркирует')


Stationery.set_color('yellow')

print(Pen.color)
print(Pencil.color)
print(Handle.color)

'''
В результате видно, что атрибут color в классе Pen остался равен 'blue', 
А в классах Pencil и Handle поменялся на 'yellow'. 
Это произошло из-за того, что метод set_color изменяет атрибут color класса Stationary, 
А класс Pen явно определяет свой атрибут color, 
В то время как классы Pencil и Handle наследуют атрибут color от класса-родителя.
'''