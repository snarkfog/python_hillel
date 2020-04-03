"""
3. Дан словарь ключами которого являются английские слова, а занчениями - списки латинских слов. Необходимо развеннуть
словарь. Другими словани, необходимо, на основании заданного словаря, создать новый словарь, у которого в качестве
ключей будут взяты латинские слова, из первого словаря, а значениями будут, соответствующие им, английские слова.
d = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}

"""

from pprint import pprint

d = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}

lat = {}

for i in d:
    for j in d[i]:
        if j not in lat:
            lat[j] = i
        else:
            lat[j] = lat[j] + ", " + i

pprint(lat)
