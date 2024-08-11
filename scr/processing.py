def filter_by_state(id_list: list, state = 'EXECUTED') -> list | None:
    """Функция возвращает список словарей с соответствующим значением состояния"""
    return [i for i in id_list if i['state'] == state]
