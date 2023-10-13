#TODO Вывести четные числа от 2 до N по 5 в строку
n = int(input())
counter = 0
for i in range(2, n + 1):
    if not i % 2:
        counter += 1
        print(i, end=' ')
        if counter == 5:
            print('')
            counter = 0
