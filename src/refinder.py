import re
from collections import Counter


def get_required_operations_list(operations: list[dict], search_bar: str) -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка
    """
    # убираем транзакции, в которых нет ключа "description"
    operations = [i for i in operations if not i.get('description') is None]

    pattern = fr'{search_bar}'
    return [i for i in operations if re.search(pattern, i.get("description").lower())]


def get_categories_count(operations: list[dict], categories_list: list[str]) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций,
    dозвращает словарь, в котором ключи — названия категорий, значения — количество операций
    в каждой категории
    """
    # оставляем только те операции, у которых описание в "description" содержится в categories_list
    operations = [i.get("description") for i in operations if i.get("description") in categories_list]

    return Counter(operations)
