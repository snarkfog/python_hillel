"""
3. Реверс списка
    - Принцип алгоритма заключается в следующем: мы меняем местами 0-ый элемент с последним, 1-ый с предпоследним и д.т.
    - Итого количество таких обменов будет равно половине длины списка. Иначе элементы поменяются местами
    по-второму кругу и вернутся в первоначальное положение.
"""


def lst_rev():
    lst = input("Введите символы через пробел: ").split()
    lst_half = len(lst) // 2
    lst_all = len(lst) - 1

    for i in range(lst_half):
        lst[i], lst[lst_all - i] = lst[lst_all - i], lst[i]
    return lst


print(lst_rev())