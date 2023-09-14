a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
x = 0
y = 0
if a >= 0:
    x += 1
else:
    y +=1
if b >= 0:
    x += 1
else:
    y +=1
if c >= 0:
    x += 1
else:
    y +=1
print("Положительных чисел =", x)
print("Отрицательных чисел =", y)
