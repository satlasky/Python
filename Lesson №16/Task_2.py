class Father:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Child(Father):
    def __init__(self, name, surname, patronim):
        super().__init__(name, surname)
        self.patronim = patronim

child = Child("Иван", "Иванов", "Иванович")
print(child.name, child.surname, child.patronim)