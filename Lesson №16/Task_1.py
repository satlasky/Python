from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age

    @abstractmethod
    def say(self):
        pass


class Cat(Animal):
    def say(self):
        print("Meow!")


class Dog(Animal):
    def say(self):
        print("Woof!")


cat = Cat("Черный", "Ласка", 3)
dog = Dog("Коричневый", "Рекс", 5)

print(cat.color)
cat.say()

print(dog.name)
dog.say()