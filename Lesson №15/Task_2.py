class Good:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def calc(self):
        self.cost = self.price * self.weight


apple = Good('apple', price=100, weight=1.5)
pear = Good('pear', price=120, weight=0.8)

apple.calc()
pear.calc()

print(f"{apple.name} cost: {apple.cost}")
print(f"{pear.name} cost: {pear.cost}")