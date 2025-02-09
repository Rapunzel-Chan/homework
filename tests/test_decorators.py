import pytest
from src.decorators import log, my_function


def test_log():
    assert log


def test_log_ok(capsys):
    my_function(1, 2)
    captured_outputs = capsys.readouterr()
    assert "" in captured_outputs.out


def test_log_wrong():
    with pytest.raises(Exception):
        my_function(1, 'абв')
