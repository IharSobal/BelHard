a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
d = (a + b + c) / 3
print("Среднее арифметическое с точностью 3 =", round(d, 3))
text = f"{d:.3f}"
print("Среднее арифметическое с точностью 3 =", text)
total = 0
for _ in range(3):
    num = float(input("Введите число: "))
    total += num
average = total/3
print("Среднее арифметическое с точностью 3 =", round(average, 3))
