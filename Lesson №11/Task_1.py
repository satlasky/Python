def calculator():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    oper = input("Введите операцию (+, -, /, *): ")

    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1 * num2
    elif oper == "/":
        if num2 == 0:
            return "Ошибка: деление на 0 невозможно"
        else:
            return num1 / num2
    else:
        return "Ошибка: неверная операция"


print(calculator())