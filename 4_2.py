#TODO Без использования collections, написать программу, которая будет создавать
# словарь для подсчитывания количества вхождения каждой буквы в текст введенный с клавиатуры
#text = input()
text = 'Доброго дня, родной город Минск, и всего наилучшего!'
text = text.lower()
some_list = list(text)
some_tuple = tuple(text)
for i in range(len(some_list)):
    print(some_list.count(i))

#some_dict =
# print(some_list)
# print(some_tuple)
#print(some_list.count('д'))
#print(''.join(some_list))
