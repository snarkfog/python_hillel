# Пустой треугольник

rows = int(input("Enter a height: "))   # Количество строк
cols = (rows * 2) - 1                   # Количество элементов в строке
print()

for i in range(rows):
    for j in range(cols):
        if rows - 1 - i == j or j == rows - 1 + i or i == rows - 1:
            if j == rows - 1 - i or j == rows - 1 + i or i == rows - 1:
                print("* ", end="")
        else:
            print("  ", end="")
    print()
