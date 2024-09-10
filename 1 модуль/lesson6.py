my_dict = {'Aba':231, 'Net':9536, 'Lok':384230}
print(my_dict)
print(my_dict.get('Aba'))
print(my_dict.get('Tom', 'Отсутствует в словаре'))
my_dict.update({'Ena':95642,
                'Wom':56897})
print(my_dict.pop('Net'))
print(my_dict)

my_set = {13, 1, 42, 'Mor', False, 42, 2 ,3, 2 ,1, (3, 42, 13)}
print(my_set)
my_set.add (5)
my_set.update ({(34, 21, 42, 1), 67878, 345})
my_set.discard(42)
print(my_set)
