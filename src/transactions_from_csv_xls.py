from pathlib import Path
import pandas as pd



def read_transactions_from_csv(path_name: str) -> list[dict]:
    """ Функция принимает путь к файлу CSV и выдает список словарей с транзакциями. """
    path_name = Path(path_name)

    if not path_name.exists():
        raise FileNotFoundError(path_name.name)

    try:
        df_csv = pd.read_csv(path_name)
        transactions_list = df_csv.to_dict(orient='records')
    except ValueError as e:
        raise e
    return transactions_list


def read_transactions_from_xls(path_name: str) -> list[dict]:
    """ Функция принимает путь к файлу XLS и выдает список словарей с транзакциями. """
    path_name = Path(path_name)

    if not path_name.exists():
        raise FileNotFoundError(path_name.name)

    try:
        df_xls = pd.read_excel(path_name)
        transactions_list = df_xls.to_dict(orient='records')
    except ValueError as e:
        raise e
    return transactions_list
