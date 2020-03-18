"""
9. Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
Небольшая подсказка. В этой задаче вам понадобится:
    - список
    - метод `revers()` (или срез [::-1], или вместо `revers()` использовать `insert()` тогда не придётся разворачивать
    список), чтоб развернуть список, метод `join()`
    - строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт `from string import
    ascii_uppercase`), она содержит все буквы латинского алфавита.
"""

from string import ascii_uppercase


def digit_2_letter(val):
    if val > 9:                             # цифры от 0 до 9, остаются цифрами
        return ascii_uppercase[val-10]      # цифры от 10 и далее, переводятся в буквы (А=11, В=12 и т.д.)
    else:
        return str(val)                     # ф-ия возвращает полученный символ.


def num_convert(num, num_sys):
    val_lst = []
    res = ''

    if num == 0:
        val_lst.append(num)

    while num > 0:
        val_lst.append(num % num_sys)
        num = num // num_sys
    rev_lst = val_lst[::-1]

    for num_sys in rev_lst:
        res = res + digit_2_letter(num_sys)

    return res


fact_num = int(input("Введите число: "))
fact_num_sys = int(input("Введите систему счисления (2-36): "))

print("Число {} в системе счисления {} равно {}".format(fact_num, fact_num_sys, num_convert(fact_num, fact_num_sys)))
