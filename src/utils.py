import json
import logging

from src.external_api import currency_conversion


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8", mode="w")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def data_transactions(path_json: str) -> list[dict]:
    """ Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список. """
    try:
        logger.info(f'Выполняется попытка открытия JSON-файла: {path_json}')
        with open(path_json, "r", encoding="utf-8") as file_transactions:
            transactions = json.load(file_transactions)
            logger.info(f'Файл: {path_json} успешно открыт')
            if transactions:
                logger.info('Операция считывания данных завершена успешно')
                return transactions
            else:
                logger.error(f'Файл {path_json} не содержит данных')
                return []
    except FileNotFoundError as ex:
        logger.error(f'Ошибка открытия файла {path_json}: {ex}')
        return []
    except json.decoder.JSONDecodeError as ex:
        logger.error(f'Ошибка декодировки файла {path_json}: {ex}')
        return []


def amount_transactions(transaction: dict) -> float:
    """ Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
     Если транзакция была в USD или в EUR, обращается к внешнему API
     для получения текущего курса валют и конвертации суммы операции в рубли. """
    currency_code = transaction['operationAmount']['currency']['code']
    amount = 0
    if currency_code == 'RUB':
        logger.info('Сумма получена успешно, транзакция в RUB')
        amount = float(transaction['operationAmount']['amount'])
    elif currency_code == 'USD' or currency_code == 'EUR':
        logger.info('Сумма получена успешно конвертацией в RUB')
        amount = currency_conversion(currency_code, transaction['operationAmount']['amount'])
    return amount
