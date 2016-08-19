from random import SystemRandom
from string import ascii_letters


system_random = SystemRandom()


def random_string(length=32):
    return ''.join(system_random.sample(ascii_letters, length))
