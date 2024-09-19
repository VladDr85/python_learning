"""
Параметр – это переменная, которая используется при создании функции.
Аргумент – это фактическое значение, которое мы передаем при вызове функции.

Параметры могут быть
    - обязательные     # def sum(a, b):
    - не обязательные  # def sum(a = 0, b = 0):
Аргументы бывают:
    - позиционные      # sum(1, 2)
    - ключевые         # sum(b = 2, a = 1)
"""

'''
Аргументы переменной длины
*args    # Позиционные аргументы переменной длины в виде кортежа
**kwargs # Ключевые аргументы переменной длины (от keyword arguments) в виде словаря

'''


def sum_arg(a, *args):
    print(a, args)
    return a + sum(args)


sum_arg(1, 10, 20, 30)


def sum_arg(a, **kwargs):
    print(a, kwargs)
    return a + sum(kwargs.values())


sum_arg(a=10, b=10, c=20, d=30)


def os_path(disk, *args, sep='\\', **kwargs):
    '''
     Смешенная передача аргументов и порядок их объявления
    '''
    print(args)
    print(kwargs)
    args = (disk,) + args
    if 'trim' in kwargs and kwargs['trim']:
        args = [x.strip() for x in args]

    path = sep.join(args)
    print(path, '\n')


os_path('F:', ' репозиторий_1 ', ' ркпозиторий2', 'файл.фу ', sep='/', trim=True)
os_path('F:', ' репозиторий_1 ', ' ркпозиторий2', 'файл.фу ', sep='/', trim=False)
os_path('F:', ' репозиторий_1 ', ' ркпозиторий2', 'файл.фу ', sep='/')
