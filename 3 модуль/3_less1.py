calls = 0
def count_calls():
    global calls
    calls += 1
def string_info (string):
    count_calls()
    # print((len(string), string.upper(), string.lower()))
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search):
    count_calls()
    if string.lower() in str(list_to_search).lower():
        return True
    else:
        return False



print(string_info('Laevea'))
print(string_info('Posa'))
print(string_info('Waxlsa'))
print(is_contains('Mask', ['mASk', 'Jsi23a']))
print(is_contains('Mask', ['ASk', 'Jsi23a']))
print(calls)

