def get_mask_card_number(card_number: int) -> str:
    """Функция маскирует номера банковской карты"""
    str_card_number = str(card_number)
    return f"{str_card_number[0:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскирует номера банковского счета"""
    str_account_number = str(account_number)
    return f"**{str_account_number[-4:]}"


if __name__ == '__main__':
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
