#TODO Дан словарь, ключ - Название страны, значение - список городов,
# на вход поступает город, необходимо сказать из какой он страны
d = {
    'Belarus': ['Minsk', 'Brest', 'Vitebsk', 'Grodno', 'Gomel', 'Mogilev'],
    'Russia': ['Moscow', 'Saint Petersburg', 'Pskov', 'Novgorod'],
    'Germany': ['Berlin', 'Hamburg', 'Mun-hen', 'Bзначению phpremen'],
    'France': ['Paris', 'Bordo', 'Lion', 'Nica', 'Marsel']
}
city = 'Hamburg'
for i in d.keys():
    for j in d[i]:
        if city.lower() == j.lower():
            print(i)
            break
