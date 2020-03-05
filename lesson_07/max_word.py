"""
Дан текст состоящий из нескольких строки. Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите последнее. Задачу необходимо решить с использованием словаря.
"""

i = "Строка '{}' встречается в тексте {} раз(а) - чаще всего."
q = int(input("Введите количество строк текста: "))
s = []
d = {}
x = 0
y = 0

while q != 0:
    a = (input("Введите строку текста: ")).split()
    s.extend(a)
    q -= 1

for key in s:
    val = d.get(key, 0)
    d[key] = val + 1

for key, val in d.items():
    if val < x:
        continue
    else:
        y, x = key, val

print(i.format(y, x))