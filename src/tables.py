import os

import csv

PATH_TO_TRANSACTIONS_CSV_FILE = os.path.join(os.path.dirname(__file__)[:-4], "data", "transactions.csv")


def get_transactions_list_from_csv(csv_file_name: str) -> list[dict]:
    """
    считывает список транзакций из csv файла
    """
    with open(csv_file_name, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        transactions_list = [row for row in reader]

    return transactions_list


if __name__ == '__main__':
    print(PATH_TO_TRANSACTIONS_CSV_FILE)
    print(get_transactions_list_from_csv(PATH_TO_TRANSACTIONS_CSV_FILE)[:5])
