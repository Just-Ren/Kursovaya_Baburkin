import os
from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.reports import spending_by_category


@pytest.fixture
def sample_transactions():
    return [
        {"���� ��������": "01.01.2024 12:00:00", "���������": "���", "�����": 100},
        {"���� ��������": "15.02.2024 12:00:00", "���������": "���������", "�����": 50},
        {"���� ��������": "10.03.2024 12:00:00", "���������": "���", "�����": 200},
        {"���� ��������": "20.04.2024 12:00:00", "���������": "���", "�����": 300},
    ]


def test_spending_by_category(sample_transactions):
    df_transactions = pd.DataFrame(sample_transactions)
    current_datetime = "20.04.2024 12:00:00"
    category = "���"

    mock_open_func = mock_open()

    with patch("builtins.open", mock_open_func):
        result = spending_by_category(df_transactions, category, current_datetime)

    # ���������, ��� ������������ ��������� ������������� ����������
    expected_result = [
        {"���� ��������": "10.03.2024 12:00:00", "���������": "���", "�����": 200},
        {"���� ��������": "20.04.2024 12:00:00", "���������": "���", "�����": 300},
    ]
    assert result == expected_result

    # ���������, ��� ���� ��� ������ ��� ������
    mock_open_func.assert_called_once_with(os.path.abspath("../data/log_file.json"), "w", encoding="utf-8")


# ������ ������
if __name__ == "__main__":
    pytest.main()
