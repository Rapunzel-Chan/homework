from unittest.mock import patch

import pytest

from main import main

mock_transactions = [
    {"id": 1, "date": "2025-02-21", "description": "Payment", "operationAmount":
        {"amount": 100, "currency": {"name": "RUB"}}},
    {"id": 2, "date": "2025-02-22", "description": "Transfer", "operationAmount":
        {"amount": 200, "currency": {"name": "USD"}}},
    {"id": 3, "date": "2025-02-23", "description": "Payment", "operationAmount":
        {"amount": 150, "currency": {"name": "RUB"}}}
]


@pytest.fixture
def mock_file_processing():
    with patch('src.utils.create_and_read_transactions_file', return_value=mock_transactions), \
            patch('src.file_reader.read_csv_transactions', return_value=mock_transactions), \
            patch('src.file_reader.read_xlsx_transactions', return_value=mock_transactions):
        yield


def test_main_invalid_file_input(mock_file_processing):
    user_inputs = ['5', 'EXECUTED', 'Да', 'по возрастанию', 'Да', 'Перевод организации']
    with patch('builtins.input', side_effect=user_inputs):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Некорректный выбор.")
