class Person:
    def __init__(self, name, age, surname):
        self.__name = name
        self.__age = age
        self.__surname = surname

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_surname(self):
        return self.__surname

    def set_age(self, age):
        self.__age = age
person1 = Person("Иван", 30, "Иванов")
person2 = Person("Мария", 25, "Петрова")

print("Первый человек: ")
print("Имя -", person1.get_name())
print("Возраст -", person1.get_age())
print("Фамилия -", person1.get_surname())

print("Второй человек: ")
print("Имя -", person2.get_name())
print("Возраст -", person2.get_age())
print("Фамилия -", person2.get_surname())

person1.set_age(35)
print("Новый возраст первого человека -", person1.get_age())