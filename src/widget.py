from src.masks import get_mask_account, get_mask_card_number


def get_mask_account_card(account_card: str) -> str:
    """Функция маскирует номера как банковской карты, так и счета"""
    if "Счет" in account_card:
        account_mask = get_mask_account(account_card)
        return account_mask
    else:
        card_mask = get_mask_card_number(account_card)
        return card_mask


def get_data(release_data: str) -> str:
    """Функция возвращает дату выпуска"""
    return f"{release_data[8:10]}.{release_data[5:7]}.{release_data[0:4]}"


if __name__ == '__main__':
    print(get_mask_account_card('Maestro 1596837868705199'))
    print(get_mask_account_card('Visa Classic 6831982476737658'))
    print(get_mask_account_card('Счет 73654108430135874305'))
    print(get_data('2024-03-11T02:26:18.671407'))
