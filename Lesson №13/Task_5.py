import random

def countdown(lst):
    result = ""
    for num in reversed(lst):
        result += str(num) + " "
    result += "Пуск!"
    return result

S = random.sample(range(11), random.randint(1, 10))
print(S)
print(countdown(S))