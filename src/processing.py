def filter_by_state(full_list: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    принимает список всех операций - возвращает только те, у которых статус = state
    """
    return [i for i in full_list if i['state'] == state]


if __name__ == '__main__':
    test_list = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    print(filter_by_state(test_list))
