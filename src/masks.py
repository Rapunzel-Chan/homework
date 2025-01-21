def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номера банковской карты"""
    card_numbers =''.join(num if num.isdigit() else '' for num in card_number)
    if len(card_numbers) == 16:
        return f"{card_number[:-17]}{card_number[-17:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    else:
        if len(card_numbers) == 0:
            raise ValueError("Вы не ввели номер карты")
        else:
            raise ValueError("Неверный номер карты")


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номера банковского счета"""
    account_numbers =''.join(num if num.isdigit() else '' for num in account_number)
    if len(account_numbers) != 20:
        raise ValueError("Неверный номер счета")
    else:
        return f"Счет **{account_number[-4:]}"
