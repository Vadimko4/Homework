from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('account_card_information, expected',
                         [('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                          ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                          ('Счет 73654108430135874305', 'Счет **4305')])
def test_mask_account_card(account_card_information: Any, expected: Any) -> None:
    assert mask_account_card(account_card_information) == expected


def test_mask_empty_account_card() -> None:
    with pytest.raises(ValueError):
        mask_account_card()


@pytest.mark.parametrize('account_card_information', [('Visa Classic 6f31982476737658'),
                                                      ('Maestro 7658'),
                                                      ('Visa Classic 6011111111111111111111111111111131982476737658')])
def test_mask_wrong_card(account_card_information: Any) -> None:
    with pytest.raises(ValueError):
        mask_account_card(account_card_information)


@pytest.mark.parametrize('account_card_information', [('счёт 6f31982476737658'),
                                                      ('счет 7658'),
                                                      ('счет 6011111111111111111111111111111131982476737658')])
def test_mask_wrong_account(account_card_information: Any) -> None:
    with pytest.raises(ValueError):
        mask_account_card(account_card_information)


@pytest.mark.parametrize('date, expected', [('2024-03-11T02:26:18.671407', '11.03.2024'),
                                            ('2025-01-27T05:15:18.604071', '27.01.2025')])
def test_get_date(date: Any, expected: Any) -> None:
    assert get_date(date) == expected


def test_get_empty_date() -> None:
    with pytest.raises(ValueError):
        get_date()


@pytest.mark.parametrize('date', [('11.03.2024'),
                                  ('11111111111111111111111111111111111111111111111111111111111'),
                                  ('-024-0a-1bT02:26:18.671407', '11.03.2024'),
                                  ('2024-23-11T02:26:18.671407', '11.03.2024'),
                                  ('2024-03-32T02:26:18.671407', '11.03.2024')])
def test_get_wrong_date(date: Any) -> None:
    with pytest.raises(ValueError):
        get_date(date)
