def cesar(text):
    result = ""

    # Приводим все буквы к нижнему регистру
    text = text.lower()

    # Проходимся по каждому символу в тексте
    for i in range(len(text)):
        char = text[i]

        # Если символ - буква английского алфавита, то сдвигаем его на 3 позиции вправо
        if char.isalpha():
            result += chr((ord(char) - 97 + 3) % 26 + 97)
        else:
            result += char

    return result
print(cesar("Where is my Coca-Cola?"))