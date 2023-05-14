# а) Решение с помощью цикла while:

def Fibonacci():
    fib_list = [0, 1]
    i = 1
    while True:
        next_num = fib_list[i] + fib_list[i-1]
        if next_num >= 100:
            break
        fib_list.append(next_num)
        i += 1
    return fib_list

print(Fibonacci())

# б) Решение с помощью рекурсии:

def Fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_rec(n-1) + Fibonacci_rec(n-2)

def Fibonacci():
    fib_list = []
    i = 0
    while True:
        next_num = Fibonacci_rec(i)
        if next_num >= 100:
            break
        fib_list.append(next_num)
        i += 1
    return fib_list

print(Fibonacci())