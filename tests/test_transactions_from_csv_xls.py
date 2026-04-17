from unittest.mock import patch

import pandas as pd
import pytest

from src.transactions_from_csv_xls import (read_transactions_from_csv,
                                           read_transactions_from_xls)
from tests.conftest import PATH_TO_FILE


@patch('pandas.read_csv')
def test_read_transactions_from_csv(mock_read_csv):
    mock_df = pd.DataFrame({
        'amount': [23423.0],
        'currency_code': ['PHP'],
        'currency_name': ['Peso'],
        'date': ['2022-03-23T08:29:37Z'],
        'description': ['Перевод с карты на карту'],
        'from': ['Discover 7269000803370165'],
        'id': [4699552.0],
        'state': ['EXECUTED'],
        'to': ['American Express 1963030970727681']
    })
    mock_read_csv.return_value = mock_df
    result = read_transactions_from_csv(PATH_TO_FILE)
    expected_result = [{
        'amount': 23423.0,
        'currency_code': 'PHP',
        'currency_name': 'Peso',
        'date': '2022-03-23T08:29:37Z',
        'description': 'Перевод с карты на карту',
        'from': 'Discover 7269000803370165',
        'id': 4699552.0,
        'state': 'EXECUTED',
        'to': 'American Express 1963030970727681'
    }]
    assert result == expected_result


@patch('pandas.read_excel')
def test_read_transactions_from_xls(mock_read_excel):
    mock_df = pd.DataFrame({
        'amount': [23423.0],
        'currency_code': ['PHP'],
        'currency_name': ['Peso'],
        'date': ['2022-03-23T08:29:37Z'],
        'description': ['Перевод с карты на карту'],
        'from': ['Discover 7269000803370165'],
        'id': [4699552.0],
        'state': ['EXECUTED'],
        'to': ['American Express 1963030970727681']
    })
    mock_read_excel.return_value = mock_df
    result = read_transactions_from_xls(PATH_TO_FILE)
    expected_result = [{
        'amount': 23423.0,
        'currency_code': 'PHP',
        'currency_name': 'Peso',
        'date': '2022-03-23T08:29:37Z',
        'description': 'Перевод с карты на карту',
        'from': 'Discover 7269000803370165',
        'id': 4699552.0,
        'state': 'EXECUTED',
        'to': 'American Express 1963030970727681'
    }]
    assert result == expected_result


def test_read_transactions_from_xls_error():
    with pytest.raises(FileNotFoundError):
        read_transactions_from_xls('000')


def test_read_transactions_from_csv_error():
    with pytest.raises(FileNotFoundError):
        read_transactions_from_xls('000')
