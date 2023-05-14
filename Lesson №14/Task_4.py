fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


class FibonacciIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.lst):
            raise StopIteration
        num = self.lst[self.index]
        self.index += 1
        return num


fib_iter = FibonacciIterator(fibonacci_numbers)

# Пустой итератор №1
for num in fib_iter:
    pass
print("Итерация по пустому итератору №1")

# Пустой итератор №2
while True:
    try:
        next(fib_iter)
    except StopIteration:
        break
print("Итерация по пустому итератору №2")