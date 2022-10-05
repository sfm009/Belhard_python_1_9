"""
Написать функцию add_to_path, которая будет добавлять директорию, в которой находится
переданный файл (путь к файлу) в sys.path
"""
import pathlib
import sys


def add_to_path():
    sys.path.extend([
        str(pathlib.Path(__file__).parent.resolve())
    ])
