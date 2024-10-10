def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding = 'utf-8')

    file.write(list(strings) + '\n')

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
