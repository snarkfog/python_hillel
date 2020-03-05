"""
4. Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
которому этот месяц принадлежит (зима, весна, лето или осень).
"""


def season(month):
    if 1 <= month <= 2 or month == 12:
        return "Зима"
    elif 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    else:
        return "Ошибка! Число должно быть от 1 до 12"


month_number = int(input("Введите число от 1 до 12: "))

result = season(month_number)

print("-" * 50)
print("Месяц {} принадлежит ко времени года - {}.".format(month_number, result))
