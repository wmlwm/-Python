print('Задача №4')
print('-' * 15)

print('Поиск самой большой цифры в числе')

number = int(input('Введите целое положительное число больше 10: '))

if number > 10:
    max_number = 0
    while number > 10:
        a = number % 10
        number //= 10
        if a > max_number:
            max_number = a
    print('Самая большая цифра в числе: ', max_number)

else:
    print('Введите число больше 10')