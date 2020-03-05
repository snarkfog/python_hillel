"""1. Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна
быть произведена над ними. Функция должна вернуть результат вычислений зависящий от третьего аргумент +, сложить
их; если —, то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть
строку "Неизвестная операция".
"""


def arithmetic(x, y, z):
    if z == "+":
        return x + y
    elif z == "-":
        return x - y
    elif z == "*":
        return x * y
    elif z == "/":
        if y != 0:
            return x / y
        else:
            return "На ноль делить нельзя."
    else:
        return "Неизвестная операция"


first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
operation = input("Введите операцию: ")

result = arithmetic(first_number, second_number, operation)

print("-" * 10)
print("Результат:", result)
