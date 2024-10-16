def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(2, result):
            if result % i == 0:
                print('Составное')
                return result
            print('Простое')
            return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result


print(sum_three(1, 4, 6))
