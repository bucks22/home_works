def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(a = True, b = 132, c = 'sds')
print_params(c = '4kwew;')
print_params(b = 25)
print_params(c = [1,2,3])

print('_____________________________')

values_list = [31, (42, 46, 48), 'список.3']
values_dict = {'a': 413, 'b': 'list2', 'c': False}
for i, k in values_dict.items():
    print(i, k)
print_params(*values_list)
print_params(**values_dict)

print('_____________________________')

values_list_2 = [1412, 'slskd323']
values_dict_2 = {'b': 10000413, 'c': '1000list3'}
print_params(*values_list_2, 90)
print_params(a = [4.2, 535, 'fdsdf'], **values_dict_2)

print('_____________________________')

# Разбираюсь с подсказкой из задания
def test(a = 'mmmam', b = []):
    b.append (3232)
    b.append(90349)
    print(a, b)
test()
b = [32,2332,3245324, 65789]
test()
print(b)
test()

print('_____________________________')
def append_to_list(a = 21, list_my = None):
    if list_my is None:
      list_my = []
      list_my.append(4243)
      list_my.append(89909)
    print(list_my)
append_to_list()
list_my = [545454, 757886]
append_to_list()
print(list_my)



