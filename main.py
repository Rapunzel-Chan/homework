import os
from collections import Counter

from config import DATA_DIR
from src.file_reader import read_csv_transactions, read_xlsx_transactions
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import create_and_read_transactions_file
from src.widget import get_mask_account_card


def main() -> None:
    """Функция собирает всю функциональность проекта"""
    print('''Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n Выберите необходимый пункт меню:
          1. Получить информацию о транзакциях из JSON-файла\n
          2. Получить информацию о транзакциях из CSV-файла\n
          3. Получить информацию о транзакциях из XLSX-файла''')
    user_input = int(input())
    if user_input == 1:
        file_path = os.path.join(DATA_DIR, 'operations.json')
        filtered_transactions = create_and_read_transactions_file(file_path)
        print('Для обработки выбран JSON-файл.')
    elif user_input == 2:
        file_path = os.path.join(DATA_DIR, 'transactions.csv')
        filtered_transactions = read_csv_transactions(file_path)
        print('Для обработки выбран CSV-файл.')
    elif user_input == 3:
        file_path = os.path.join(DATA_DIR, 'transactions_excel.xlsx')
        filtered_transactions = read_xlsx_transactions(file_path)
        print('Для обработки выбран XLSX-файл.')
    else:
        print('Некорректный выбор.')
        return
    while True:
        print('''Введите статус, по которому необходимо выполнить фильтрацию.
    \nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
        status_input = input().upper()
        if status_input in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Операции отфильтрованы по статусу {status_input}')
            filtered_id_state = filter_by_state(filtered_transactions, status_input)
            break
        else:
            print(f'Статус операции {status_input} недоступен.')

    while True:
        print('Отсортировать операции по дате? Да/Нет')
        sort_input = input().title()
        if sort_input == 'Да':
            sorted_transactions = sort_by_date(filtered_id_state)
            break
        elif sort_input == 'Нет':
            sorted_transactions = filtered_id_state
            break
        else:
            print('Некорректный ввод.')

    while True:
        print('Отсортировать по возрастанию или по убыванию?')
        order_input = input().lower()
        if order_input == 'по возрастанию':
            sorted_transactions_date = sort_by_date(filtered_id_state, reverse=False)
            break
        elif order_input == 'по убыванию':
            sorted_transactions_date = sorted_transactions
            break
        else:
            print('Некорректный ввод.')

    while True:
        print('Выводить только рублевые тразакции? Да/Нет')
        currency_input = input().title()
        if currency_input == 'Да':
            filtered_transactions_currency = list(filter_by_currency(sorted_transactions_date, 'RUB'))
            break
        elif currency_input == 'Нет':
            filtered_transactions_currency = sorted_transactions_date
            break
        else:
            print('Некорректный ввод.')

    while True:
        print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
        description_input = input().title()
        if description_input == 'Да':
            sorted_transactions_description = sorted(filtered_transactions_currency, key=lambda x: x['description'])
            break
        elif description_input == 'Нет':
            sorted_transactions_description = filtered_transactions_currency
            break
        else:
            print('Некорректный ввод.')

    print('Распечатываю итоговый список транзакций...')

    if not sorted_transactions_description:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    else:
        if user_input == 1:
            formatted_transactions = []
            for transaction in sorted_transactions_description:
                date = transaction.get('date', 'Дата не указана')
                description = transaction.get('description', 'Описание не указано')
                amount = transaction['operationAmount'].get('amount', 'Сумма не указана')
                currency = transaction['operationAmount']['currency'].get('name', 'Валюта не указана')
                from_account = get_mask_account_card(transaction.get('from', ''))
                to_account = get_mask_account_card(transaction.get('to', ''))
                formatted_output = (f'{date} {description}\n{from_account} -> {to_account}\nСумма: '
                                    f'{amount} {currency}\n')
                formatted_transactions.append(formatted_output)
            counted_and_filtered_transactions = Counter(formatted_transactions)
            print(f'Всего банковских операций в выборке: {len(counted_and_filtered_transactions)}')
        else:
            formatted_transactions = []
            print(sorted_transactions_description)
            for transaction in sorted_transactions_description:
                print(transaction)
                date = transaction.get('date', 'Дата не указана')
                description = transaction.get('description', 'Описание не указано')
                amount = transaction.get('amount', 'Сумма не указана')
                from_account = get_mask_account_card(transaction.get('from', ''))
                to_account = get_mask_account_card(transaction.get('to', ''))
                if user_input == 1:
                    currency = transaction.get('name', 'Валюта не указана')
                else:
                    currency = transaction.get('currency_code', 'Валюта не указана')
                formatted_output = (f'{date} {description}\n{from_account} -> '
                                    f'{to_account}\nСумма: {amount} {currency}\n')
                formatted_transactions.append(formatted_output)
            counted_and_filtered_transactions = Counter(formatted_transactions)
            print(f'Всего банковских операций в выборке: {len(counted_and_filtered_transactions)}')

        for transaction in formatted_transactions:
            print(transaction)


if __name__ == "__main__":
    main()
