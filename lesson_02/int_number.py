"""
12. Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере
(пробелы важны!). Первая строка содержит следующее значение, а втора строка содержит предыдущее значение введёного
числа

Пример вывода:

Please enter an integer number: 1234
The next number for the number 1234 is 1235.
The previous number for the number 1234 is 1233.

или

Please enter an integer number: 0
The next number for the number 0 is 1.
The previous number for the number 0 is -1.

Вывод программы должен соответствовать примеру!
"""

int_number = int(input("Please enter an integer number: "))
text = "The {} number for the number {} is {}."
print(text.format("next", int_number, int_number + 1))
print(text.format("previous", int_number, int_number - 1))
