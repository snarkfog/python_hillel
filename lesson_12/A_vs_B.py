"""
2. Имеется строка вида: AABABBAABBBAB. Необходимо написать функцию которая заменит буквы A на B, а B, соответственно,
на A. Замену можно производить ТОЛЬКО используя функцию replace(). В результате применения функции к исходной строке,
функция должна вернуть строку: BBABAABBAAABA
"""

fact_str = "AABABBAABBBAB"


def a_replace_b(cond_str):
    cond_str1 = ""
    i = 0

    while i != len(cond_str):
        if cond_str[i] == "A":
            cond_str1 = cond_str1 + cond_str[i].replace("A", "B")
        elif cond_str[i] == "B":
            cond_str1 = cond_str1 + cond_str[i].replace("B", "A")
        else:
            cond_str1 = cond_str1 + cond_str[i]
        i += 1

    return cond_str1


print(a_replace_b(fact_str))
