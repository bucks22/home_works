calls = 0
def count_calls():
    global calls
    calls += 1
def string_info (string):
    count_calls()
    print((len(string), string.upper(), string.lower()))
def is_contains (string, list_to_search):
    count_calls()
    if string.lower() in str(list_to_search).lower():
        print(True)
    else:
        print(False)


string_info('Laevea')
string_info('Posa')
string_info('Waxlsa')
is_contains('Mask', ['mASk', 'Jsi23a'])
is_contains('Mask', ['ASk', 'Jsi23a'])
print(calls)

