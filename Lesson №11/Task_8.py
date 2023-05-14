def guess_num(correct, attempts=10):
    """
    Функция рекурсивно предлагает пользователю отгадать случайное число.
    :param correct: правильный ответ
    :param attempts: количество оставшихся попыток (10 по умолчанию)
    """
    if attempts == 0:
        print(f"Вы проиграли! Было загадано число {correct}.")
        return

    guess = int(input(f"Угадайте число от 0 до 100 (осталось попыток: {attempts}): "))
    if guess == correct:
        print("Поздравляю! Вы угадали!")
        return
    elif guess < correct:
        print("Загаданное число больше введенного.")
    else:
        print("Загаданное число меньше введенного.")

    guess_num(correct, attempts - 1)


# пример вызова функции с загаданным числом 42
guess_num(42)