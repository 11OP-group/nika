import math

try:
    x1, y1 = map(int, input("Введите координаты первой клетки: ").split())
    x2, y2 = map(int, input("Введите координаты второй клетки: ").split())

    if any(a<1 or a>8 for a in (x1, y1, x2, y2)):
        raise ValueError("Упс! Мы за пределами доски.")
except ValueError as e:
    print(f"Ошибка ввода! {e}")

# Заметим, что математически движение "наискосок" возможно, если столбцы и строки отличаются
# на одинаковое количество клеток. Т.к. "число различия" положительное, используем abs()
if abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")
