import pytest

from scr.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "test_card, result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 73654", "None"),
    ],
)
def test_mask_account_card(test_card: str, result: str | None) -> None:
    assert mask_account_card(test_card) == result


@pytest.mark.parametrize(
    "test_date, result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-27T02:54:18.671407", "27.12.2023"),
        ("2024-03-11", "11.03.2024"),
    ],
)
def test_get_date(test_date: str, result: str) -> None:
    assert get_date(test_date) == result
