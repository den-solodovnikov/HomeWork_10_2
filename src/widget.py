import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_account: str) -> str:
    """ Функция принимает строку тип и номер карты или счета,
    возвращает строку с замаскированным номером.
    """
    new_number_account = ''.join(re.findall('[0-9]', number_account, re.M))
    if 'Счет' in number_account:
        number_account_masked = (
                number_account.replace(new_number_account, "") +
                get_mask_account(new_number_account)
                                 )
    else:
        number_account_masked = (
                number_account.replace(new_number_account, "")
                + get_mask_card_number(new_number_account)
        )
    return number_account_masked


def get_date(date_str: str) -> str:
    """ Возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    # new_date = '.'.join(reversed(date_str[0:10].split('-')))
    new_date = re.sub(r"(\d+).(\d+).(\d+)",r"\3.\2.\1", date_str)
    return new_date