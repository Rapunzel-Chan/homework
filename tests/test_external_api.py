from unittest.mock import patch

from src.external_api import calculate_currency_exchange


def test_calculate_currency_exchange(transactions):
    assert calculate_currency_exchange(transactions)


@patch('requests.get')
def test_calculate_currency_exchange_with_error(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"rates": {"USD": 5, "EUR": 1}}
    transactions = [{'operationAmount': {'amount': "123", 'currency': {'code': 'USD'}}}]
    result = calculate_currency_exchange(transactions)
    expected_value = float(123) * 5
    assert result == expected_value
