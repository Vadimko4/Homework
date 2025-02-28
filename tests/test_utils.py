from unittest.mock import patch, mock_open
from src.utils import get_fin_transactions_from_json, PATH_TO_FILE


'''@patch('json.load')
def test_get_fin_transactions_from_json(mock_get):
    mock_get.return_value = []
    assert get_fin_transactions_from_json(PATH_TO_FILE) == []
    #mock_get.assert_called_with()'''


@patch('builtins.open', new_callable=mock_open, read_data='[]')
@patch('json.load')
def test_get_fin_transactions_from_json(mock_json_load, mock_open):
    mock_json_load.return_value = []

    result = get_fin_transactions_from_json(PATH_TO_FILE)

    assert result == []
    mock_open.assert_called_once_with(PATH_TO_FILE, encoding='utf-8')
    mock_json_load.assert_called_once()
