from pytest import fixture, raises
from unittest.mock import MagicMock
from line_reader import read_from_file

@fixture
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.read = MagicMock(return_value="Hello line_reader!")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open


def test_return_correct_string(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    rslt = read_from_file("try_line_reader.txt")
    mock_open.assert_called_once_with("try_line_reader.txt")
    assert rslt == "Hello line_reader!"


def test_throw_except_with_bad_file(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        read_from_file("trry_line_reader.txt")
