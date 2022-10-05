"""
Написать функцию check_login, которая будет принимать строку и проверять,
что она является логином, который соответствует следующим правилам:
1. Длина от 5 до 20 символов
2. Состоит из букв верхнего и нижнего регистра, цифр, знаков подчеркивания
"""
import re


def check_login(string: str):
    pattern = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[_])(?:.{5,20})')
    if pattern.match(string):
        print('valid login')
    else:
        print('not valid login')


check_login('sfS_m009')
