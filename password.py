attempts = 0

while True:
    password = input("Введите пароль: ")
    attempts += 1

    if password == "admin":
        print("Доступ разрешен")
        break

    if attempts == 3:
        print("Вход заблокирован")
        break