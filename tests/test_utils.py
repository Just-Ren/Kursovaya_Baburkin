import sys
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

import pytest

from src.config import ROOT_PATH
from src.utils import greeting, read_excel


@pytest.fixture()
def path_to_file():
    return "/Users/evgen/PycharmProjects/Kursovaya_Baburkin/data/OperationsTest.xlsx"


def test_read_excel(path_to_file):
    assert read_excel(path_to_file) == [
        {
            "Бонусы (включая кешбэк)": 3,
            "Валюта операции": "RUB",
            "Валюта платежа": "RUB",
            "Дата операции": "31.12.2021 16:44:00",
            "Дата платежа": "31.12.2021",
            "Категория": "Супермаркеты",
            "Кешбэк": 0,
            "МСС": 5411,
            "Номер карты": "*7197",
            "Округление на Инвесткопилку": 0,
            "Описание": "Колхоз",
            "Статус": "OK",
            "Сумма операции": -160.89,
            "Сумма операции с округлением": 160.89,
        },
        {
            "Бонусы (включая кешбэк)": 1,
            "Валюта операции": "RUB",
            "Валюта платежа": "RUB",
            "Дата операции": "31.12.2021 16:42:04",
            "Дата платежа": "31.12.2021",
            "Категория": "Супермаркеты",
            "Кешбэк": 0,
            "МСС": 5411,
            "Номер карты": "*7197",
            "Округление на Инвесткопилку": 0,
            "Описание": "Колхоз",
            "Статус": "OK",
            "Сумма операции": -64,
            "Сумма операции с округлением": 64,
        },
    ]


@patch("src.utils.datetime")
@pytest.mark.parametrize(
    "current_hour, expected_greeting",
    [
        (8, "доброе утро!"),
        (14, "добрый день!"),
        (21, "добрый вечер!"),
        (3, "доброй ночи!"),
    ],
)
def test_greeting(mock_datetime, current_hour, expected_greeting):
    mock_now = datetime(2021, 7, 25, current_hour, 0, 0)
    mock_datetime.datetime.now.return_value = mock_now
    result = greeting()
    assert result == expected_greeting