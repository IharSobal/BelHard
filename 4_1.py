#TODO Заполнить список степенями числа 2 от 2**1 до 2**n
n = int(input())
spisok = []
for i in range(1, n+1):
    spisok.append(2**i)
print(spisok)
