def filter_by_state(id_list: list, state: str = "EXECUTED") -> list | None:
    """Функция возвращает список словарей с соответствующим значением состояния"""
    return [i for i in id_list if i["state"] == state]


def sort_by_date(id_list: list, ascending: bool = True) -> list | None:
    """Функция сортирует список по дате"""
    sorted_list = sorted(id_list, key=lambda id_operation: id_operation.get("date", 0), reverse=ascending)
    return sorted_list
