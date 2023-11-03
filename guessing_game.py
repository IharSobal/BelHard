from random import randint
def is_valid_digit(string):
    return string.isdigit()
n = input('Введите число до какого хотите угадывать (больше 1) для игры "Числовая угадайка": ')
while not is_valid_digit(n) or not int(n) > 1:
    n = input('Введите все же ЧИСЛО больше 1: ')
n = int(n)
num = randint(1, n)
print(f'Добро пожаловать в числовую угадайку от 1 до {n}.')
flag = True
counter = 0
while flag:
    s = input('Попробуйте угадать число, введите сюда: ')
    if is_valid_digit(s) and 1 <= int(s) <= n:
        s = int(s)
        counter += 1
        if s == num:
            flag = False
            print('Вы угадали, поздравляем!')
        if s < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        if s > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print(f'А может быть все-таки введем целое число от 1 до {n}?')
print('Количество ваших попыток:', counter)
print('Спасибо, что играли в числовую угадайку. Еще увидимся!!!')
