from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_information: str = '') -> str:
    '''
     принимает строку, содержащую тип и номер карты/счета
     возвращает строку, содержащую тип и номер карты/счета
     с замаскированным номером (тип маскировки для счетов и карт разные)
    '''
    # пустое поле в информации о карте/счёте
    if not account_card_information:
        raise ValueError('Поле с информацией о карте/счёте не может быть пустым')

    words = account_card_information.split()
    is_card = words[0].lower() not in 'счетсчёт'

    # карта с неправильной информацией
    if is_card:
        # ишем номер карты
        card_number = ''
        for word in words:
            if all(i.isdigit() for i in word):
                card_number = word

        # нет поля с одними цифрами вообще или длина такого поля не равна 16
        if not card_number or len(card_number) != 16:
            raise ValueError('Неверный формат номера карты')

    # счёт с неправильным номером
    if not is_card:
        account_number = words[1]  # то, что идёт сразу после слова СЧЁТ

        if len(account_number) != 20 or any(not i.isdigit() for i in account_number):
            raise ValueError('Неверный формат номера счёта')

    for i in range(len(words)):
        if words[i][0].isdigit():
            if is_card:
                words[i] = get_mask_card_number(int(words[i]))
            else:
                words[i] = get_mask_account(int(words[i]))
    return ' '.join(words)


def get_date(date: str = '') -> str:
    """
    Принимает на вход строку с датой в формате: "2024-03-11T02:26:18.671407"
    Возвращает строку с датой в формате: "ДД.ММ.ГГГГ" ("11.03.2024")
    """
    if not date:
        raise ValueError('Поле даты не может быть пустым')

    if len(date) != 26:
        raise ValueError('Неверный формат даты')  # длина входной строки не равна 26 символов - больше или меньше

    if any(not i.isdigit() for i in (date[8: 10], date[5: 7], date[: 4])) or \
            (int(date[8: 10]) not in range(1, 32)) or (int(date[5: 7]) not in range(1, 13)):
        raise ValueError('Неверный формат даты')

    return f'{date[8: 10]}.{date[5: 7]}.{date[: 4]}'


if __name__ == '__main__':
    print(mask_account_card('Visa Classic 6831982476737658'))
    print(get_date('2024-03-11T02:26:18.671407'))
