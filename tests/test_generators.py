from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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
            "to": "Счет 75651667383060284188"}]


def test_filter_by_currency_RUB(test_transaction_list: Any) -> None:
    assert list(filter_by_currency(test_transaction_list, 'RUB')) == \
           [{
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"},
               {
                   "id": 594226727,
                   "state": "CANCELED",
                   "date": "2018-09-12T21:27:25.241689",
                   "operationAmount": {
                       "amount": "67314.70",
                       "currency": {
                           "name": "руб.",
                           "code": "RUB"
                       }
                   },
                   "description": "Перевод организации",
                   "from": "Visa Platinum 1246377376343588",
                   "to": "Счет 14211924144426031657"
               }]


def test_filter_by_currency_xls(test_transaction_list_xls):
    assert [i for i in filter_by_currency(test_transaction_list_xls, "RUB", 'xls')] == [
        {
            'id': '651026',
            'state': 'EXECUTED',
            'date': '2021-07-10T20:52:54Z',
            'Amount': '27596',
            'currency_name': 'Ruble',
            'currency_code': 'RUB',
            'from': '',
            'to': 'Счет 41878599375303475996',
            'description': 'Открытие вклада'
        },
        {
            'id': '4653425',
            'state': 'EXECUTED',
            'date': '2020-03-10T07:48:21Z',
            'Amount': '22131',
            'currency_name': 'Ruble',
            'currency_code': 'RUB',
            'from': '',
            'to': 'Счет 58936710508356884628',
            'description': 'Открытие вклада'
        }
    ]


def test_filter_by_currency_xls_with_empty_dict_in_list():
    assert ([i for i in filter_by_currency(
        [
            {
                "operationAmount":
                    {"currency":
                        {"code": "RUB"}
                     }
            },
            {}
        ],
        "RUB", "json")] ==
            [
                {
                    "operationAmount":
                        {"currency": {"code": "RUB"}
                         }
                }
            ])
    assert (([i for i in filter_by_currency([{"currency_code": "RUB"}, {}], "RUB", "xls")]) ==
            [{"currency_code": "RUB"}])


def test_filter_by_currency_with_wrong_currency_in_list() -> None:
    with pytest.raises(ValueError):
        filter_by_currency([{"operationAmount": {"currency": {"name": "EUR", "code": "EEE"}}}])


def test_filter_by_currency_with_wrong_currency_request() -> None:
    with pytest.raises(ValueError):
        filter_by_currency([{"operationAmount": {"currency": {"name": "EUR", "code": "EUR"}}}], "EEE")


def test_transaction_descriptions(test_transaction_list: Any) -> None:
    assert list(transaction_descriptions(test_transaction_list)) == \
           ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет",
            "Перевод со счета на счет", "Перевод организации"]


def test_transaction_descriptions_with_empty_list() -> None:
    with pytest.raises(ValueError):
        transaction_descriptions([])


@pytest.mark.parametrize('start_number, fin_number, expected', [(1, 6,
                                                                 ['0000 0000 0000 0001', '0000 0000 0000 0002',
                                                                  '0000 0000 0000 0003', '0000 0000 0000 0004',
                                                                  '0000 0000 0000 0005', '0000 0000 0000 0006']),
                                                                (4, 7,
                                                                 ['0000 0000 0000 0004', '0000 0000 0000 0005',
                                                                  '0000 0000 0000 0006', '0000 0000 0000 0007'])
                                                                ])
def test_card_number_generator(start_number: int, fin_number: int, expected: Any) -> Any:
    assert list(card_number_generator(start_number, fin_number)) == expected


@pytest.mark.parametrize('start_number, fin_number', [(100, 1), (100, 100), (-32, 32), (10 ** 20, 1), (100, 10 ** 20)])
def test_card_number_generator_with_wrong_values(start_number: int, fin_number: int) -> None:
    with pytest.raises(ValueError):
        card_number_generator(start_number, fin_number)


@pytest.mark.parametrize('start_number, fin_number', [('1a00', 1), (100, '100')])
def test_card_number_generator_with_wrong_input(start_number: Any, fin_number: Any) -> None:
    with pytest.raises(ValueError):
        card_number_generator(start_number, fin_number)
