PI = 3.14

def calculate_rectangle_area (width, height):
    """
    Рассчитывает площадь прямоугольника
    Args:
        width, height (float) : ширина и высота соответственно
    Returns:
        width*height : площадь прямоугольника
    """
    return width*height

def calculate_circle_area(radius):
    """
    Рассчитывает площадь круга
    Args:
        radius (float) : радиус
    Returns:
        PI*radius**2 : площадь прямоугольника
    """
    return PI*radius**2

width, height = map(float, input("Введите ширину и высоту прямоугольника через пробел: ").split())
print(f"Площадь прямогульника: {calculate_rectangle_area(width,height)}")

radius = float(input("Введите радиус круга: "))
print(f"Площадь круга: {calculate_circle_area(radius)}")

