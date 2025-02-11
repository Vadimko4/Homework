def filter_by_currency(transactions: list[dict], currency: str = 'USD'):
    """
        принимает на вход список словарей, представляющих транзакции
        возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
        в параметре currency
        """
    return filter(lambda x: x['currency'] == currency, transactions)
