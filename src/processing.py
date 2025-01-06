def filter_by_state(operations: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    принимает список всех операций - возвращает только те, у которых статус = state
    """
    return [i for i in operations if i['state'] == state]


def sort_by_date(operations: list[dict], decreasing: bool = True) -> list[dict]:
    """
    принимает список всех операций - новый список, отсортированный по дате (date)
    если decreasing = True (значение по умолчанию) - сортирует по убыванию,
    иначе по возрастанию
    """
    sorted_operations = sorted(operations, key=lambda x: x['date'], reverse=decreasing)
    return sorted_operations


if __name__ == '__main__':
    test_list = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    print(filter_by_state(test_list))
    print(sort_by_date(test_list))
