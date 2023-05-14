class Queue:
    def __init__(self):
        self.inside = []

    def __str__(self):
        return '=>'.join(self.inside)

    def add(self, name):
        self.inside.append(name)

    def take_out(self):
        self.inside.pop(0)

    def __add__(self, name):
        self.add(name)
        return self

    def __sub__(self, name):
        self.take_out()
        return self

    def __iadd__(self, name):
        self.add(name)
        return self

    def __isub__(self, name):
        self.take_out()
        return self
my_queue = Queue()
my_queue += 'Алиса'
my_queue += 'Андрей'
my_queue += 'Женя'
my_queue -= 'Алиса'
print(my_queue)