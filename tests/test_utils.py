import pytest
from src.utils import create_and_read_transactions_file
from unittest.mock import Mock

def test_create_and_read_transactions_file():
    assert create_and_read_transactions_file()

def test_create_and_read_transactions_file():
    with pytest.raises(ValueError):
        create_and_read_transactions_file('123')


def test_create_and_read_transactions_file():
    mock_file = Mock(return_value="all is ok")
    create_and_read_transactions_file = mock_file
    assert create_and_read_transactions_file() == "all is ok"
    mock_file.assert_called_once_with()


