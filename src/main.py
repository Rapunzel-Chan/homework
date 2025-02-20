import os
from src.file_reader import read_csv_transactions, read_xlsx_transactions
from src.utils import create_and_read_transactions_file
from config import DATA_DIR
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency, transaction_descriptions
from src.masks import get_mask_card_number, get_mask_account
from collections import Counter
from src.widget import get_mask_account_card
from src.filter_sort_re import search_definite_transactions, search_category_transactions

def main():
    print('''Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n Выберите необходимый пункт меню:
          1. Получить информацию о транзакциях из JSON-файла\n
          2. Получить информацию о транзакциях из CSV-файла\n
          3. Получить информацию о транзакциях из XLSX-файла''')

    user_input = int(input())
    if user_input == 1:
        file_path = os.path.join(DATA_DIR, 'operations.json')
        filtered_transactions = create_and_read_transactions_file(file_path)
        print('Для обработки выбран JSON-файл.')
        print(filtered_transactions)


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
            filtered_transactions_description = list(search_definite_transactions(filtered_transactions_currency, 'Перевод организации'))
            break
        elif description_input == 'Нет':
            filtered_transactions_description = filtered_transactions_currency
            break
        else:
            print('Некорректный ввод.')

    print('Распечатываю итоговый список транзакций...')




    if not filtered_transactions_description:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    else:
        formatted_transactions = []
        for transaction in filtered_transactions_description:
            date = transaction.get('date', 'Дата не указана')  # Provide default value if the field is missing
            description = transaction.get('description', 'Описание не указано')
            amount = transaction['operationAmount'].get('amount', 'Сумма не указана')
            currency = transaction['operationAmount']['currency'].get('name', 'Валюта не указана')
            from_account = get_mask_account_card(transaction.get('from', ''))
            to_account = get_mask_account_card(transaction.get('to', ''))
            formatted_output = f"{date} {description}\n{from_account} -> {to_account}\nСумма: {amount} {currency}\n"
            formatted_transactions.append(formatted_output)
        counted_and_filtered_transactions = Counter(transaction['id'] for transaction in filtered_transactions_description)
        print(f'Всего банковских операций в выборке: {len(counted_and_filtered_transactions)}')

        for transaction in formatted_transactions:
            print(transaction)

if __name__ == "__main__":
    main()
#
# 08.12.2019 Открытие вклада
# Счет **4321
# Сумма: 40542 руб.
#
# 12.11.2019 Перевод с карты на карту
# MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
# Сумма: 130 USD
#
# 18.07.2018 Перевод организации
# Visa Platinum 7492 65** **** 7202 -> Счет **0034
# Сумма: 8390 руб.
#
# 03.06.2018 Перевод со счета на счет
# Счет **2935 -> Счет **4321
# Сумма: 8200 EUR
#


