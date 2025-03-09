from unittest.mock import mock_open, patch

from src.tables import PATH_TO_TRANSACTIONS_CSV_FILE, PATH_TO_TRANSACTIONS_XLSX_FILE, \
    get_transactions_list_from_csv, get_transactions_list_from_xlsx


@patch('builtins.open', new_callable=mock_open, read_data='[]')
@patch('csv.DictReader')
def test_get_transactions_list_from_csv(mock_csv_DictReader, mock_open):
    mock_csv_DictReader.return_value = []

    result = get_transactions_list_from_csv(PATH_TO_TRANSACTIONS_CSV_FILE)

    assert result == []
    mock_open.assert_called_once_with(PATH_TO_TRANSACTIONS_CSV_FILE, encoding='utf-8')
    mock_csv_DictReader.assert_called_once()


@patch('pandas.read_excel')
def test_get_transactions_list_from_xlsx(mock_get):
    mock_get.return_value.to_dict.return_value = []
    assert get_transactions_list_from_xlsx(PATH_TO_TRANSACTIONS_XLSX_FILE) == []
    mock_get.assert_called_with(PATH_TO_TRANSACTIONS_XLSX_FILE)
