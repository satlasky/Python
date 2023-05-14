import random


class Box:

    def __init__(self, name, from_city, target_city):
        self.__postcode = random.randint(100000, 999999)
        self.__name = name
        self.__from_city = from_city
        self.__target_city = target_city

    def get_postcode(self):
        return self.__postcode

    def get_name(self):
        return self.__name

    def get_from_city(self):
        return self.__from_city

    def get_target_city(self):
        return self.__target_city

    def set_target_city(self, target_city):
        self.__target_city = target_city

box = Box("Гришин Сергей", "Казань", "Санкт-Петербург")

print(f"Номер посылки: {box.get_postcode()}")
print(f"Отправитель: {box.get_name()}, г. {box.get_from_city()}")
print(f"Город назначения: {box.get_target_city()}")

box.set_target_city("Краснодар")

print(f"Город назначения (измененный): {box.get_target_city()}")