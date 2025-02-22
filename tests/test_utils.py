import os
from unittest.mock import Mock, mock_open, patch

import pytest
from requests.models import Response

from config import DATA_DIR
from src.utils import create_and_read_transactions_file


def test_create_and_read_transactions_file() -> None:
    file_name = 'operations.json'
    file_path = os.path.join(DATA_DIR, file_name)
    assert create_and_read_transactions_file(file_path)


def test_create_and_read_transactions_file_wrong() -> None:
    with pytest.raises(TypeError):
        create_and_read_transactions_file(123)


def test_http_error(mock_get) -> None:
    mock_response = Response()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    with patch("builtins.open", mock_open()) as mock_file:
        transactions = create_and_read_transactions_file('test_path/operations.json')
    assert transactions == []
    mock_file.assert_not_called()


@pytest.fixture
def mock_get(mocker) -> None:
    return mocker.patch("requests.get")


def test_invalid_json(mock_get) -> None:
    mock_response = Response()
    mock_response.status_code = 200
    mock_response._content = b'Invalid JSON content'
    mock_get.return_value = mock_response
    m = mock_open(read_data='Invalid JSON content')
    with patch("builtins.open", m) as mock_file:
        transactions = create_and_read_transactions_file('test_path/operations.json')
    assert transactions == []
    mock_file.assert_called_with('test_path/operations.json', 'r', encoding='utf-8')


def test_create_and_read_transactions_file_mocked() -> None:
    mock_file = Mock(return_value="all is ok")
    create_and_read_transactions_file = mock_file
    assert create_and_read_transactions_file() == "all is ok"
    mock_file.assert_called_once_with()
