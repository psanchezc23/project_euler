import time
import numpy as np


def exercise_020(number):
    """
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is
    3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!

    :param number: Number to calculate factorial.
    :type number: int

    :return: Sum of digits of factorial
    :rtype: int
    """

    # TODO. number too large

    factorial = np.prod(np.arange(1, number + 1)).astype(np.float64)
    digits = list(map(int, list(str(factorial))))
    return sum(digits)


if __name__ == '__main__':

    start_time = time.time()
    number = 100
    print(exercise_020(number))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
