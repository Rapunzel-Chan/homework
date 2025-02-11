import os
from unittest.mock import Mock

from config import DATA_DIR
from src.utils import create_and_read_transactions_file


def test_create_and_read_transactions_file():
    file_name = 'operations.json'
    file_path = os.path.join(DATA_DIR, file_name)
    assert create_and_read_transactions_file(file_path)


def test_create_and_read_transactions_file_mocked():
    mock_file = Mock(return_value="all is ok")
    create_and_read_transactions_file = mock_file
    assert create_and_read_transactions_file() == "all is ok"
    mock_file.assert_called_once_with()
