
def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions = {}
    start_position = 0

    for line_number, string in enumerate(strings, 1):
        byte_position = start_position
        file.write(string + '\n')
        start_position += len(string.encode('utf-8')) + 2
        strings_positions[(line_number, byte_position)] = string
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
