#TODO Вывести первые N чисел кратные M и больше K
n, m, k = int(input()), int(input()), int(input())
counter = 0
while counter < n:
    k += 1
    if not k % m:
        print(k, end=' ')
        counter += 1
