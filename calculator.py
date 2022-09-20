num_1 = float(input('Введите первое число: '))
znak = input('Введите один из предложенных знаков: +, -, *, /: ')
num_2 = float(input('Введите второе число: '))
if znak == '+':
    result = num_1 + num_2
    print('Результат равен: ' + str(result))
elif znak == '-':
    result = num_1 - num_2
    print('Результат равен: ' + str(result))
elif znak == '*':
    result = num_1 * num_2
    print('Результат равен: ' + str(result))
elif znak == '/':
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        result = 0
        print('На ноль делить нельзя!')
    print('Результат равен: ' + str(result))
else:
    print('Такой знак использовать нельзя!')

