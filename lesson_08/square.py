"""
3. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью
кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
"""

from math import sqrt


def square(formal_side):
    perimeter = formal_side * 4
    sqr = formal_side ** 2
    diagonal = sqrt(2) * formal_side
    formal_result = (perimeter, sqr, diagonal)
    return formal_result


user_side = int(input("Введите сторону квадрата: "))

result = square(user_side)
print("-" * 50)
print("Периметр, площадь и диагональ соответсвенно {}.".format(result))
