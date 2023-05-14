names = ["Сергей", "Андрей", "Александр"]

def hello():
    name = input("Введите имя: ")
    if name in names:
        print(f"Привет, {name}!")
    else:
        names.append(name)
        print(f"Привет, {name}! Рад знакомству.")

hello()