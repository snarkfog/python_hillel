"""
2. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
Окончанием ввода пусть служит
пустая строка. Каждая введённая строка, в файле, должна начинаться с новой строки.
"""

lst = []
while True:
    file_input = input("Введите данные: ")
    if file_input != "":
        lst.append(file_input)
    else:
        break

print(lst)

file_write = open("file_2.txt", "w", encoding="utf-8")
for line in lst:
    file_write.write(line)
    file_write.write("\n")

file_write.close()
