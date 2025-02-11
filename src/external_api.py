import requests
import os
from dotenv import load_dotenv

load_dotenv()


def calculate_currency_exchange(transactions) -> float:
    url = "https://api.apilayer.com/exchangerates_data/latest?symbols=USD,EUR&base=RUB"
    headers = {
        "apikey": os.getenv('API_KEY')
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Failed to get currency rates: {response.status_code} - {response.text}")
    data = response.json()
    usd_rate = data["rates"]["USD"]
    euro_rate = data["rates"]["EUR"]
    total_usd_amount = 0
    total_euro_amount = 0
    total_rub_amount = 0
    for transaction in transactions:
        amount = float(transaction['operationAmount']['amount'])
        currency_code = transaction['operationAmount']['currency']['code']
        if currency_code == 'USD':
            total_usd_amount += amount * usd_rate
        elif currency_code == 'EUR':
            total_euro_amount += amount * euro_rate
        elif currency_code == 'RUB':
            total_rub_amount += amount
    total_amount = round((total_usd_amount + total_euro_amount + total_rub_amount), 2)
    return total_amount


amount_with_rate = calculate_currency_exchange([
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }}}])
print(amount_with_rate)
