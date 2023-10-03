#TODO Без использования collections, написать программу, которая будет создавать
# словарь для подсчитывания количества вхождения каждой буквы в текст введенный с клавиатуры
text = input()
#text = 'Доброго дня, родной город Минск, и всего наилучшего!'
text = text.lower()
some_list = list(text)
some_dict = {}
#some_tuple = tuple(text)
for i in some_list:
    some_dict_letter = {i: some_list.count(i)}
    if i.isalpha():
        some_dict.update(some_dict_letter)
print(some_dict)
# print(some_list)
# print(some_tuple)
#print(some_list.count('д'))
#print(''.join(some_list))
