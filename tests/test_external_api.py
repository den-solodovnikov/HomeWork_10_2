from unittest.mock import Mock, patch

from src.external_api import currency_conversion


@patch('requests.get')
def test_currency_conversion_pass(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'success': True, 'result': 7788.7788}
    mock_get.return_value = mock_response
    assert currency_conversion('USD', 8) == 7788.7788
    mock_get.assert_called_once()

@patch('requests.get')
def test_currency_conversion_filed(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {0}
    mock_get.return_value = mock_response
    assert currency_conversion('USD', 8) == 0
    mock_get.assert_called_once()
