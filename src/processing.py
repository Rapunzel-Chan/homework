def filter_by_state(bank_operations: list, state: str = 'EXECUTED') -> list:
    """Функция возвращает список словарей, отфильтрованных по заданному параметру"""
    filtered_id_state = []
    for operation in bank_operations:
        if operation['state'] == state:
            filtered_id_state.append(operation)
    return filtered_id_state


def sort_by_date(bank_operations: list, reverse: bool = True) -> list:
    """Функция возвращает список словарей, отфильтрованных по дате"""
    filtered_id_date = sorted(bank_operations, key=lambda operation: operation["date"], reverse=reverse)
    return filtered_id_date


if __name__ == '__main__':
    operation_state_ex = filter_by_state(
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
    operation_state_can = filter_by_state(
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
        state='CANCELED')
    print(operation_state_ex)
    print(operation_state_can)

    print(sort_by_date(
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                       reverse=False))
