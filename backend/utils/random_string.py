from random import SystemRandom
from string import ascii_letters


def random_string(length):
    system_random = SystemRandom()
    return ''.join(system_random.sample(ascii_letters, length))
