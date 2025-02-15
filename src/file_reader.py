import csv
import os

import pandas as pd

from config import DATA_DIR

file_path_csv = os.path.join(DATA_DIR, 'transactions.csv')
file_path_xlsx = os.path.join(DATA_DIR, 'transactions_excel.xlsx')


def read_csv_transactions(file_path_csv):
    """Функция считывает csv.file и выводит список словарей с транзакциями"""
    with open(file_path_csv) as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            print(row)


def read_xlsx_transactions(file_path_xlsx):
    """Функция считывает xlsx.file и возвращает список словарей с транзакциями"""
    excel_data = pd.read_excel(file_path_xlsx)
    transactions = excel_data.to_dict(orient='records')
    return transactions


if __name__ == '__main__':
    read_csv_transactions(file_path_csv)
    transactions = read_xlsx_transactions(file_path_xlsx)
    for transaction in transactions:
        print(transaction)
