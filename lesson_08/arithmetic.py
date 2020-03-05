"""1. Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна
быть произведена над ними. Функция должна вернуть результат вычислений зависящий от третьего аргумент +, сложить
их; если —, то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть
строку "Неизвестная операция".
"""


def arithmetic(x, y, z):
    if z == "+":
        res = x + y
    elif z == "-":
        res = x - y
    elif z == "*":
        res = x * y
    elif z == "/":
        if y != 0:
            res = x / y
        else:
            res = "Ошибка! На ноль делить нельзя."
    else:
        res = "Неизвестная операция"

    return res


first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
operation = input("Введите операцию: ")

result = arithmetic(first_number, second_number, operation)

print("-" * 10)
print("Результат операции {} числа {} на число {} является: {}.".format(operation, first_number, second_number, result))
