def filter_by_state(bank_operations: list, state: str) -> list:
    """Функция возвращает список словарей, отсортированных по заданному параметру"""
    filtered_id_state = []
    for operation in bank_operations:
        if operation.get('state') == state:
            filtered_id_state.append(operation)
    if filtered_id_state:
        return filtered_id_state
    else:
        raise KeyError('Словарей для такого статуса нет')
        return []


def sort_by_date(bank_operations: list, reverse: bool = True) -> list:
    """Функция возвращает список словарей, отсортированных по дате"""
    for operation in bank_operations:
        if len(operation["date"]) != 26:
            raise ValueError("Неверный формат даты")
    filtered_id_date = sorted(bank_operations, key=lambda operation: operation["date"], reverse=reverse)
    return filtered_id_date


