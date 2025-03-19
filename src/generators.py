from typing import Any


def filter_by_currency(transactions: list[dict], currency: str = 'USD', records_type: str = 'json') -> Any:
    """
    принимает на вход список словарей, представляющих транзакции
    records_type - определяет тип записей (различаются записи из json файла и csv/xlsx файлов
    возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    в параметре currency
    """

    # убираем транзакции, в которых нет ключей "operationAmount", "currency", "code"
    if records_type == 'json':
        transactions = [i for i in transactions if not i.get("operationAmount") is None and
                    not i.get("operationAmount").get("currency") is None and
                    not i.get("operationAmount").get("currency").get("code") is None]
    else:
        transactions = [i for i in transactions if not i.get("currency_code") is None]

    if not transactions:
        return []

    #  некорректная валюта в списке транзакций
    if records_type == 'json':
        if any(i.get("operationAmount").get("currency").get("code").upper() not in 'USDEURRUBBTC'
               for i in transactions if not i.get("operationAmount") is None):
            raise ValueError('Ошибка в списке транзакций: нет такой валюты!')
    else:
        if any(i.get("currency_code").upper() not in 'USDEURRUBBTC'
               for i in transactions if not i.get("operationAmount") is None):
            raise ValueError('Ошибка в списке транзакций: нет такой валюты!')

    #  некорректная валюта в параметре currency
    if currency.upper() not in 'USDEURRUBBTC':
        raise ValueError('Ошибка запроса: нет такой валюты!')

    if records_type == 'json':
        return filter(lambda x: x.get("operationAmount").get("currency").get("code") == currency.upper(), transactions)
    else:
        return filter(lambda x: x.get("currency_code") == currency.upper(), transactions)


def transaction_descriptions(transactions: list[dict]) -> Any:
    """
    принимает на вход список словарей, представляющих транзакции
    возвращает итератор, содержащий описание каждой операции по очереди
    """

    if len(transactions) == 0:
        raise ValueError('Список транзакций не может быть пустым')

    # убираем транзакции, в которых нет ключа "description"
    transactions = [i for i in transactions if not i.get("description") is None]

    return (item["description"] for item in transactions)


def get_valid_card_number_form(number: int) -> str:
    """
    вспомогательная к функции card_number_generator
    принимает на вход число от 1 до 9999999999999999
    выдает строку из 16 символов вида XXXX XXXX XXXX XXXX
    недостающие цифры заменяет нулями слева
    """
    result_without_spaces = '0' * (16 - len(str(number))) + str(number)
    list_groups_4_digits = []
    for i in range(4):
        list_groups_4_digits.append(result_without_spaces[i * 4: i * 4 + 4])
    result = ' '.join(list_groups_4_digits)
    return result


def card_number_generator(start_value: int = 1, fin_value: int = int('9' * 16)) -> Any:
    """
    выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где
    X — цифра номера карты. Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
    принимает на вход начальное и конечное значения для генерации диапазона номеров
    """

    try:
        if start_value >= fin_value or start_value < 0 or fin_value < 2 \
                or fin_value > 10 ** 16 - 1 or start_value > 10 ** 16 - 1:
            raise ValueError('Ошибка диапазона генерации номеров карт')  # ввели недопустимые числа
    except Exception:
        # ввели не числа
        raise ValueError('Некорректный ввод стартового и финишного значений диапазона номеров карт')

    return (get_valid_card_number_form(number) for number in range(start_value, fin_value + 1))


'''if __name__ == '__main__':
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
        },
        {}]

    tr = filter_by_currency(test_transactions)
    print(next(tr))
    print(next(tr))

    dsc = transaction_descriptions(test_transactions)
    print(next(dsc))
    print(next(dsc))
    print(next(dsc))

    card_number = card_number_generator(1, int('9' * 16))
    for _ in range(10):
        print(next(card_number))'''
