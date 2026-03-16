import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


@pytest.mark.parametrize("currency_code, expected_count", [
    ("USD", 3),  # Три транзакции в USD
    ("RUB", 2),  # Две транзакции в RUB
    ("EUR", 0),  # Нет транзакций в EUR
])
def test_filter_by_currency(transactions_, currency_code, expected_count):
    result = list(filter_by_currency(transactions_, currency_code))
    assert len(result) == expected_count

    result = list(filter_by_currency([], currency_code))  # Пустой список транзакций
    assert len(result) == 0


@pytest.mark.parametrize("transactions_, expected_descriptions", [
    ([  # Список транзакций
        {'description': 'Перевод организации'},
        {'description': 'Перевод со счета на счет'},
        {'description': 'Перевод со счета на счет'},
        {'description': 'Перевод с карты на карту'},
        {'description': 'Перевод организации'}
    ],
     [
        "Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет",
        "Перевод с карты на карту", "Перевод организации"
     ]
    ),
    ([], [])  # Пустой список транзакций
])
def test_transaction_descriptions(transactions_, expected_descriptions):
    result = list(transaction_descriptions(transactions_))
    assert result == expected_descriptions


@pytest.mark.parametrize("start, stop, expected",
                         [(1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
                          (5, 6, ["0000 0000 0000 0005", "0000 0000 0000 0006"]),
                          (8, 8, ["0000 0000 0000 0008"])
                          ]
                         )
def test_card_number_generator(start: int, stop: int, expected: str):
    assert list(card_number_generator(start, stop)) == expected
