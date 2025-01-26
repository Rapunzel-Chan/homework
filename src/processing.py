def filter_by_state(bank_operations: list, state: str) -> list:
    """Функция возвращает список словарей, отсортированных по заданному параметру"""
    filtered_id_state = []
    for operation in bank_operations:
        if operation['state'] == state:
            filtered_id_state.append(operation)
    if filtered_id_state != []:
        return filtered_id_state
    else:
        raise KeyError('Словарей для такого статуса нет')


def sort_by_date(bank_operations: list, reverse: bool = True) -> list:
    """Функция возвращает список словарей, отсортированных по дате"""
    filtered_id_date = sorted(bank_operations, key=lambda operation: operation["date"], reverse=reverse)
    for d_operation in bank_operations:
        date_length = d_operation['date']
        if len(date_length) == 26:
            continue
        else:
            raise ValueError("Неверный формат даты")
    return filtered_id_date
