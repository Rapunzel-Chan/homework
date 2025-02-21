import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number('Maestro 6831982476737658') == 'Maestro 6831 98** **** 7658'


def test_get_mask_card_number_wrong_card_number() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number('Visa Classic 82476737658')


def test_get_mask_card_number_empty_card_number() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number('')


def test_get_mask_account() -> None:
    assert get_mask_account('Счет 73654108430135874305') == 'Счет **4305'


def test_get_mask_account_wrong_account_number() -> None:
    with pytest.raises(ValueError):
        get_mask_account('Счет 736541084304305')
