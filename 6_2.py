#TODO Код Морзе для представления цифр и букв использует тире и точки.
# Напишите функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
# (словари в помощь)
def code_morze(text):
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    morse = [
        '.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
        '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
        '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--',
        '-..-', '-.--', '--..', '-----', '.----', '..---', '...--',
        '....-', '.....', '-....', '--...', '---..', '----.'
    ]
    dict_morse = dict(zip(letters, morse))
    input_s = text.upper()
    output_s = (dict_morse.get(letter) for letter in input_s if dict_morse.get(letter))
    return ' '.join(output_s)

s = 'Hello World'

print(code_morze(s))
