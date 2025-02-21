import pytest

from src.filter_sort_re import search_category_transactions, search_definite_transactions


def test_search_definite_transactions(transactions) -> None:
    assert search_definite_transactions(transactions, 'Перевод со счета на счет')


def test_search_definite_transactions_empty(transactions) -> None:
    with pytest.raises(ValueError):
        search_definite_transactions([], 'Перевод со счета на счет')


def test_search_category_transactions(transactions) -> None:
    assert search_category_transactions(transactions, {1: 'Перевод с карты на счет', 2: 'Перевод со счета на счет'})


def test_search_category_transactions_empty_category(transactions) -> None:
    with pytest.raises(ValueError):
        search_category_transactions(transactions, {})
