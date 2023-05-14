def calculate():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = input("Введите операцию(+,-,*,/): ")
    expression = str(num1) + operation + str(num2)

    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Деление на ноль невозможно"
    except:
        return "Неверная операция"
print(calculate())