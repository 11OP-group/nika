import random

numbers_list = [random.randint(1, 100) for _ in range(5)]
print(f"Исходный список: {numbers_list}")

# Ищем индекс минимального элемента вручную
min_index = 0
for i in range(1, len(numbers_list)):
    if numbers_list[i] < numbers_list[min_index]:
        min_index = i

numbers_list[0], numbers_list[min_index] = numbers_list[min_index], numbers_list[0]

print(f"Индекс минимального элемента: {min_index}")
print(f"Список после обмена: {numbers_list}")