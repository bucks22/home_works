def add_everything_up(a, b):
    if type(a) != bool and isinstance(b, (float, str, int)):
        try:
            c = a + b
        except TypeError as TE:
            c = str(a) + str(b)
        return c
    else:
        print('Введите числа или строки')
    return None

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))