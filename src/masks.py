import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8", mode="w")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """ Функция принимает на вход номер карты в виде строки
    и возвращает маску номера по правилу XXXX XX** **** XXXX. """
    logger.info('Проверка на ввод не пустой строки номера карты')
    if card_number == "":
        logger.error(f'Введенна пустая строка номера карты {card_number}')
        return ""
    new_card_number = card_number.replace(" ", "")
    logger.info('Проверка на корректность введенных данных номера карты')
    if not new_card_number.isdigit():
        logger.error(f'Введены данные карты не верного типа: {new_card_number}')
        raise TypeError("Не верный тип номера карты")
    logger.info('Операция маскировки номера карты завершена успешно')
    return (f"{new_card_number[:4]} "
            f"{new_card_number[4:6]}** **** "
            f"{new_card_number[-4:]}")


def get_mask_account(account_number: str) -> str:
    """ Функция принимает на вход номер счета в виде строки
    и возвращает маску номера по правилу **XXXX. """
    logger.info('Проверка на ввод не пустой строки счета')
    if account_number == "":
        logger.error(f'Введенна пустая строка счета {account_number}')
        return ""
    new_account_number = account_number.replace(" ", "")
    logger.info('Проверка на корректность введенных данных номера счета')
    if not new_account_number.isdigit():
        logger.error(f'Введены данные не верного типа счета: {account_number}')
        raise TypeError("Не верный тип номера счета")
    logger.info('Операция маскировки номера счета завершена успешно')
    return f"**{account_number[-4:]}"
