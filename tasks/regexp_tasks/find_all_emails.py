"""
Написать функцию find_emails, которая принимает текст и находит в нем
все email вида some@some.some
"""
import re


def find_emails(email: str):
    result = re.findall(r'\w+@\w+.\w+', email)
    return result


print(find_emails('some@some.some other text ms@ms.ms'))
