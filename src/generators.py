def filter_by_currency(transactions: list[dict], currency: str = 'USD'):
    """
        принимает на вход список словарей, представляющих транзакции
        возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
        в параметре currency
        """
    if len(transactions) == 0:
        raise ValueError('Список транзакций не может быть пустым')

    if any(i["operationAmount"]["currency"]["code"].upper() not in 'USDEURRUB' for i in transactions):
        raise ValueError('Ошибка в списке транзакций: нет такой валюты!')

    if currency.upper() not in 'USDEURRUB':
        raise ValueError('Ошибка запроса: нет такой валюты!')

    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency.upper(), transactions)


test_transactions = [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
        {
            "id": 112765260,
            "state": "EXECUTED",
            "date": "2020-05-05T23:23:12.206578",
            "operationAmount": {
                "amount": "19054.12",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227159521",
            "to": "Счет 75651667383060284188"
        }]

if __name__ == '__main__':
    tr = filter_by_currency(test_transactions)
    print(next(tr))
    print(next(tr))
    filter_by_currency([{
            "id": 112765260,
            "state": "EXECUTED",
            "date": "2020-05-05T23:23:12.206578",
            "operationAmount": {
                "amount": "19054.12",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227159521",
            "to": "Счет 75651667383060284188"
        }], 'EEE')
