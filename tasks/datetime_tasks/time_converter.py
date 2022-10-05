"""
Написать функцию convert_date, которая будет конвертировать время
из одной временной зоны в другую.

Функция должна принимать 3 аргумента: timestamp, current_zone, new_zone.

Функция должна возвращать время в новой временной зоне.
"""
import datetime


def convert_date():
    timestamp = datetime.timedelta(hours=3)
    current_zone = datetime.datetime.now()
    new_zone = current_zone + timestamp
    return current_zone, new_zone


print(convert_date())
