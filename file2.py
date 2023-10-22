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
