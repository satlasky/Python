# а)

def countdown():
    for i in range(10, -1, -1):
        yield i


for num in countdown():
    print(num)


# б)

def countdown():
    for i in range(10, -1, -1):
        yield i


generator = countdown()

while True:
    try:
        print(next(generator))
    except StopIteration:
        break