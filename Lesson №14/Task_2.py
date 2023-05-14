def alphabet_generator():
    for letter in range(ord('a'), ord('z')+1):
        yield chr(letter)

# Пример использования
for letter in alphabet_generator():
    print(letter)

# Опустошение генератора
list(alphabet_generator())