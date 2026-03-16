def get_mask_card_number(card_number: str) -> str:
    """ Функция принимает на вход номер карты в виде строки
    и возвращает маску номера по правилу XXXX XX** **** XXXX . """
    if card_number == "":
        return ""
    new_card_number = card_number.replace(" ", "")
    if not new_card_number.isdigit():
        raise TypeError("Не верный тип номера карты")
    return f"{new_card_number[:4]} {new_card_number[4:6]}** **** {new_card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """ Функция принимает на вход номер счета в виде строки
    и возвращает маску номера по правилу **XXXX . """
    if account_number == "":
        return ""
    new_account_number = account_number.replace(" ", "")
    if not new_account_number.isdigit():
        raise TypeError("Не верный тип номера счета")
    return f"**{account_number[-4:]}"