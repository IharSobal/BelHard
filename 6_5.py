#TODO Дан список чисел, необходимо его развернуть без использования
# метода reverse и функции reversed, а так же дополнительного списка и среза
s = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(s) // 2):
    s[i], s[-i -1] = s[-i -1], s[i]
print(s)

