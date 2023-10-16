#TODO Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести имена тех,
# у кого не указана почта (нет ключа email или значение этого ключа - пустая строка)
user_1 = {'name': 'Masha', 'surname': 'Ivanova', 'phon': '+375005550001', 'email': 'Iv@mail.com'}
user_2 = {'name': 'Petya', 'surname': 'Petrov', 'phon': '+375005550002'}
user_3 = {'name': 'Vasya', 'surname': 'Sidorov', 'phon': '+375005550003', 'email': 'Si@mail.com'}
user_4 = {'name': 'Katya', 'surname': 'Nikolaeva', 'phon': '+375005550004', 'email': ''}
d = {1: user_1, 2: user_2, 3: user_3, 4: user_4}
for i in d.keys():
    if 'email' not in d[i] or d[i]['email'] == '':
        print(d[i]['name'])
