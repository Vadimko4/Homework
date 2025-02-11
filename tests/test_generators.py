from typing import Any

import pytest

from src.generators import filter_by_currency


def test_filter_by_currency_USD(test_transaction_list: Any) -> None:
    assert list(filter_by_currency(test_transaction_list, 'USD')) == \
           [{
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
               }]


def test_filter_by_currency_EUR(test_transaction_list: Any) -> None:
    assert list(filter_by_currency(test_transaction_list, 'EUR')) == \
           [{
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

def test_filter_by_currency_with_empty_list() -> None:
    with pytest.raises(ValueError):
        filter_by_currency([])


def test_filter_by_currency_with_wrong_currency_in_list() -> None:
    with pytest.raises(ValueError):
        filter_by_currency([{"operationAmount": {"currency": {"name": "EUR", "code": "EEE"}}}])


def test_filter_by_currency_with_wrong_currency_request() -> None:
    with pytest.raises(ValueError):
        filter_by_currency([{"operationAmount": {"currency": {"name": "EUR", "code": "EUR"}}}], "EEE")
