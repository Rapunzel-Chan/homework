import json
import requests
import os
from config import DATA_DIR

file_name = 'operations.json'
file_path = os.path.join(DATA_DIR, file_name)
file_url = 'https://drive.google.com/uc?export=download&id=1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy'

def create_and_read_transactions_file(file_path):
    try:
        response = requests.get(file_url)
        response.raise_for_status()
        with open(file_path, 'w') as f:
            f.write(response.text)
        with open(file_path, 'r') as f:
            transactions = json.load(f)
        if len(transactions) > 0 and isinstance(transactions, list):
            return transactions
        else:
            return []
    except (json.JSONDecodeError, ValueError):
        return []



if __name__ == '__main__':
    print(create_and_read_transactions_file(file_path))

