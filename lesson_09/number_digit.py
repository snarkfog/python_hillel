"""
10. Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего
параметра функции. Функция должна принимать три параметра: в первом параметре передаётся число для сдвига, второй
параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр задаёт
направление сдвига (по умолчанию влево (False)).
"""


def num_dig(num, dig=1, way=False):
    if way:
        num = num * (10 ** dig)
    elif not way:
        num = num * (10 ** -dig)
    return num


print()
print(num_dig(10))
print(num_dig(10, 2, True))
print()

fact_num = int(input("Введите число: "))
default = input("По-умолчанию, выполняется сдвиг на 1 разряд влево. Желаете изменить? (y - да, n - нет): ")
fact_dig = None
fact_way = None

if default == "y":
    fact_dig = int(input("Введите величину сдвига: "))
    fact_way = input("Введите направление сдвига (l - влево, r - вправо): ")

if fact_way == "l":
    fact_way = False
elif fact_way == "r":
    fact_way = True

elif default == "n":
    fact_dig = 1
    fact_way = False

res = num_dig(fact_num, fact_dig, fact_way)
print("Результат сдвига: ", res)
