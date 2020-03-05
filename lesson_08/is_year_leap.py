"""
2. Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и
False иначе.
"""


def is_year_leap(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True


leap_year = int(input("Введите год: "))
result = is_year_leap(leap_year)
print(result)
