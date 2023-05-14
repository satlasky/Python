def fibonacci():
    fib_list = [0, 1]
    for i in range(8):
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
    return fib_list

print(fibonacci())