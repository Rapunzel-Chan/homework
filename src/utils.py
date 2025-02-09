import json
import requests
import os
from config import DATA_DIR
import external_api

file_name = 'operations.json'
file_path = os.path.join(DATA_DIR, file_name)
file_url = 'https://drive.usercontent.google.com/u/0/uc?id=1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy&export=download'

def create_transactions_file():
    try:
        response = requests.get(file_url)
        transactions = response.json()
        with open(file_path, 'w') as f:
            json.dump(transactions, f)
        return transactions
    except (json.JSONDecodeError, ValueError):
        return []
def calculate_currency_exchange(transaction) -> float:
    return amount
#     if transactions == [] or transactions not in [] or j_file doesn't exist
#
#
#
#
#
#
#
# def stat_decorator(func):
#     """Декоратор для вывода статистики по отфильтрованным транзакциям."""
#
#     def wrapper(*args, **kwargs):
#         filtered_transactions = func(*args, **kwargs)
#         total_amount = sum([transaction['amount'] for transaction in filtered_transactions])
#         print(f"Отфильтровано {len(filtered_transactions)} транзакций на сумму {total_amount}")
#         return filtered_transactions
#
#     return wrapper
#
# @stat_decorator
# def filter_transactions_by_currency(input_file, output_file, currency):
#     """Фильтрует транзакции по валюте и сохраняет результат в новый файл."""
#
#     with open(input_file, 'r') as f:
#         transactions = json.load(f)
#
#     filtered_transactions = [transaction for transaction in transactions if transaction['currency'] == currency]
#
#     with open(output_file, 'w') as f:
#         json.dump(filtered_transactions, f, indent=4)
#
#     return filtered_transactions
#
# def main():
#     input_file = 'transactions.json'
#     output_file = 'transactions_filtered.json'
#     currency = 'USD'
#
#     filtered_transactions = filter_transactions_by_currency(input_file, output_file, currency)
#     print(filtered_transactions)

if __name__ == '__main__':
    print(create_transactions_file())

