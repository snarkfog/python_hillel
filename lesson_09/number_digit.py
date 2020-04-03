"""
10. Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего
параметра функции. Функция должна принимать три параметра: в первом параметре передаётся число для сдвига, второй
параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр задаёт
направление сдвига (по умолчанию влево (False)).
"""


def num_dig(num, dig=1, way=False):
    num = str(num)
    if not way:
        res = num[len(num) - dig:len(num)] + num[:len(num) - dig]
    else:
        res = num[dig:len(num)] + num[:dig]

    return res


fact_num = int(input("Введите число: "))
fact_dig = int(input("Введите величину сдвига: "))
fact_way = None

while True:
    fact_way = input("Введите направление сдвига (l - влево, r - вправо): ")
    if fact_way == 'r':
        fact_way = False
        break
    elif fact_way == 'l':
        fact_way = True
        break
    else:
        print("Необходимо вводить только 'l' или 'r'")
        continue

fact_res = num_dig(fact_num, fact_dig, fact_way)
print("Результат сдвига:", fact_res)
