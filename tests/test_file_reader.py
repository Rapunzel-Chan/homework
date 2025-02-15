import os
import unittest
from unittest.mock import Mock, mock_open, patch

import pandas as pd

from src.file_reader import read_csv_transactions, read_xlsx_transactions


@patch('builtins.open', mock_open(read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n"
                                            "4137938;EXECUTED;2023-01-04T13:13:34Z;15560;Real;BRL;;Счет "
                                            "38164279390569873521;Открытие "
                                            "вклада\n4699552;EXECUTED;2022-03-23T08:29:37Z;23423;Peso;PHP;Discover "
                                            "7269000803370165;American Express 1963030970727681;Перевод с карты на "
                                            "карту"))
@patch('csv.DictReader')
@patch('builtins.print')
def test_read_csv_transactions(mock_print, mock_dict_reader, mock_open):
    mock_data = [
        {'id': '4137938', 'state': 'EXECUTED', 'date': '2023-01-04T13:13:34Z', 'amount': '15560',
         'currency_name': 'Real', 'currency_code': 'BRL', 'from': '', 'to': 'Счет 38164279390569873521',
         'description': 'Открытие вклада'},
        {'id': '4699552', 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z', 'amount': '23423',
         'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Discover 7269000803370165',
         'to': 'American Express 1963030970727681', 'description': 'Перевод с карты на карту'}
    ]

    mock_dict_reader.return_value = mock_data
    file_path_csv = os.path.join('fake', 'path', 'transactions.csv')
    read_csv_transactions(file_path_csv)
    mock_print.assert_any_call(mock_data[0])
    mock_open.assert_called_once_with(file_path_csv)
    mock_dict_reader.assert_called_once_with(mock_open())


@patch('pandas.read_excel')
def test_read_xlsx_transactions(self, mock_read_excel):
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
    mock_read_excel.assert_called_once_with(file_path)
