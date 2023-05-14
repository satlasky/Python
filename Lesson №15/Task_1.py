class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def meow(self):
        print(f'{self.name} мяукает')

    def purr(self):
        print(f'{self.name} мурлыкает')

    def sleep(self):
        print(f'{self.name} спит')


cat1 = Cat('Барсик', 'рыжий', 3)
print(f"Имя кота: {cat1.name}")
print(f"Окрас кота: {cat1.color}")
print(f"Возраст кота: {cat1.age}")
cat1.meow()
cat1.purr()
cat1.sleep()