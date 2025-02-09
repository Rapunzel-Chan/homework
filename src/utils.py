import json
import requests
import os
from config import DATA_DIR

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

#     if transactions == [] or transactions not in [] or j_file doesn't exist

if __name__ == '__main__':
    print(create_transactions_file())

