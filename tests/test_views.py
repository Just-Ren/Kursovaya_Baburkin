from unittest.mock import patch

from src.views import currency_rate, price_stocks


@patch("requests.get")
def test_currency_rate(mock_get):
    """Тестирование функции, передающей курсы валют"""
    mock_get.return_value.json.return_value = {"result": 62.25}
    assert currency_rate("USD") == 62.249
    if mock_get.return_value.json.return_value:
        try:
            data = json.loads(mock_get.return_value.json.return_value)
        except json.JSONDecodeError as e:
            print(f"Ошибка: {e}")
    else:
        print("JSON строка пуста")


# курс валют на 2021-07-01


def test_price_stocks():
    """Тестирование функции, передающей цены на акции"""
    assert price_stocks("TSLA") == 201.02
