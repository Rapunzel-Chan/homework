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
    day = release_data[8:10]
    month = release_data[5:7]
    year = release_data[0:4]
    if day.isdigit() and month.isdigit() and year.isdigit():
        if 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 1900 <= int(year) <= 2025:
            return f"{release_data[8:10]}.{release_data[5:7]}.{release_data[0:4]}"
        else:
            raise ValueError("Неверная дата")
