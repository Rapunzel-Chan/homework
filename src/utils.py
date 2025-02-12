import json
import os
from logger import setup_logging


import requests

from config import DATA_DIR

utils_logger = setup_logging('utils')

file_name = 'operations.json'
file_path = os.path.join(DATA_DIR, file_name)
file_url = 'https://drive.google.com/uc?export=download&id=1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy'


def create_and_read_transactions_file(file_path: str) -> list:
    """Функция возвращает список словарей банковских операций, загруженных из внешнего хранилища"""
    try:
        if not isinstance(file_path, str):

            raise TypeError("The 'file_path' must be a string.")
        response = requests.get(file_url)
        response.raise_for_status()
        with open(file_path, 'w') as f:
            f.write(response.text)
        with open(file_path, 'r') as f:
            transactions = json.load(f)
        if len(transactions) > 0 and isinstance(transactions, list):
            utils_logger.info('Получилось!')
            return transactions
        else:
            return []
    except (json.JSONDecodeError, ValueError):
        return []
    except requests.exceptions.HTTPError:
        print("HTTP Error. Please check the URL.")
    except TypeError as e:
        utils_logger.error(f"TypeError: {e}")
        return []


# if __name__ == '__main__':
#     print(create_and_read_transactions_file(file_path))
#     print(create_and_read_transactions_file(123))
