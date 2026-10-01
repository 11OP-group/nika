B5000 = 5000
B2000 = 2000
B1000 = 1000
B500 = 500
B200 = 200
B100 = 100

amount = int(input("Введите сумму для снятия (кратную 100): "))

print(f"Выдача суммы {amount} руб.:")

count = amount // B5000
amount = amount % B5000
print(f"  Купюр по {B5000} руб.: {count}")

count = amount // B2000
amount = amount % B2000
print(f"  Купюр по {B2000} руб.: {count}")

count = amount // B1000
amount = amount % B1000
print(f"  Купюр по {B1000} руб.: {count}")

count = amount // B500
amount = amount % B500
print(f"  Купюр по {B500} руб.: {count}")

count = amount // B200
amount = amount % B200
print(f"  Купюр по {B200} руб.: {count}")

count = amount // B100
amount = amount % B100
print(f"  Купюр по {B100} руб.: {count}")
