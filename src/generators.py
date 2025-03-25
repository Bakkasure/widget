from typing import Generator, Union


def filter_by_currency(transaction_list: list[dict], currency: str) -> Generator[Union[dict, str], None, None]:
    """Функция возвращает итератор, который поочередно выдает транзакции с указанной валютой"""
    if transaction_list:
        for transaction in transaction_list:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


def transaction_descriptions(transaction_list: list[dict]) -> Generator[str, None, None]:
    if transaction_list:
        for transaction in transaction_list:
            yield transaction["description"]
    else:
        print("Список пуст!")


def card_number_generator(first: int, last: int) -> Generator[str, None, None]:
    """Функция генерирует номера карт в заданном диапазоне"""
    for number in range(first, last + 1):
        number_str = f"{number:016}"
        formatted_number = f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
        yield formatted_number
