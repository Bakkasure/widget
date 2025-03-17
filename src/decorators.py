import datetime
from functools import wraps
from typing import Any

from _collections_abc import Callable


def log(filename: str) -> Callable:
    """Декоратор для логирования вызовов функций"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{datetime.datetime.now()} {func.__name__} ok")
                else:
                    print(f"{datetime.datetime.now()} {func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(
                            f"{datetime.datetime.now()} {func.__name__} error: "
                            f"{e.__class__.__name__}. Inputs: {args}, {kwargs}"
                        )
                else:
                    print(
                        f"{datetime.datetime.now()} {func.__name__} error: "
                        f"{e.__class__.__name__}. Inputs: {args}, {kwargs}"
                    )
                raise

        return wrapper

    return decorator
