import re
from collections import Counter


def search_description(transactions: list[dict], descript_word: str) -> list[dict]:
    """ Функция для поиска в списке словарей операций по заданной строке
    возвращает список словарей с операциями, у которых в описании есть строка,
    переданная аргументу функции. """
    transactions_result = []
    pattern = re.compile(descript_word, re.IGNORECASE)
    for transaction in transactions:
        if pattern.search(str(transaction.get('description', ''))):
            transactions_result.append(transaction)
    return transactions_result


def count_transactions(transactions: list[dict], categories: list[str]) -> dict:
    """ Функция для подсчета количества банковских операций определенного типа. """
    result_list = []
    for item in transactions:
        for category in categories:
            if category.lower() in item.get('description', '').lower():
                result_list.append(item.get('description', ''))
    count_dict = dict(Counter(result_list))
    return count_dict
