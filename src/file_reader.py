import os
from typing import Any

import pandas as pd

from config import DATA_DIR

file_path_csv = os.path.join(DATA_DIR, 'transactions.csv')
file_path_xlsx = os.path.join(DATA_DIR, 'transactions_excel.xlsx')


def read_csv_transactions(file_path_csv: Any):
    """Функция считывает csv.file и выводит список словарей с транзакциями"""
    df = pd.read_csv(file_path_csv, delimiter=';')
    transactions_csv = df.to_dict(orient='records')
    for row in transactions_csv:
        print(row)


def read_xlsx_transactions(file_path_xlsx: Any):
    """Функция считывает xlsx.file и возвращает список словарей с транзакциями"""
    excel_data = pd.read_excel(file_path_xlsx)
    transactions_xlsx = excel_data.to_dict(orient='records')
    return transactions_xlsx


# if __name__ == '__main__':
#     read_csv_transactions(file_path_csv)
#     transactions_xlsx = read_xlsx_transactions(file_path_xlsx)
#     for transaction in transactions_xlsx:
#         print(transaction)
