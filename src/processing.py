def filter_by_state(operations: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Принимает список всех операций - возвращает только те, у которых статус = state
    """
    if all(operation['state'] != state for operation in operations):
        raise ValueError('Нет операций с таким статусом')

    return [i for i in operations if i['state'] == state]


def sort_by_date(operations: list[dict], decreasing: bool = True) -> list[dict]:
    """
    Принимает список всех операций - новый список, отсортированный по дате (date).
    Если decreasing = True (значение по умолчанию) - сортирует по убыванию,
    иначе по возрастанию
    """
    if any((len(operation['date']) != 26 or
            not (operation['date'])[:4].isdigit() or
            not (operation['date'])[5:7].isdigit() or
            not (operation['date'])[8:10].isdigit())
           for operation in operations):
        raise ValueError('Неверный формат даты')

    if any(int(operation['date'][5:7]) not in range(1, 13) or int(operation['date'][8:10]) not in range(1, 32)
           for operation in operations):
        raise ValueError('Неверный формат даты')

    sorted_operations = sorted(operations, key=lambda x: (x['date'], x['id']), reverse=decreasing)
    return sorted_operations


if __name__ == '__main__':
    test_list = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 615064592, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    print(filter_by_state(test_list))
    print(sort_by_date(test_list, True))
