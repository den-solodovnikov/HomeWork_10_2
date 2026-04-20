from pprint import pprint

from src.summary_data import count_transactions, search_description
from src.utils import data_transactions


if __name__ == "__main__":
    operation = input('Введите операцию для поиска транзакций: ')
    transactions = data_transactions('data/operations.json')
    pprint(search_description(transactions, operation))
    category = (input('Введите через запятую категории операций для поиска транзакций: ')).split(',')
    print(count_transactions(transactions, category))
