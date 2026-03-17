from datetime import datetime


def filter_by_state(list_dict: list[dict], state: str = 'EXECUTED') \
        -> list[dict]:
    """ Функция возвращает новый список словарей,
    у которых ключ 'state' соответствует укзанному значению.
    """
    list_filtered_by_sort: list[dict] = []
    for item in list_dict:
        if item['state'] == state:
            list_filtered_by_sort.append(item)
    return list_filtered_by_sort


def sort_by_date(list_dict: list[dict], revers_order: bool = True) -> list[dict]:
    """ Функция возвращает отсортированный список словарей по дате. """
    list_sort_by_date: list[dict] = []
    for item in list_dict:
        if revers_order:
            list_sort_by_date = sorted(list_dict,
                                       key=lambda d: datetime.strptime(d['date'],
                                                                       '%Y-%m-%dT%H:%M:%S.%f'),
                                       reverse=True)
        else:
            list_sort_by_date = sorted(list_dict,
                                       key=lambda d: datetime.strptime(d['date'],
                                                                       '%Y-%m-%dT%H:%M:%S.%f'))
    return list_sort_by_date
