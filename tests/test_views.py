from unittest.mock import patch

from src.views import currency_rate, price_stocks


@patch("requests.get")
def test_currency_rate(mock_get):
    """Тестирование функции, передающей курсы валют"""
    mock_get.return_value.json.return_value = {"result": 62.25}
    assert round(currency_rate("USD"), 2) == 62.25



# курс валют на 2021-07-01


def test_price_stocks():
    """Тестирование функции, передающей цены на акции"""
    assert price_stocks("TSLA") == 201.02
