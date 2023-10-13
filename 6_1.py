#TODO Написать функцию перевода десятичного числа в двоичное и обратно,
# без использования функции int
def convert_10_2_10(decimal_num):
    bin_num = f'{decimal_num:b}'
    dec_num = eval('0b' + bin_num)
    return dec_num

n = 2023

print(convert_10_2_10(n))
