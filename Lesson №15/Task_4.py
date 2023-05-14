class Car:
    def __init__(self, color, brand, body, speed, transmission):
        self.color = color
        self.brand = brand
        self.body = body
        self.speed = speed
        self.transmission = transmission

    def start(self):
        print("Машина начала движение")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def speed_up(self, amount):
        if self.body == "грузовик" and self.speed + amount > 60:
            print("Скорость превышена! Разрешенная скорость 60 км/ч")
            return
        elif self.body == "седан" and self.speed + amount > 80:
            print("Скорость превышена! Разрешенная скорость 80 км/ч")
            return
        self.speed += amount
        print(f"Машина ускорилась до {self.speed} км/ч")

    def speed_down(self, amount):
        self.speed -= amount
        print(f"Машина замедлилась до {self.speed} км/ч")

    def beep(self):
        print("Бип-бип")


truck1 = Car("синий", "MAN", "грузовик", 70, "механика")
truck2 = Car("желтый", "Volvo", "грузовик", 80, "автомат")
car = Car("красный", "Ford", "седан", 90, "автомат")

truck1.start()
car.turn("налево")
truck2.speed_up(10)
car.beep()
truck1.stop()