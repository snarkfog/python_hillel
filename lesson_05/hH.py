"""
11. Дана строка. Замените в этой строке все появления буквы `h` на букву `H`, кроме первого и последнего вхождения.
"""

s = input("Enter a string: ")

s1 = s[s.find('h') + 1:s.rfind('h')]
s1 = s1.replace('h', 'H')

print(s[:s.find('h') + 1] + s1 + s[s.rfind('h'):])
