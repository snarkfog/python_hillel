"""
1. Представьте себе бухгалтерскую книгу в книжном магазине. В этой книге хранятся
записи о номере заказа, названии книги, колличестве и стоимости одной книги, как
представленно ниже, в таблице.
+--------------+------------------------------------+----------+----------------+
| Order Number | Book Title and Author | Quantity | Price per Item |
+--------------+------------------------------------+----------+----------------+
| 34587 | Learning Python, Mark Lutz | 4 | 40.95 |
| 98762 | Programming Python, Mark Lutz | 5 | 56.80 |
| 77226 | Head First Python, Paul Barry | 3 | 32.95 |
| 88112 | Einfuhrung in Python3, Bernd Klein | 3 | 24.99 |
+--------------+------------------------------------+----------+----------------+
Напишите программу на Python, которая на вход получает список списков:
[
[34587, 'Learning Python, Mark Lutz', 4, 40.95],
[98762, 'Programming Python, Mark Lutz', 5, 56.80],
[77226, 'Head First Python, Paul Barry', 3, 32.95],
[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]
и возвращает список кортежей. Каждый кортеж состоит из номера заказа и произведения
цены на товары и количества. Стоимость товара должена быть увеличена на $10, если
стоимость заказа меньше $100. Программа должна использовать lambda и map.
"""

inp = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

lst = list(map(lambda x: (x[0], round(x[2] * x[3] if x[2] * x[3] >= 100 else x[2] * x[3] + 10, 2)), inp))
print(lst)
