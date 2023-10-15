#TODO Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка незаконно
s = [1, 2, 3, 4, 5, 'a', 'b', 'c', 6, 7, 8, 'ab', 'bc', 'ac', 9, 10]
def filter_str(in_list):
    if type(in_list) is str:
        return True
    else:
        return False
s = [*filter(filter_str, s)]
print(s)
