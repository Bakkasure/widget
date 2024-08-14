def filter_by_state(id_list: list, state: str = "EXECUTED") -> list | None:
    """Функция возвращает список словарей с соответствующим значением состояния"""
    if len(id_list) > 0:
        return [i for i in id_list if i.get("state") == state]
    else:
        return None


def sort_by_date(id_list: list, ascending: bool = True) -> list | None:
    """Функция сортирует список по дате"""
    if len(id_list) > 0:
        sorted_list = sorted(id_list, key=lambda id_operation: id_operation.get("date", 0), reverse=ascending)
        return sorted_list
    else:
        return None
