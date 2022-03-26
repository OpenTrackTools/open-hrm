import random


def random_abbr(self):
    chars = 'abcdefghijklmnopqrstuvwxyz'.upper()
    len = 6
    return ''.join(random.choices(chars, k=len))
