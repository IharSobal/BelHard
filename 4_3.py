#TODO Заполнить словарь где ключами будут выступать числа от 0 до n,
# а значениями вложенный словарь с ключами "name" и "email",
# а значения для этих ключей будут браться с клавиатуры
n = int(input())
some_dict = {}
my_dict = {}
for i in range(n + 1):
    some_dict['name'] = input()
    some_dict['email'] = input()
    my_dict_1 = {i: some_dict}
    my_dict.update(my_dict_1)
print(my_dict)
