import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
api_key = os.getenv('API_KEY')


def get_transaction_amount(transaction: dict) -> float:
    """
    Функция возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли
    """
    if (
            ("operationAmount" not in transaction)
            or ("amount" not in transaction["operationAmount"])
            or ("currency" not in transaction["operationAmount"])
            or ("code" not in transaction["operationAmount"]["currency"])
            or (any(not i.isdigit() for i in str(transaction["operationAmount"]["amount"]) if i != '.'))
            or (float(transaction["operationAmount"]["amount"]) < 0)
    ):
        raise ValueError('Неверные данные о транзакции')

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        result_amount = transaction["operationAmount"]["amount"]
    elif transaction["operationAmount"]["currency"]["code"] in ("USD", "EUR"):
        url = "https://api.apilayer.com/exchangerates_data/convert"
        headers = {
            "apikey": api_key
        }
        payload = {
            "amount": transaction["operationAmount"]["amount"],
            "from": transaction["operationAmount"]["currency"]["code"],
            "to": "RUB"
        }
        response = requests.get(url, headers=headers, params=payload)
        result_amount = response.json()["result"]
        # status_code = response.status_code
    else:
        raise ValueError('Такая валюта не предусмотрена')

    return float(result_amount)


if __name__ == '__main__':
    print(get_transaction_amount({
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "100.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        }
    }))
