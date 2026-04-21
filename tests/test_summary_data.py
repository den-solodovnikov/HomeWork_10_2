import pytest

from src.summary_data import count_transactions, search_description


@pytest.mark.parametrize('transactions, categories, expected',
                         [
                             ([{'description': 'Перевод с карты на счет'},
                              {'description': 'Перевод с карты на карту'},
                              {'description': 'Перевод с карты на карту'}],
                              ['на карту'], {'Перевод с карты на карту': 2}),
                             ([{'description': 'Перевод с карты на счет'},
                              {'description': 'Перевод с карты на карту'},
                              {'description': 'Перевод с карты на карту'}],
                              ['открытие'], {})
                         ]
                         )
def test_count_transactions(transactions, categories, expected):
    assert count_transactions(transactions, categories) == expected


@pytest.mark.parametrize('transactions, descript_word, expected',
                         [
                             ([{'description': 'Перевод с карты на счет'},
                              {"description": "Открытие вклада"},
                              {"description": "Перевод с карты на карту"}],
                              'перевод', [{'description': 'Перевод с карты на счет'},
                                          {'description': 'Перевод с карты на карту'}]),
                             ([{'description': 'Перевод с карты на счет'},
                              {'description': 'Перевод с карты на карту'},
                              {"description": 'Перевод с карты на карту'}],
                              'открытие', [])
                         ]
                         )
def test_search_description(transactions, descript_word, expected):
    assert search_description(transactions, descript_word) == expected
