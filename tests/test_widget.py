import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("number_account, expected",
                         [("Счет 64686473678894779589", "Счет **9589"),
                          ("Счет 79589", "Счет **9589"),
                          ("Счет 6468645665473678894779589", "Счет **9589"),
                          ("Счет ", "Счет "),
                          ("64686473678894779589", "6468 64** **** 9589"),
                          ("", "")
                          ]
                         )
def test_mask_account_card(number_account, expected):
    assert mask_account_card(number_account) == expected


@pytest.mark.parametrize("date_str, expected",
                         [("2024-11-05", "05.11.2024"),
                          ("2024:11:05", "05.11.2024"),
                          ("", "")
                          ]
                         )
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
