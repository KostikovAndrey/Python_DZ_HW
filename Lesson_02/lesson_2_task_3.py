import math


def square(side):
    area = side * side

    if not isinstance(side, int) and side % 1 != 0:
        area = math.ceil(area)

    return area


print(f"Сторона 5: {square(5)}")  # 25
print(f"Сторона 3.5: {square(3.5)}")  # 12.25 → округляем до 13
print(f"Сторона 2.1: {square(2.1)}")  # 4.41 → округляем до 5
print(f"Сторона 4.0: {square(4.0)}")  # 16.0 → 16 (целое число)

side_length = 4.7
result = square(side_length)
print(f"Сторона {side_length}: площадь = {result}")
