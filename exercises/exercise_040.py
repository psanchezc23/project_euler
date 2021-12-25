import time

import numpy as np


def exercise_040(decimal_positions):
    """
    An irrational decimal fraction is created by concatenating the positive
    integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of
    the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

    :return: multiply decimals
    :rtype: int
    """

    decimals = "."
    number = 1

    max_length = max(decimal_positions)
    while len(decimals) <= max_length:
        decimals += str(number)
        number += 1

    return np.prod([int(decimals[dp]) for dp in decimal_positions])


if __name__ == '__main__':
    start_time = time.time()
    decimal_positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
    print(exercise_040(decimal_positions))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
