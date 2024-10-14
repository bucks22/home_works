
def apply_all_func(int_list, *functions):
    try:
        result = {}
        for func in functions:
            result[func.__name__] = func(int_list)
        return result
    except:
        return ('Ошибка, введите список из чисел')

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9, 'as'], len, sum, sorted))

