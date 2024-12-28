def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номера банковской карты"""
    return f"{card_number[:-17]}{card_number[-17:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номера банковского счета"""
    return f"Счет **{account_number[-4:]}"


if __name__ == '__main__':
    print(get_mask_card_number('Maestro 1596837868705199'))
    print(get_mask_card_number('Visa Classic 6831982476737658'))
    print(get_mask_account('Счет 73654108430135874305'))
