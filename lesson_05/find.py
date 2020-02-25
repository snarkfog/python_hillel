"""
3. Пользователь вводит, отдельно, строку `s` и один символ `ch`. Необходимо выполнить поиск в строке `s` всех символов
`ch`.
Для решения можно использовать только функцию `find`(rfind), операторы  if и while.
"""

s = input("Enter a string: ")
ch = input("Введите symbol: ")
i = 0
a = 0

while a != -1:
    a = s.find(ch, i)
    if a == -1:
        continue
    i = a + 1
    print(a, end=", ")
