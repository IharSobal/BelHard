x = 0
y = 0
for _ in range(3):
    num = float(input("Введите число: "))
    if num >= 0:
        x += 1
    else:
        y += 1
print("Положительных чисел =", x)
print("Отрицательных чисел =", y)
