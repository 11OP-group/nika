prices_str = '100 50 200 150 75 300'

print(f"Исходная строка: {prices_str}\n")

# 1. Разбить строку на список цен (split)
prices_list_str = prices_str.split()
print(f"1. Список строк: {prices_list_str}")

# 2. Преобразовать в числа
# Используем генератор списка для перевода строк в целые числа
prices = [int(price) for price in prices_list_str]
print(f"2. Список чисел: {prices}")

# 3. Удалить самый дорогой товар (300)
max_price = max(prices)
prices.remove(max_price)
print(f"3. После удаления {max_price}: {prices}")

# 4. Добавить новый товар со скидкой (50% от максимума)
# 50% от 300 = 150. Приводим к целому числу для аккуратности
discount_price = int(max_price * 0.5)
prices.append(discount_price)
print(f"4. Добавлен товар со скидкой ({discount_price}): {prices}")

# 5. Отсортировать от меньшего к большему
prices.sort()
print(f"5. После сортировки: {prices}")

# 6. Вывести все цены через запятую
# Метод join работает только со строками, поэтому конвертируем числа обратно в строки
prices_for_join = [str(price) for price in prices]
prices_joined = ", ".join(prices_for_join)
print(f"6. Цены через запятую: {prices_joined}")

# 7. Вывести среднюю цену
average_price = sum(prices) / len(prices)
print(f"7. Средняя цена: {average_price:.2f}")