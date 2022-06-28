import time
from functools import wraps
from typing import Any, Callable, TypeVar, cast

F = TypeVar('F', bound=Callable[..., Any])


def timeit(func: F) -> F:
    @wraps(func)
    def wrapped(*args, **kwargs):  # type: ignore
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"func:{func.__name__} took: {elapsed:2.4f} sec")
        return result

    return cast(F, wrapped)
