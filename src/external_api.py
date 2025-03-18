import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("API_KEY")


def convertion_to_rub(operation_info: dict) -> float | Any | None:
    """Функция конвертирует валюту и возвращает сумму в рублях"""
    try:
        if operation_info["operationAmount"]["currency"]["name"] != "руб.":
            value_from = operation_info["operationAmount"]["currency"]["name"]
            amount = operation_info["operationAmount"]["amount"]
            param = {"from": value_from, "to": "RUB", "amount": amount}
            header = {"apikey": token}
            url = "https://api.apilayer.com/exchangerates_data/convert"

            response = requests.get(url, headers=header, params=param)
            amount_rub = response.json()
            return amount_rub.get("result")
        else:
            return operation_info["operationAmount"]["amount"]
    except KeyError:
        print("Указанный ключ не найден")
        return None
