from typing import Callable
import functools



def cache(func: callable) -> callable:
    cash_storage = {}

    @functools.wraps(func)
    def wrapper(*args: tuple) -> callable:
        if args in cash_storage:
            print("Getting from cash")
            return cash_storage[args]

        print("Calculating new result")
        result = func(*args)
        cash_storage[args] = result
        return result
    return wrapper
