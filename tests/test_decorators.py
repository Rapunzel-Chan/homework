from typing import Any

import pytest

from src.decorators import log, my_function


def test_log() -> None:
    assert log


def test_log_ok(capsys: Any) -> None:
    my_function(1, 2)
    captured_outputs = capsys.readouterr()
    assert "" in captured_outputs.out


def test_log_wrong() -> None:
    with pytest.raises(Exception):
        my_function(1, 'абв')
