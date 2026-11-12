import math

limit = 150

# Вычисляем 5 степени заранее, чтобы не возводить каждый раз в цикле

p5 = [i**5 for i  in range(limit+1)]
# Множество для быстрой проверки, является ли сумма 5 степенью
p5_set = set(p5)

find = False

for a in range(1, limit - 3):
    for b in range(a+1, limit - 2):
        for c in range(b+1,limit-1):
            for d in range(c+1,limit):
                total_sum = p5[a] + p5[b] + p5[c] + p5[d]
                if total_sum > p5[limit]:
                    break
                if total_sum in p5_set:
                    e = int(round(total_sum**(1/5)))
                    if p5[e] == total_sum:
                        print(f"Решение: а = {a}, b = {b}, c = {c}, d = {d}")
                        sum_abcde = a+b+c+d+e
                        print(f"a + b + c + d + e = {sum_abcde}")

                        find = True
                    break
                if find: break
        if find: break
    if find: break


