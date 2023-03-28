import random


def reverse(str_value):
    return str_value[::-1]


def str_shuffle(str_value):
    str_list = list(str_value)
    random.shuffle(str_list)
    return "".join(str_list)
