from typing import Callable
import functools


def cache(func: callable) -> callable:
    cache_storage = {}

    @functools.wraps(func)
    def wrapper(*args: tuple) -> callable:
        if args in cache_storage:
            print("Getting from cashe")
            return cache_storage[args]

        print("Calculating new result")
        result = func(*args)
        cache_storage[args] = result
        return result
    return wrapper
