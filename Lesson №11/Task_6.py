# а) Решение через цикл while
def factorial(num):
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result

print(factorial(5))


# б) Решение через рекурсию
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))