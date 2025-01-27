import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions):
    generator_usd = filter_by_currency(transactions, "USD")
    #generator_rub = filter_by_currency(transactions, "RUB")
    assert next(generator_usd) == {"id": 939719570,
     "state": "EXECUTED",
     "date": "2018-06-30T02:08:58.425572",
     "operationAmount":
     {"amount": "9824.07",
      "currency":
     {"name": "USD",
      "code": "USD"
     }},
     "description": "Перевод организации",
     "from": "Счет 75106830613657916952",
     "to": "Счет 11776614605963066702"
    }



#def test_transaction_descriptions(transactions):
    assert transaction_descriptions()


#def card_number_generator(start: int, stop: int):
    """Функция выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for num in range(start, stop + 1):
        nulls = 16
        nulls -= len(str(num))
        result = "0" * nulls + str(num)
        if '0000000000000001' <= result <= '9999999999999999':
            card_number = f"{result[:-17]}{result[-17:-12]} {result[-12:-8]} {result[-8:-4]} {result[-4:]}"
            yield card_number
