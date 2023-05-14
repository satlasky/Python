class Battery:
    def __init__(self, max_charge=5):
        self.capacity = []
        self.max_charge = max_charge

    def charge(self):
        if len(self.capacity) < self.max_charge:
            self.capacity.append(')')

    def discharge(self):
        if self.capacity:
            self.capacity.pop()

    def __str__(self):
        return '[' + ''.join(self.capacity) + ']' + (')' * (self.max_charge - len(self.capacity)))

b = Battery()
b.charge()
b.charge()
b.charge()
b.charge()
b.charge()
b.charge()
print(b)