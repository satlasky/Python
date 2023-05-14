def alphabet():
    # а) вывод букв и их порядкового номера
    for i in range(26):
        print(f"{i + 1}: {chr(i + 65)}")

    # б) создание словаря
    alpha_dict = {}
    for i in range(26):
        alpha_dict[i + 1] = chr(i + 65)
    print(alpha_dict)


alphabet()