# Полузаполненный ромб с полосой

rows = int(input("Enter a height: "))   # Количество строк
cols = (rows * 2) - 1                   # Количество элементов в строке
print()

if (rows % 2) == 0:
    rows = rows // 2
    cols = (rows * 2) - 1
else:
    rows = (rows // 2) + 1
    cols = (rows * 2) - 1

for i in range(rows):
    for j in range(cols):
        if rows - 1 - i <= j <= rows - 1 + i:
            print("* ", end="")
        else:
            print("  ", end='')
    print()
for i in range(rows):
    if i == 0:
        continue
    for j in range(cols):
        if i == j or i == cols - j - 1 or j == cols // 2:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
