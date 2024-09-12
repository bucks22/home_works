import random

first_number = random.randint(3, 20)
result = []
print(f'Число в первой ячейке: {first_number}')
for i in range(1, 21):
    for j in range(1, 21):
        if first_number % (i + j) == 0 and j > i:
            result.append(i)
            result.append(j)
result1 = ''
for k in result:
    result1 += str(k)

print('Шифр:', result1)