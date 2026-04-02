from unittest.mock import patch

from src.utils import amount_transactions, data_transactions


def test_data_transactions_FileNotFound():
    assert data_transactions("23.64") == []


def test_amount_transactions_rub(transaction_rub):
    assert amount_transactions(transaction_rub) == 31957.58


@patch('src.utils.currency_conversion')
def test_amount_transactions_eur_usd(mock_conversion, transaction_usd):
    mock_conversion.return_value = 28555.55
    assert amount_transactions(transaction_usd) == 28555.55
    mock_conversion.assert_called_once()


