# text = input('Введите возраст ')
# while not text.isdigit():
#     text = input('Введите возраст числом ')
# sum_vklad = float(input())
# def is_palindrom(a):
#     a = input()
#     b = reversed(a)
#     if
# def text(key: str, messege: str) -> list[int]:
#     key = SYSTEM
#     messege = LONDON
#     for i in range(len(key)):
#
#         print(i)
# def find_shop(shops: dict[str, list[str]], product: str) -> list[str]:
#     result = []
#     for shop, products in
#
# def spisok(spisok_strok: str, okonchanie: str) -> list[str]:
#     spisok_strok = spisok_strok.split()
#
# 28n+30k+31m=365 |13,12,11
# for n in range(1, 13):
#     for k in range(1, 12):
#         for m in range(1,11):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print('n =', n, 'k =', k, 'm =', m)
#
# 100 rub, kupit 100 golov scota, bic 10, korova 5, telok 0.5
# b+k+t=100 ; 10b+5k+0.5t=100
# for b in range(1, 10):
#     for k in range(1, 20):
#         for t in range(1,200):
#             if 10 * b + 5 * k + 0.5 * t == 100 and b + k + t == 100:
#                 print('b =', b, 'k =', k, 't =', t)
#
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     counter = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             counter += 1
#     if counter == 2:
#         print(i)
#Числа Рамануджана
# for z in range(1729, 36000):
#     for a in range(1, 33):
#         for b in range(a, 33):
#             for c in range(b, 33):
#                 for d in range(c, 33):
#                     if a ** 3 + b ** 3 == c ** 3 + d ** 3 == z and a != c and a != d and a != b and c != d and c != b and d != b:
#                         print(z, a, b, c, d)
# s = 'abcdef'
# for c in s:
#     print(c)
#
# print(chr(ord('A') + 1))
# s = '    Python rocks!     '
# print(s.strip())
# count = 0
# my_list = []
# for i in range(97, 123):
#     count += 1
#     s = chr(i) * count
#     my_list.append(s)
# print(my_list)
# numbers = [8, 9, 10, 11]
# del numbers[1]
# numbers.insert(1, 17)
# print(numbers)
# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# n = len(a)
# a2 = []
# for i in range(n):
#     for j in a:
#         a2.append(min(a))
#         a.remove(min(a))
# a = a2
# print(a)
# print(pow(243, 1/5))
# объявление функции
# def convert_to_miles(km):
#     return num * 0.6214
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(convert_to_miles(num))
# def get_days(month):
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         return (31)
#     elif month in [4, 6, 9, 11]:
#         return (30)
#     else:
#         return (28)
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(get_days(num))
# объявление функции
# def get_factors(num):
#     return len([i for i in range(1, num + 1) if num % i == 0])
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_factors(n))
# объявление функции
# def find_all(target, symbol):
#     my_list = []
#     count = -1
#     for i in target:
#         count += 1
#         if i == symbol:
#             my_list.append(count)
#     return my_list
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))

# объявление функции
# def merge(list1, list2):
#     list1 += list2
#     list1.sort()
#     return list1
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
# # print(numbers1, numbers2)
# # вызываем функцию
# print(merge(numbers1, numbers2))
# объявление функции
# def is_valid_triangle(side1, side2, side3):
#     return True if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2 else False
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))
# объявление функции
# def get_next_prime(num):
#     counter = 0
#     num2 = num + 1
#     while counter != 2:
#         for i in range(1, num2 + 1):
#             if num2 % i == 0:
#                 counter += 1
#         if counter != 2:
#             num2 += 1
#             counter = 0
#         else:
#             return num2
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_next_prime(n))
# # объявление функции
# def is_one_away(word1, word2):
#     counter = 0
#     if len(word1) == len(word1):
#         for i in range(len(word1)):
#             if word1[i] == word2[i]:
#                 counter += 1
#     if counter == len(word1) - 1:
#         return True
#     else:
#         return False
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))
# text = 'А роза упала на лапу Азора.'
# s = list(text.lower())
# s1 = [i for i in s if i.isalpha()]
# # s1 = []
# # for i in s:
# #     if i.isalpha():
# #         s1.append(i)
# if s1 == s1[::-1]:
#     print(s1)
# else:
#     print(False)
# объявление функции
# def is_valid_password(password):
#     s = password.split(':')
#     counter = 0
#     count =0
#     t1, t2, t3 = s[0], s[1], s[2]
#     if t1 == t1[::-1]:
#         counter += 1
#     for i in range(1, int(t2) + 1):
#         if int(t2) % i == 0:
#             count += 1
#     if count == 2:
#         counter += 1
#     if int(t3) % 2 == 0:
#         counter += 1
#     if counter == 3:
#         return True
#     else:
#         return False
#
#
# # считываем данные
# psw = '565:30:50'
#
# # вызываем функцию
# print(is_valid_password(psw))
# # print('asdf'[::-1])
# объявление функции
# def is_correct_bracket(text):
# text = 'ThisIsCamelCased'
# s = list(text)
# s1 = []
# for i in s:
#     if i.isupper():
#         s1.append('_')
#         s1.append(i.lower())
#         continue
#     s1.append(i)
# del s1[0]
# # print(''.join(s1))
# print(s1)
# from math import pi
# # объявление функции
# def get_circle(radius):
#     c_l = 2 * pi * radius
#     s = pi * pow(radius, 2)
#     return c_l, s
#
# # считываем данные
# r = float(input())
#
# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)
# for i in range(8):
#     print(' ' * (7 - i), '*' * (1 + i * 2), sep='')
# d = {
#     1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
#     6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять',
#     11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
#     16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать',
#     30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
#     80: 'восемьдесят', 90: 'девяносто'
# }
# num = 25
# if 1 <= num <= 20:
#     print(d.get(num))
# if 21 <= num <= 99:
#     two = num % 10
#     one = num // 10 * 10
#     if two == 0:
#         print(d.get(one))
#     else:
#         print(d.get(one), d.get(two))
# d = {
#     'ru': {
#         1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь',
#         7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'
#     },
#     'en': {
#         1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june',
#         7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'
#     }
# }
# lan = 'en'
# num = 10
# print(d.get(lan).get(num))
# date = '11.06.1960'
# text = 'Hello world'
# text2 = 'abcdefghijklmnopqrstuvwxyz'
# # s = text.lower().split()
# s = text.lower().split()
# s2 = list(text2)
# s1 = []
# for i in s:
#     s1.extend(i)
# if set(s1) == set(s2):
#     print(True)
# else:
#     print(False)
text = 'Блажен, кто верует, тепло ему на свете!'
for i in text:
    if i.isalpha():
        sim = ord(i) + 10
        if sim > 1103:
            sim -= 64
        print(chr(sim), end='')
    else:
        print(i, end='')
print(ord('А'), ord('Я'), ord('а'), ord('я'))
text = 'To be, or not to be, that is the question!'
for i in text:
    if i.isalpha():
        if i.isupper():
            sim = ord(i) + 17
            if sim > 90:
                sim -= 26
        if i.islower():
            sim = ord(i) + 17
            if sim > 122:
                sim -= 26
        print(chr(sim), end='')
    else:
        print(i, end='')
print(ord('A'), ord('Z'), ord('a'), ord('z'), [chr(i) for i in range(91, 97)])
