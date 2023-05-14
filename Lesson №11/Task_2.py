def reverse(*args):
    result = ''
    for word in args:
        reversed_word = ''
        for letter in word:
            reversed_word = letter + reversed_word
        result += reversed_word
    return result
print(reverse("Здраствуйте, Сергей Вячеславович!"))