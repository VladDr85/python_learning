import time

"""
Декоратор - расширние функционала существующей функции.
Добавляются операторы ДО и ПОСЛЕ вызова существующей функции.
"""


# Общее определение декоратора
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print('\tЧто-то, до вызова функции')
        res = func(*args, **kwargs)
        print('\tЧто-то, после вызова функции')
        return res

    return wrapper


def some_func(tiltle: str, tag: str):
    print(f'\t\tРаботает: {tiltle}')
    res = f'\t\ttiltle = {tiltle}, tag = {tag}'
    return res


# f = func_decorator(some_func)
# f()
some_func = func_decorator(some_func)
res = some_func('Основная функция', 'h1')
print(res)


###########################################################

# Практическое примерение декоратора + декорирование через @.

def test_time(func):
    """
    Универсальный декоратор вычисления времени работы функции
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        dt = end_time - start_time
        print(f'Время работы функции: {dt}')
        return res

    return wrapper


@test_time
def get_nod(a, b):
    """
    Медленный алгоритм Евклида
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


res_1 = get_nod(2, 1000000)
res_2 = get_fast_nod(2, 1000000)

print(res_1, res_2)
