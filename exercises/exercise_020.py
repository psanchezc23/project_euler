import time

from exercises.utils import range_product


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

    if number < 2:
        return 1
    factorial = range_product(1, number)
    factorial_digits = list(map(int, list(str(factorial))))
    return sum(factorial_digits)


if __name__ == '__main__':

    start_time = time.time()
    number = 10
    print(exercise_020(number))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
