import pytest

from src.widget import get_data, get_mask_account_card


@pytest.mark.parametrize('card_account, expected', [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                                    ('MasterCard 1786547763705147', 'MasterCard 1786 54** **** 5147'),
                                                    ('Счет 35383033474447895560', 'Счет **5560'),
                                                    ('Счет 64686473678894779589', 'Счет **9589')]
                         )
def test_get_mask_account_card(card_account, expected):
    assert get_mask_account_card(card_account) == expected


def test_get_mask_account_card_wrong_card_number()-> None:
    with pytest.raises(ValueError):
        get_mask_account_card('MasterCard 1787763705147')


def test_get_mask_account_card_empty_card_number():
    with pytest.raises(ValueError):
        get_mask_account_card('')


def test_get_mask_account_card_wrong_account_number():
    with pytest.raises(ValueError):
        get_mask_account_card('Счет 646864736788989')


def test_get_mask_account_card_empty_account_number():
    with pytest.raises(ValueError):
        get_mask_account_card('')


def test_get_data():
    assert get_data('2024-03-11T02:26:18.671407') == '11.03.2024'


def test_get_data_wrong():
    with pytest.raises(ValueError):
        get_data('')
