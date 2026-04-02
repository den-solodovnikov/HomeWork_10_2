import json

from src.external_api import currency_conversion


def data_transactions(path_json: str) -> list[dict]:
    """ Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список. """
    try:
        with open(path_json, "r", encoding="utf-8") as file_transactions:
            transactions = json.load(file_transactions)
            if transactions:
                return transactions
            else:
                return []
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []


def amount_transactions(transaction: dict) -> float:
    """ Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
     Усли транзакция в была USD или в EUR, обращается к внешнему API
     для получения текущего курса валют и конвертации суммы операции в рубли."""
    currency_code = transaction['operationAmount']['currency']['code']
    amount = 0
    if currency_code == 'RUB':
        amount = float(transaction['operationAmount']['amount'])
    elif currency_code == 'USD' or currency_code == 'EUR':
        amount = currency_conversion(currency_code, transaction['operationAmount']['amount'])
    return amount

