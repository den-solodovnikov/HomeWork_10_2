from pprint import pprint

from src.summary_data import search_description
from src.utils import data_transactions
from transactions_from_csv_xls import read_transactions_from_csv, read_transactions_from_xls


def main() -> None:
    """ Функция приветствия интерактивно связывает функциональности между собой. """
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('Выберите необходимый пункт меню:\n'
          '1. Получить информацию о транзакциях из JSON-файла\n'
          '2. Получить информацию о транзакциях из CSV-файла\n'
          '3. Получить информацию о транзакциях из XLSX-файла\n')
    tipe_file = input()
    if tipe_file == '1':
        transactions = data_transactions('data/operations.json')
        print('Для обработки Выбран JSON-файл')
    elif tipe_file == '2':
        transactions = read_transactions_from_csv('data/transactions.csv')
        print('Для обработки выбран CSV-файл')
    elif tipe_file == '3':
        transactions = read_transactions_from_xls('data/transactions_excel.xlsx')
        print('Для обработки выбран EXCEL-файл')
    else:
        return print('Не выбран тип файла транзакций')


    states = ['EXECUTED', 'CANCELED', 'PENDING']
    state_in = ''
    flag = True
    while flag:
        state_in = input('Введите статус, по которому необходимо выполнить фильтрацию.\n'
                   '(доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING):\n')
        for state in states:
            if state_in.lower() in state.lower():
                state_in = state
                flag = False
        if flag:
            print(f'Статус операции {state_in} недоступен')

    transactions_filtered = [transaction for transaction in transactions if transaction.get('state') == state_in]
    print(f'Операции отфильтрованы по статусу: {state_in.upper()}\n')

    if input('Отсортировать операции по дате? Да/Нет\n').lower() == 'да':
        if input('Отсортировать по возрастанию или по убыванию?\n').lower() in 'по убыванию':
            transactions_filtered = sorted(transactions_filtered, key=lambda x: x['date'], reverse=True)
        else:
            transactions_filtered = sorted(transactions_filtered, key=lambda x: x['date'], reverse=False)

    if input('Выводить только рублевые транзакции? Да/Нет\n').lower() == 'да':
        transactions_filtered = [transaction for transaction in transactions
                                 if transaction['operationAmount']['currency'].get('code', '').lower() == 'rub']

    if input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n').lower() == 'да':
        descript_word = input('Введите слово для фильтрации по описанию: \n')
        transactions_result = search_description(transactions_filtered, descript_word)
    else:
        transactions_result = transactions_filtered
    print('Распечатываю итоговый список транзакций...\n')
    if transactions_result:
        print(f'Всего банковских операций в выборке: {len(transactions_result)}\n')
        pprint(transactions_result)
        return None
    else:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
        return None


if __name__ == "__main__":
    main()