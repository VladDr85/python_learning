"""
Рекурсивные функции - это функция, которая вызывает саму себя
"""

def max_rec(value):
    """
    Максимальная глубина рекурсии 997
    """
    print(value)
    max_rec(value + 1)


#max_rec(1)


def rec(value):
    """
    Рекурсия с условием остановки
    Пример выполнения рекуррсии как вложенных функций
        - идем в глубину
        - затем поднимаемся на шаг назад и выполняем все что не выполнилось в функции
    """
    print('*' * value)
    if value < 5:
        rec(value + 1)
    print('*' * value)  # выполняется когда выходим из рекурсии


rec(1)

# Обход каталогов и файлов (дерево)
F = {
    'C': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
        }
    }
}


def get_files(paht, depth=0):
    for f in paht:
        print(' ' * depth, f)
        if type(paht[f]) == dict:
            get_files(paht[f], depth + 1)
        else:
            print(' ' * (depth + 1), ' '.join(paht[f]), )


get_files(F)