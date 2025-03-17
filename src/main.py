def foolproof_user_input(valid_values: list[str]) -> str:
    user_answer = ''
    while user_answer not in valid_values:
        user_answer = input('\nПользователь: ').upper()
        if user_answer not in valid_values:
            print("Программа: неверный ввод, попробуйте ещё раз")
    return user_answer


print("""Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями. 

Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")
user_answer = foolproof_user_input(['1', '2', '3'])
user_cases = {'1': 'JSON-файл', '2': 'CSV-файл', '3': 'XLSX-файл'}
print(f"\nПрограмма: для обработки выбран {user_cases[user_answer]}")

print("""\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING (1/2/3)""")
user_answer = foolproof_user_input(['1', '2', '3'])
user_cases = {'1': 'EXECUTED', '2': 'CANCELED', '3': 'PENDING'}
print(f'\nПрограмма: Операции отфильтрованы по статусу "{user_answer}"')

print("\nПрограмма: Отсортировать операции по дате? (Да/Нет)")
user_answer = foolproof_user_input(['ДА', 'НЕТ'])

print("\nПрограмма: Отсортировать по возрастанию или по убыванию? (1/2)")
user_answer = foolproof_user_input(['1', '2'])

print("\nПрограмма: Выводить только рублевые тразакции? (Да/Нет)")
user_answer = foolproof_user_input(['ДА', 'НЕТ'])

print("\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? (Да/Нет)")
user_answer = foolproof_user_input(['ДА', 'НЕТ'])

print('Программа: Распечатываю итоговый список транзакций...')
