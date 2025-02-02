from functools import wraps
from datetime import datetime
from typing import Callable, Any


def log(filename='') -> Callable[..., Any]:
    '''Декоратор, логирующий работу функции и ее результат в файл или в консоль'''
    def inner(func):
        @wraps(func)
        def wrapper(*args):
            start = datetime.now()
            try:
                result = func(*args)
                stop = datetime.now()
                if filename:
                    with open(filename, 'a', encoding='UTF-8') as file:
                        file.write(f'{start}, {stop}, {func.__name__} ok\n')
                else:
                    print(f'{start}, {stop}, {func.__name__} ok')
            except Exception as e:
                stop = datetime.now()
                with open(filename, 'a', encoding='UTF-8') as file:
                    file.write(f'{start}, {stop}, {func.__name__} error: ({e}). Inputs: {args}\n')
                raise e
            return result
        return wrapper
    return inner

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
#my_function(4, 'абв')
#
# @log()
# def my_function_without_filename(x, y):
#     return x + y
#
# my_function_without_filename(5, 8)