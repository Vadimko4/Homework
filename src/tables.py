import os

import csv
import pandas as pd

PATH_TO_TRANSACTIONS_CSV_FILE = os.path.join(os.path.dirname(__file__)[:-4], "data", "transactions.csv")
PATH_TO_TRANSACTIONS_XLSX_FILE = os.path.join(os.path.dirname(__file__)[:-4], "data", "transactions_excel.xlsx")


def get_transactions_list_from_csv(csv_file_name: str) -> list[dict]:
    """
    считывает список транзакций (словари) из csv файла
    """
    with open(csv_file_name, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        transactions_list = [row for row in reader]

    return transactions_list


def get_transactions_list_from_xlsx(xlsx_file_name: str) -> list[dict]:
    """
    считывает список транзакций (словари) из xlsx файла
    """
    excel_data = pd.read_excel(xlsx_file_name)
    transactions_list = excel_data.to_dict(orient='records')

    return transactions_list


if __name__ == '__main__':
    print(PATH_TO_TRANSACTIONS_CSV_FILE)
    print(get_transactions_list_from_xlsx(PATH_TO_TRANSACTIONS_XLSX_FILE)[:5])
