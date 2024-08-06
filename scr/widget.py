from scr.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_card: str) -> str | None:
    """Функция возвращает тип или счёт и замаскированный номер карты"""
    if "Счет" in user_card:
        return f"{user_card[:-20]}{get_mask_account(user_card[-20:])}"
    else:
        return f"{user_card[:-16]}{get_mask_card_number(user_card[-16:])}"


def get_date(date: str) -> str | None:
    """Функция возвращает строку с датой в новом формате"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
