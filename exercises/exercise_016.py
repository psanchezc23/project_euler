import time
import numpy as np


def exercise_016(exponent):
    """
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?

    :param exponent: Exponent
    :type exponent: int

    :return: Sum of the digits of the number
    :rtype: int
    """

    digits = list(str(2 ** exponent))
    return np.sum(list(map(int, digits)))


if __name__ == '__main__':
    start_time = time.time()
    exponent = 1000
    print(exercise_016(exponent))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
