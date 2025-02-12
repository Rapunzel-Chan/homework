from logger import setup_logging

masks_logger = setup_logging('masks')


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номера банковской карты"""
    card_numbers = ''.join(num if num.isdigit() else '' for num in card_number)
    if len(card_numbers) == 16:
        masks_logger.info('Удача!')
        return f"{card_number[:-17]}{card_number[-17:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    else:
        if len(card_numbers) == 0:
            masks_logger.error('Пустой номер!')
            raise ValueError("Вы не ввели номер карты")
        else:
            masks_logger.error('Проверьте номер!')
            raise ValueError("Неверный номер карты")


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номера банковского счета"""
    account_numbers = ''.join(num if num.isdigit() else '' for num in account_number)
    if len(account_numbers) != 20:
        masks_logger.error('Вы не ввели номер счета')
        raise ValueError("Неверный номер счета")
    else:
        masks_logger.info('Успех!')
        return f"Счет **{account_number[-4:]}"

if __name__ == '__main__':
    get_mask_account('Счет 11776614605963066702')
    get_mask_account('Счет 11776614605962')
    get_mask_card_number('Visa Platinum 1246377376343588')
    get_mask_card_number('')
    get_mask_card_number('124')


