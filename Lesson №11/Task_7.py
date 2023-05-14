users = {'user1': 'pass1', 'user2': 'pass2'}  # пример базы пользователей


def login():
    # запрашиваем у пользователя логин и пароль
    login = input('Введите логин: ')
    password = input('Введите пароль: ')

    # проверяем по базе
    if login in users:
        if users[login] == password:
            print('Доступ разрешен')
        else:
            print('Доступ запрещен')
    else:
        # если пользователя с таким логином нет - записываем его в базу
        users[login] = password
        print('Регистрация прошла успешно')
print(login())