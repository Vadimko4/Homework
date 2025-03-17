import json
import os

from src.logger import utils_logger

PATH_TO_JSON_FILE = os.path.join(os.path.dirname(__file__)[:-4], "data", "operations.json")


def get_fin_transactions_from_json(file_name: str = '') -> list[dict]:
    """
    Функция принимает на вход путь до JSON-файла,
    возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_name, encoding='utf-8') as f:
            fin_transactions = json.load(f)
        utils_logger.info('Успешное чтение из файла')

    except Exception as e:
        fin_transactions = []
        utils_logger.error(f'Произошла ошибка: {e}', exc_info=True)

    if not fin_transactions:
        utils_logger.warning('Список транзакций пуст')
    return fin_transactions


if __name__ == '__main__':
    print(get_fin_transactions_from_json(PATH_TO_JSON_FILE)[0]['state'])
