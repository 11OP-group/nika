product = 1

while True:
    num = float(input("Введите число: "))
    if num == 0:
        continue

    if num < 0:
        break

    if num > 0:
        product *= num

print(f"Результат произведения: {product}")