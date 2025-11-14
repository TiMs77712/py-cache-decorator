from typing import Callable
import functools



def cache(func: callable) -> callable:
    cashe_storage = {}

    @functools.wraps(func)
    def wrapper(*args: tuple) -> callable:
        if args in cashe_storage:
            print("Getting from cashe")
            return cashe_storage[args]

        print("Calculating new result")
        result = func(*args)
        cashe_storage[args] = result
        return result
    return wrapper
