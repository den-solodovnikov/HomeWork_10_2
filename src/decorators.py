from functools import wraps
from time import time


def log(filename=''):
    """ Декоратор логирует работу функции и ее результат как в файл 'filename', так и в консоль. """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_start = time()
            try:
                func(*args, **kwargs)
                data_log = f'{func.__name__} OK'
            except Exception as e:
                data_log = f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}'
            time_finish = time()
            if filename == '':
                print(data_log)
            else:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(data_log)
        return wrapper
    return decorator


@log(filename='')
def my_function(x, y):
    return x + y


my_function(1, '2')
