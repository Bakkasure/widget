import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("API_KEY")


def convertion_to_rub(operation_info: dict) -> float | Any | None:
    """Функция конвертирует валюту и возвращает сумму в рублях"""
    try:
        try:
            if operation_info["operationAmount"]["currency"]["name"] != "руб.":
                value_from = operation_info["operationAmount"]["currency"]["name"]
                amount = operation_info["operationAmount"]["amount"]

                header = {
                    "apikey": token,
                }
                url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={value_from}&amount={amount}"

                response = requests.get(url, headers=header)
                amount_rub = response.json()
                return amount_rub["result"]
            else:
                return operation_info["operationAmount"]["amount"]
        except KeyError:
            print("Указанный ключ не найден")
            return None
    except TypeError:
        print("Аргумент функции должен быть словарём")
        return None
