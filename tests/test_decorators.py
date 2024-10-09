import datetime
from typing import Any

import pytest

from scr.decorators import log


@log(filename="")
def example_func(x: int, y: int) -> int:
    """Функция складывает 2 числа"""
    return x + y


def test_decorator_success(capsys: Any) -> None:
    example_func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == f"{datetime.datetime.now()} example_func ok\n"


def test_decorator_failed() -> None:
    with pytest.raises(TypeError):
        example_func(1, "a")
