
from unittest.mock import patch

import pandas as pd
import pytest

from src.file_reader import read_csv_transactions, read_xlsx_transactions


@patch('pandas.read_csv')
def test_read_csv_transactions(mock_read_csv) -> None:
    mock_data = pd.DataFrame([
        {'id': '4137938', 'state': 'EXECUTED', 'date': '2023-01-04T13:13:34Z', 'amount': '15560',
         'currency_name': 'Real', 'currency_code': 'BRL', 'from': '', 'to': 'Счет 38164279390569873521',
         'description': 'Открытие вклада'},
        {'id': '4699552', 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z', 'amount': '23423',
         'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Discover 7269000803370165',
         'to': 'American Express 1963030970727681', 'description': 'Перевод с карты на карту'}
    ])

    mock_read_csv.return_value = mock_data
    file_path_csv = 'fake_path.transactions.csv'
    read_csv_transactions(file_path_csv)
    mock_read_csv.assert_called_once_with(file_path_csv, delimiter=';')


@pytest.fixture
def mock_read_excel(mocker) -> None:
    mock_read_excel = mocker.patch('pandas.read_excel')
    return mock_read_excel


def test_read_xlsx_transactions(mock_read_excel) -> None:
    mock_data = pd.DataFrame([
        {'id': '4137938', 'state': 'EXECUTED', 'date': '2023-01-04T13:13:34Z', 'amount': '15560',
         'currency_name': 'Real', 'currency_code': 'BRL', 'from': '', 'to': 'Счет 38164279390569873521',
         'description': 'Открытие вклада'},
        {'id': '4699552', 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z', 'amount': '23423',
         'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Discover 7269000803370165',
         'to': 'American Express 1963030970727681', 'description': 'Перевод с карты на карту'}
    ])
    mock_read_excel.return_value = mock_data
    file_path = 'fake_path.transactions_excel.xlsx'
    read_xlsx_transactions(file_path)
    mock_read_excel.assert_called_once_with(file_path)
