from unittest.mock import mock_open, patch

from src.utils import get_operations_list


def test_file_not_found() -> None:
    """Функция возвращает пустой список при отсутствии файла"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = get_operations_list("test.json")
        assert result == []


def test_decode_error() -> None:
    """Функция возвращает пустой список при ошибке чтения файла"""
    mock_data = "[{'key':'value'},"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = get_operations_list("test.json")
        assert result == []


def test_get_operations_list_success() -> None:
    """Функция проверяет корректность возвращаемых данных"""
    mock_data = '[{"key":"value"}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = get_operations_list("test.json")
        assert result == [{"key": "value"}]
