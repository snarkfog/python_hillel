"""
Написать функцию сортировки двухмерного списка МхМ (матрицы)
Значение М - задаётся пользователем, с клавиатуры. Может быть любым
целым, положительным числом, больше 5.

Функция должна:
1. найти сумму элементов столбцов и отсортировать столбцы по
возрастанию этих сумм

2. отсортировать каждый нечётный столбец по возрастанию значений снизу
вверх, а каждый чётный столбец по возрастанию значений сверху вниз.
Так же, ваша программа должна иметь функцию вывода данного списка
на экран. При выводе, внизу каждого столбца должна выводиться сумма
элементов этого столбца.
Что можно использовать:

1. для создания списка использовать ТОЛЬКО 'list comprehension' и
генератор случайных чисел. Диапазон случайных чисел для заполнения
списка от 1 до 50. Список должен создаваться однострочным
выражением.

2. Можно использовать ТОЛЬКО ДВА списка. Первый это двухмерный список
размером МхМ, второй, вспомогательный, одномерный список размером
М. Использование других списков (или коллекций) НЕДОПУСТИМО.

3. Можно использовать ТОЛЬКО ОДНУ переменную М для хранения размера
списка, плюс переменные циклов for.

4. Для сортировки можно использовать алгоритм пузырьковой сортировки.
Использование встроенных функций сортировки - НЕДОПУСТИМО (да и не
получится их использовать)!

5. Решение должно включать ТОЛЬКО ДВЕ функции: функцию сортировки (по
правилам описанным выше) и функцию вывода на экран.
Задача считается решённой верно при условии соблюдения всех требований.
Аккуратный вывод на экран - приветствуется.

Пример вывода задачи:

До сортировки
 47 48 36 12 39 33 13 1 47 20
 17 2 9 40 2 1 36 35 48 44
 50 24 20 29 27 49 8 50 20 32
 30 3 17 33 43 10 17 2 42 19
 14 5 50 38 17 18 24 26 19 24
 12 41 45 12 4 33 33 16 36 25
 15 27 12 30 22 36 45 46 43 21
 46 34 34 47 22 34 45 12 47 19
 31 47 2 1 12 45 44 26 11 23
 25 49 47 50 36 9 36 10 21 26
 287 280 272 292 224 268 301 224 334 253

После сортировки
 43 1 44 1 50 2 50 1 45 11
 39 2 32 9 47 3 47 12 45 19
 36 10 26 10 45 5 46 12 44 20
 27 12 25 18 36 24 31 29 36 21
 22 16 24 33 34 27 30 30 36 36
 22 26 23 33 20 34 25 33 33 42
 17 26 21 34 17 41 17 38 24 43
 12 35 20 36 12 47 15 40 17 47
 4 46 19 45 9 48 14 47 13 47
 2 50 19 49 2 49 12 50 8 48
 224 224 253 268 272 280 287 292 301 334
"""

from random import randint

m = int(input("Введите размер матрицы: "))

matrix = [[randint(1, 50) for i in range(m)] for i in range(m)]


def matrix_print(m, matrix, message):

    if message == 0:
        message = "\tДо сортировки:"
    else:
        message = "\tПосле сортировки:"

    # Вывод матрицы
    print()
    print(message)
    for i in range(m):
        for j in range(m):
            print("{:>4}".format(matrix[i][j]), end="")
        print("", " ")

    # Создание списка сумм столбцов
    total = 0  # Сумма стобца
    lst = []  # Список сумм столбцов
    for j in range(m):
        for i in range(m):
            total += matrix[i][j]
        lst.append(total)
        total = 0

    # Вывод сумм столбцов
    print()
    for i in lst:
        print("{:>4}".format(i), end="")
    print()


def matrix_sort(m, matrix):
    # Создание списка сумм столбцов
    total = 0  # Сумма столбца
    lst = []  # Список сумм столбцов
    for j in range(m):
        for i in range(m):
            total += matrix[i][j]
        lst.append(total)
        total = 0

    # Сортировка столбцов и списка
    for _ in range(m):
        flag = True
        for col in range(m - 1):
            if lst[col] > lst[col + 1]:
                for elem in range(m):
                    matrix[elem][col], matrix[elem][col + 1] = matrix[elem][col + 1], matrix[elem][col]
                lst[col], lst[col + 1] = lst[col + 1], lst[col]
                flag = False
        if flag:
            break

    # Сортировка элементов в столбцах
    for col in range(m):
        for j in range(m):
            for i in range(m - 1):

                if j % 2 == 1:  # Нечетные столбцы
                    flag = True
                    if matrix[i][j] > matrix[i + 1][j]:
                        matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
                        flag = False
                    if flag:
                        continue

                else:  # Четные столбцы
                    flag = True
                    if matrix[i][j] < matrix[i + 1][j]:
                        matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
                        flag = False
                    if flag:
                        continue


matrix_print(m, matrix, 0)
matrix_sort(m, matrix)
matrix_print(m, matrix, 1)
