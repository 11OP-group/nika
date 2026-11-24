n = int(input())

last_digit = n % 10

count_3 = 0
count_last = 0
count_even = 0
sum_gt_5 = 0
prod_gt_7 = 1
count_0_and_5 = 0

num = n

while num > 0:
    digit = num % 10

    # Вложенный while: обрабатываем текущую цифру один раз
    flag = 1
    while flag:
        if digit == 3:
            count_3 += 1

        if digit == last_digit:
            count_last += 1

        if digit % 2 == 0:
            count_even += 1

        if digit > 5:
            sum_gt_5 += digit

        if digit > 7:
            prod_gt_7 *= digit

        if digit == 0 or digit == 5:
            count_0_and_5 += 1

        flag = 0

    num //= 10

print(f"Количество цифр 3: {count_3}")
print(f"Сколько раз встречается последняя цифра: {count_last}")
print(f"Количество чётных цифр: {count_even}")
print(f"Сумма цифр, больших пяти: {sum_gt_5}")
print(f"Произведение цифр, больших семи: {prod_gt_7}")
print(f"Сколько раз встречаются цифры 0 и 5: {count_0_and_5}")