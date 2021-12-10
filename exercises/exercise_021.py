import time
import numpy as np

from exercises.utils import sum_divisors


def exercise_021(number_limit):
    """
    Let d(n) be defined as the sum of proper divisors of n (numbers less than
    n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
    and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
    44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are
    1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.

    :param number_limit: Number to calculate factorial.
    :type number_limit: int

    :return: Sum of digits of factorial
    :rtype: int
    """

    numbers_to_check = np.arange(1, number_limit)
    checked_numbers = dict()
    amicable_numbers = set()

    for number in numbers_to_check:
        if number not in checked_numbers:
            d_number = sum_divisors(number)
            checked_numbers[number] = d_number
            if number != d_number:
                d_d_number = sum_divisors(d_number)
                checked_numbers[d_number] = d_d_number

                if number == d_d_number:
                    amicable_numbers.add(number)
                    amicable_numbers.add(d_number)

    return sum(amicable_numbers)


if __name__ == '__main__':

    start_time = time.time()
    number_limit = 10000
    print(exercise_021(number_limit))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
