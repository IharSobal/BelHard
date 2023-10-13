#TODO Сделать калькулятор:
# у пользователя спрашивается число, потом действие и второе число
def calculator(num1, action, num2):
    if action == '+':
        result = num1 + num2
    elif action == '-':
        result = num1 - num2
    elif action == '*':
        result = num1 * num2
    elif action == '/':
        result = num1 / num2
    elif action == '^' or action == '**':
        result = pow(num1, num2)
    else:
        result = 'Такого действия в данном калькуляторе нет.'
    return result

n1 = int(input('Введите первое число:'))
a = input('Введите действие для расчета:')
n2 = int(input('Введите второе число:'))

print(n1, a, n2, '=', calculator(n1, a, n2))
