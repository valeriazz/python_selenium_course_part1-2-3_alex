a = int(input('Введите первое значение: '))
b = int(input('Введите второе значение: '))

try:
    result = int(a / b)
except ZeroDivisionError:
    result = 0
    print('На ноль делить нельзя')
print('Результат: ' + str(result))

result2 = a + b
print(result2)

#ZeroDivisionError
#ValueError

