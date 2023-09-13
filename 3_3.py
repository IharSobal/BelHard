import args as args
import kwargs as kwargs

name = input("Введите Ваше имя:")
age = int(input("Введите ваш возраст:"))
city = input("Введите ваш город проживания:")
text1 = "Привет %s возрастом %d лет из города %s" % (name, age, city)
print(text1)
text2 = "Привет {} возрастом {} лет из города {}".format(name, age, city)
print(text2)
text3 = f"Привет {name} возрастом {age} лет из города {city}"
print(text3)
