#TODO Дан список чисел, необходимо для каждого элемента посчитать сумму его соседей,
# для крайних чисел одним из соседей является число с противоположной стороны списка
s = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(s)):
    if s[i] == s[len(s) - 1]:
        i = -1
    sum_i = s[i] + s[i - 1] + s[i + 1]
    print(sum_i)
