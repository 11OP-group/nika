numbers = [10, 20, 30, 40, 50]
target = int(input("Введите число для поиска: "))

for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Индекс числа {target}: {i}")
        break
else:
    print("Нет такого числа")