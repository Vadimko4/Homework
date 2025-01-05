from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_information: str) -> str:
    '''
     принимает строку, содержащую тип и номер карты/счета
     возвращает строку, содержащую тип и номер карты/счета
     с замаскированным номером (тип маскировки для счетов и карт разные)
    '''
    words = account_card_information.split()
    is_card = words[0].lower() != 'счет'
    for i in range(len(words)):
        if words[i][0].isdigit():
            if is_card:
                words[i] = get_mask_card_number(int(words[i]))
            else:
                words[i] = get_mask_account(int(words[i]))
    return ' '.join(words)


def get_date(date: str) -> str:
    '''
    принимает на вход строку с датой в формате: "2024-03-11T02:26:18.671407"
    возвращает строку с датой в формате: "ДД.ММ.ГГГГ" ("11.03.2024")
    '''
    return f'{date[8: 10]}.{date[5: 7]}.{date[: 4]}'


if __name__ == '__main__':
    print(mask_account_card('Visa Classic 6831982476737658'))
    print(get_date('2024-03-11T02:26:18.671407'))
