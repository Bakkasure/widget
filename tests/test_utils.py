import json
from unittest.mock import patch, mock_open

from src.utils import get_operations_list


@patch("builtins.open", new_callable=mock_open, read_data='[{"key": "value"}]')
@patch("json.load", return_value=[{"key": "value"}])
def test_get_operations_valid_file(mock_json_file_load, mock_file_open) -> None:
    assert get_operations_list('test_file.json')
    mock_json_file_load.assert_called_once()


@patch('builtins.open', side_effect=FileNotFoundError)
def test_get_operations_file_nit_found(mock_file_open) -> None:
    assert get_operations_list('test_file.json') == []
    mock_file_open.assert_called_once()


@patch('builtins.open', new_callable=mock_open, read_data='что-то на русском')
@patch('json.load', side_effect=json.JSONDecodeError('Ошибка декодирования файла', 'Неверный формат данных', 0))
def test_get_operation_invalid_data_in_file(mock_json_file_load, mock_file_open) -> None:
    assert get_operations_list('test_file.json') == []
    mock_json_file_load.assert_called_once()
