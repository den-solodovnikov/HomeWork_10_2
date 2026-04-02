import os

import requests
from dotenv import load_dotenv


def currency_conversion(currency_code: str, amount: float) -> float:
    """ Функция обращается к внешнему API для получения текущего курса валют
    и конвертирует суммы операции в рубли. """
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    headers = {"apikey": f'{API_KEY}'}
    params = {
        "to": "RUB",
        "from": f'{currency_code}',
        "amount": f'{amount}'
    }
    url = 'https://api.apilayer.com/exchangerates_data/convert'
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()['result']
    else:
        return 0
