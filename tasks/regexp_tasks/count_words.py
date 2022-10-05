"""
Написать функцию count_words, которая будет считать количество слов в тексте,
с учетом, что в начале могут быть пробелы, в конце могут быть пробелы, между слов
может встречаться больше одного пробела подряд.
"""
import re


def count_words(string: str):
    result = re.split(r'^\s+|\s+|\s+$', string)
    result.pop(0)
    result.pop(-1)
    return len(result)


print(count_words(' One Two  Three    Four Five '))
