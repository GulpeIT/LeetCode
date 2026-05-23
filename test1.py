import asyncio
import functools
from typing import Callable, Coroutine

def counter(num: int):
    def inner(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(args, kwargs)
            return result
        return wrapper
    return inner

# def async_a():
#     def b(func: Coroutine):
#         async def wrapper(*arg, **args):
#             print("call coroutine")
#             await func(*arg, **args)
#         return wrapper
#     return b

@counter(0)
def foo(see: str, boo: str):
    """
    Docstring для foo
    
    :param see: маму
    :type see: str
    :param boo: param буу
    :type boo: str
    """
    print(see+boo)

# @async_a()
# async def async_def():
#     print("test_1")

if __name__ == '__main__':
    foo("laa", "lyy")
    print(foo.__name__)
    print(foo.__doc__)
    # asyncio.run(async_def())