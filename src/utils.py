import csv
import datetime
import logging
import sys
from logging import FileHandler
from pathlib import Path
from typing import List

import pandas as pd

from src.config import ROOT_PATH

sys.path.append(str(Path(__file__).resolve().parent.parent))


logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(filename='logs/utils.log', mode='w')
file_formatted = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatted)
logger.addHandler(file_handler)


def read_excel(path_to_file: Path) -> list:
    """Функция чтения транзакций из excel-файла"""
    with open(path_to_file, "r", encoding="utf-8"):
        try:
            df = pd.read_excel(path_to_file, dtype="object")  # очищаем числовые значения от ненужной информации
            # pd.read_excel("file", dtype="object")
            transactions = []
            for i in range(0, len(df)):
                row_dict = {
                    "Дата операции": df.loc[i, "Дата операции"],
                    "Дата платежа": df.loc[i, "Дата платежа"],
                    "Номер карты": df.loc[i, "Номер карты"],
                    "Статус": df.loc[i, "Статус"],
                    "Сумма операции": df.loc[i, "Сумма операции"],
                    "Валюта операции": df.loc[i, "Валюта операции"],
                    "Валюта платежа": df.loc[i, "Валюта платежа"],
                    "Кешбэк": df.loc[i, "Кэшбэк"],
                    "Категория": df.loc[i, "Категория"],
                    "МСС": df.loc[i, "MCC"],
                    "Описание": df.loc[i, "Описание"],
                    "Бонусы (включая кешбэк)": df.loc[i, "Бонусы (включая кэшбэк)"],
                    "Округление на Инвесткопилку": df.loc[i, "Округление на инвесткопилку"],
                    "Сумма операции с округлением": df.loc[i, "Сумма операции с округлением"],
                }
                transactions.append(row_dict)
        except Exception as e:
            print(e)
            print("Ошибка чтения excel")
            logger.error("Ошибка чтения excel")
            return []
    logger.info("excel-файл прочитан")
    return transactions


def greeting():
    """Функция для определения времени суток и вывода приветствия"""
    current_time = datetime.datetime.now()
    logger.info("Приветствие")
    if 6 <= int(current_time.hour) < 12:
        return "доброе утро!"
    elif 12 <= int(current_time.hour) < 18:
        return "добрый день!"
    elif 18 <= int(current_time.hour) < 23:
        return "добрый вечер!"
    else:
        return "доброй ночи!"


# def data_to_df(path_to_file):
#     df = pd.read_csv(path_to_file, delimiter=",")
#     logger.info("Файл формата csv преобразован в DataFrame")
#     print(df.head())
#     return df


def data_to_df(path_to_file):
    df = pd.read_excel(path_to_file)
    logger.info("Файл формата excel преобразован в DataFrame")
    # print(df.head())
    return df


if __name__ == "__main__":
    path_to_file = Path(ROOT_PATH, "../data/operations.xlsx")
    # path_to_file = Path(ROOT_PATH, "../data/Отчет по операциям.csv")
    data_to_df(path_to_file)
