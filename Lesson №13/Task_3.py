def honest(lst):
    return [i for i in lst if i % 2 == 0]

lst = list(range(21)) # создание списка от 0 до 20
result = honest(lst)
print(result) # вывод списка четных элементов