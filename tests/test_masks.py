import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('card_number, expected', [(7000792289606361, '7000 79** **** 6361'),
                                                   (7000812289607459, '7000 81** **** 7459')])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_empty_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number()


@pytest.mark.parametrize('card_number', [111, 111111111111111111111111111111111111111111111])
def test_get_mask_card_number_wrong_length(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize('account_number, expected', [(73654108430135874305, '**4305'),
                                                      (70008122896074597512, '**7512')])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

def test_get_mask_empty_account():
    with pytest.raises(ValueError):
        get_mask_account()


@pytest.mark.parametrize('account_number', [111, 111111111111111111111111111111111111111111111])
def test_get_mask_account_wrong_length(account_number):
    with pytest.raises(ValueError):
        get_mask_card_number(account_number)
