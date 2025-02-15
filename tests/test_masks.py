import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number('Maestro 6831982476737658') == 'Maestro 6831 98** **** 7658'


def test_get_mask_card_number_wrong_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number('Visa Classic 82476737658')


def test_get_mask_card_number_empty_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number('')


def test_get_mask_account():
    assert get_mask_account('Счет 73654108430135874305') == 'Счет **4305'


def test_get_mask_account_wrong_account_number():
    with pytest.raises(ValueError):
        get_mask_account(['Счет 736541084304305', 'Счет 7365 410 84301 35 85'])
