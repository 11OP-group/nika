n = int(input("Введите число: "))

odd_numbers = []
# Формируем список нечётных чисел от 1 до n включительно
for number in range(1, n + 1):
    if number % 2 != 0:
        odd_numbers += [number]

print(f"Список нечётных чисел: {odd_numbers}")