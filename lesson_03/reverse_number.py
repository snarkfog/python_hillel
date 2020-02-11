"""
TASK*:	Дано целое, положительное, трёхзначное число. Например: 123, 867, 374. Необходимо его перевернуть. Например,
если ввели число 123, то должно получиться на выходе ЧИСЛО 321. ВАЖНО! Работать только с числами. Строки использовать
НЕЛЬЗЯ!
"""

number = int(input("Введите трехзначное положительное число: "))

if number < 100 or number > 999:
    print("")
    print("Число должно быть положительным трехзначным.")
else:
    reverse_number = number                                                     # Сохраняем начальное число для вывода
    reverse_number_1 = reverse_number % 10                                      # Сохраняем третье число
    reverse_number_2 = reverse_number // 10                                     # Отбрасываем третье число
    reverse_number_3 = reverse_number_2 % 10                                    # Сохраняем второе число
    reverse_number_4 = reverse_number_2 // 10                                   # Отбрасываем второе число
    reverse_number_1 *= 100                                                     # Увеличваем разряд третьего числа
    reverse_number_3 *= 10                                                      # Увеличваем разряд второго числа
    reverse_number = reverse_number_1 + reverse_number_3 + reverse_number_4     # К третьему прибавляем второе и первое
    print("")
    print("Обратным числу {} является число {}.".format(number, reverse_number))
