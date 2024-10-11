# написать рандомайзер для распределения уборки на 3 человек

import random
def cleaning (*names):
    options = ['кухня', 'туалет', 'ванна', 'полы']
    # options = [1, 2, 3, 4, 5]
    win1 = random.choice(options)
    options.remove(win1)
    win2 = random.choice(options)
    options.remove(win2)
    win3 = random.choice(options)
    options.remove(win3)
    win4 = random.choice(options)
    print(*names)
    return win1, win2, win3, win4

names = ['Art', 'Nic', 'Gris', 'Vas']
win1, win2, win3, win4 = cleaning(names)
print (names[0], ':', win1)
print (names[1], ':', win2)
print (names[2], ':', win3)
print (names[3], ':', win4)