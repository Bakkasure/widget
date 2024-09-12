from typing import Generator, Union


def filter_by_currency(transaction_list: list[dict], currency: str) -> Generator[Union[dict, str], None, None]:
    """Функция возвращает итератор, который поочередно выдает транзакции с указанной валютой"""
    if transaction_list:
        for transaction in transaction_list:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
    else:
        raise Exception("Транзакций с указанной валютой нет")
