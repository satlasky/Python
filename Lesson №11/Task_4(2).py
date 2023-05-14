# a) Цикл while

def count():
    even = 0
    odd = 0
    i = 0
    while i <= 10:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
        i += 1
    print("Четных чисел:", even)
    print("Нечетных чисел:", odd)


count()

# б) Рекурсия

def count(n, even=0, odd=0):
    if n == 0:
        print("Четных чисел:", even)
        print("Нечетных чисел:", odd)
    else:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
        count(n - 1, even, odd)


count(10)
