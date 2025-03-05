from src.logger import masks_logger

def get_mask_card_number(card_number: int = 0) -> str:
    """
    принимает на вход номер карты и возвращает ее маску
    в формате: XXX XX** **** XXXX, где X — это цифра номера
    7000792289606361     - входной аргумент
    7000 79** **** 6361  - выход функции
    """

    if card_number == 0:
        masks_logger.error('Номер карты отсутствовал')
        raise ValueError('Номер карты не может отсутствовать')


    card_number_s = str(card_number)

    if len(card_number_s) != 16:
        masks_logger.error('Неверная длина номера карты')
        raise ValueError('Неверная длина номера карты')

    if any(not digit.isdigit() for digit in card_number_s):
        masks_logger.error('Неверный формат номера карты')
        raise ValueError('Неверный формат номера карты')

    masks_logger.info('Маска номера карты успешно получена')
    return f"{card_number_s[:4]} {card_number_s[4:6]}** **** {card_number_s[-4:]}"


def get_mask_account(account_number: int = 0) -> str:
    """
    принимает на вход номер счёта и возвращает его маску
    пример:
    73654108430135874305  # входной аргумент
    **4305  # выход функции
    """

    if account_number == 0:
        masks_logger.error('Номер счёта отсутствовал')
        raise ValueError('Номер счёта не может отсутствовать')

    account_number_s = str(account_number)

    if len(account_number_s) != 20:
        masks_logger.error('Неверная длина номера счёта')
        raise ValueError('Неверная длина номера счёта')

    if any(not digit.isdigit() for digit in account_number_s):
        masks_logger.error('Неверный формат номера счёта')
        raise ValueError('Неверный формат номера счёта')

    masks_logger.info('Маска номера счёта успешно получена')
    return f"**{account_number_s[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874308))
