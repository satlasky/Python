# а) Цикл while

def count():
    i = 0
    while i <= 10:
        print(i)
        i += 1

# б) Рекурсия

def count(i=0):
    if i <= 10:
        print(i)
        count(i+1)

# Пример использования:
count() # Выведет числа от 0 до 10