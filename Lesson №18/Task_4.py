from Task_3 import Box

class Truck:
    def __init__(self, capacity):
        self.capacity = capacity

    def __str__(self):
        boxes = ", ".join(str(box) for box in self.capacity)
        return f"Truck with boxes: {boxes}"

    def add(self, box):
        if len(self.capacity) == 0:
            self.capacity.append(box)
        elif len(self.capacity) < 10:
            self.capacity.append(box)
        else:
            print("Truck capacity is full")

    def sub(self, index):
        if len(self.capacity) > index and index >= 0:
            return self.capacity.pop(index)
        else:
            print("Index is out of range")

box1 = Box("Book", 2)
box2 = Box("Toy", 1.5)
box3 = Box("Shirt", 1)
box4 = Box("Shoes", 1.8)

truck = Truck([box1, box2])
print(truck)

truck.add(box3)
truck.add(box4)
print(truck)

truck.sub(1)
print(truck)

truck.sub(3)
print(truck)