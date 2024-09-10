first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
elif first != second and second != third:
    print('0')
else:
    print('Что-то пошло не так')