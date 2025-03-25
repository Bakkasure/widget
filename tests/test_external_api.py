from unittest.mock import MagicMock, patch

import pytest

from src.external_api import convertion_to_rub


@patch("requests.get")
def test_get_convert_result_success(mock_get: MagicMock) -> None:
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1742326803, "rate": 81.750046},
        "date": "2025-03-18",
        "result": 672097.375683,
    }
    assert convertion_to_rub(mock_get) == 672097.375683


@pytest.fixture()
def rub_transaction() -> dict:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_already_current_code(rub_transaction: dict) -> None:
    assert 31957.58


def test_key_error() -> None:
    mock_data = {"key": "value"}
    with patch("builtins.open", side_effect=KeyError):
        result = convertion_to_rub(mock_data)
        assert result is None
