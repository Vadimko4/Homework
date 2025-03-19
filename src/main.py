from src.utils import get_fin_transactions_from_json, PATH_TO_JSON_FILE
from src.tables import get_transactions_list_from_csv, get_transactions_list_from_xlsx, \
    PATH_TO_TRANSACTIONS_XLSX_FILE, PATH_TO_TRANSACTIONS_CSV_FILE
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.refinder import get_required_operations_list, get_categories_count


def foolproof_user_input(valid_values: list[str]) -> str:
    user_answer = ''
    while user_answer not in valid_values:
        user_answer = input('\nПользователь: ').upper()
        if user_answer not in valid_values:
            print("Программа: неверный ввод, попробуйте ещё раз")
    return user_answer


def main():
    print("""Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
    
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")
    user_answer = foolproof_user_input(['1', '2', '3'])
    user_cases = {'1': 'JSON-файл', '2': 'CSV-файл', '3': 'XLSX-файл'}
    print(f"\nПрограмма: для обработки выбран {user_cases[user_answer]}")
    if user_answer == '1':
        transactions_list = get_fin_transactions_from_json(PATH_TO_JSON_FILE)
    elif user_answer == '2':
        transactions_list = get_transactions_list_from_csv(PATH_TO_TRANSACTIONS_CSV_FILE)
    else:
        transactions_list = get_transactions_list_from_xlsx(PATH_TO_TRANSACTIONS_XLSX_FILE)

    print("""\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING (1/2/3)""")
    user_answer = foolproof_user_input(['1', '2', '3'])
    user_cases = {'1': 'EXECUTED', '2': 'CANCELED', '3': 'PENDING'}
    transactions_list = filter_by_state(transactions_list, user_cases[user_answer])
    print(f'\nПрограмма: Операции отфильтрованы по статусу "{user_cases[user_answer]}"')


    print("\nПрограмма: Отсортировать операции по дате? (Да/Нет)")
    user_answer = foolproof_user_input(['ДА', 'НЕТ'])
    if user_answer == 'ДА':
        print("\nПрограмма: Отсортировать по возрастанию или по убыванию? (1/2)")
        user_answer = foolproof_user_input(['1', '2'])
        if user_answer == '1':
            transactions_list = sort_by_date(transactions_list, False)
        else:
            transactions_list = sort_by_date(transactions_list)

    print("\nПрограмма: Выводить только рублевые тразакции? (Да/Нет)")
    user_answer = foolproof_user_input(['ДА', 'НЕТ'])
    if user_answer == 'ДА':
        transactions_list = [transaction for transaction in filter_by_currency(transactions_list, 'RUB')]

    print("\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? (Да/Нет)")
    user_answer = foolproof_user_input(['ДА', 'НЕТ'])
    if user_answer == 'ДА':
        search_bar = input('\nПрограмма: введите слово для фильтрации: ').lower()
        transactions_list = get_required_operations_list(transactions_list, search_bar)

    print('Программа: Распечатываю итоговый список транзакций...')
    print(*transactions_list, sep='\n')


main()