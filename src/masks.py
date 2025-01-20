def get_mask_card_number(card_number: int = None) -> str:
    """
    принимает на вход номер карты и возвращает ее маску
    в формате: XXX XX** **** XXXX, где X — это цифра номера
    7000792289606361     - входной аргумент
    7000 79** **** 6361  - выход функции
    """

    if card_number == None:
        raise ValueError('Номер карты не может отсутствовать')

    card_number_s = str(card_number)

    if len(card_number_s) != 16:
        raise ValueError('Неверная длина номера карты')

    if any(not digit.isdigit() for digit in card_number_s):
        raise ValueError('Неверный формат номера карты')

    return f"{card_number_s[:4]} {card_number_s[4:6]}** **** {card_number_s[-4:]}"


def get_mask_account(account_number: int = None) -> str:
    """
    принимает на вход номер счёта и возвращает его маску
    пример:
    73654108430135874305  # входной аргумент
    **4305  # выход функции
    """

    if account_number == None:
        raise ValueError('Номер счёта не может отсутствовать')

    account_number_s = str(account_number)

    if len(account_number_s) != 20:
        raise ValueError('Неверная длина номера карты')

    if any(not digit.isdigit() for digit in account_number_s):
        raise ValueError('Неверный формат номера карты')

    return f"**{account_number_s[-4:]}"
