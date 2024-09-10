def get_matrix ():
    n = [4, 42, 324]
    m = [6, 54, 363]
    value = [43, 9, 32, 64, 357, 45634, 32]
    matrix = []
    for i in n:
        matrix.append(i)
        for k in m:
            matrix.append(value)
    return matrix
get_matrix()
print(matrix)

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

