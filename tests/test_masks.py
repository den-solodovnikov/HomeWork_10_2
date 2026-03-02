import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected",
                         [("7000792289606361", "7000 79** **** 6361"),
                          ("1234123412341234", "1234 12** **** 1234"),
                          ("1234  1234 1234 1234", "1234 12** **** 1234"),
                          ("123412341234123456", "1234 12** **** 3456"),
                          ("123412341234", "1234 12** **** 1234"),
                          ("", "")
                          ])
def test_get_mask_card_number(card_number: str, expected: str):
    assert get_mask_card_number(card_number) == expected

def test_get_mask_card_number_type_error():
    with pytest.raises(TypeError):
        get_mask_card_number("4562kisj.64")

@pytest.mark.parametrize("account_number, expected",
                         [("73654108430135874305", "**4305"),
                          ("1234  1234 1234 1234", "**1234"),
                          ("123412341234123456", "**3456"),
                          ("123", "**123"),
                          ("", "")
                          ])
def test_get_mask_account(account_number: str, expected: str):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_number_type_error():
    with pytest.raises(TypeError):
        get_mask_account("4562kisj.64")