counter1 = 0
counter2 = 0
for _ in range(3):
    num = float(input("Введите число: "))
    if num >= 0:
        counter1 += 1
    else:
        counter2 += 1
print("Положительных чисел =", counter1)
print("Отрицательных чисел =", counter2)
