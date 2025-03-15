import json
from typing import Any


def get_operations_list(path: str) -> Any:
    """Функция принимает путь к JSON-файлу и возвращает список словарей транзакций"""
    try:
        with open(path, encoding="UTF-8") as file:
            try:
                operations_list = json.load(file)
                return operations_list
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []
