from functools import wraps
from time import time


def log(filename=''):
    """ Декоратор логирует работу функции и ее результат как в файл 'filename', так и в консоль. """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_start = time()
            try:
                result = func(*args, **kwargs)
                data_log = f'{func.__name__} OK'
                if filename:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(data_log)
                else:
                    print(data_log)
                return result
            except Exception as e:
                data_log = f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}'
                if filename:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(data_log)
                else:
                    print(data_log)
            time_finish = time()
        return wrapper
    return decorator


@log(filename='')
def my_function(x, y):
    return x + y


print(my_function(1, 2))
