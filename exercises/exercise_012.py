import time

from exercises.utils import get_divisors


def exercise_012(n_divisors):
    """
    The sequence of triangle numbers is generated by adding the natural
    numbers. So the 7th triangle number would be
    1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred
    divisors?

    :param n_divisors: Number of divisors
    :type n_divisors: int

    :return: first triangle number with at least <n_divisors> divisors.
    :rtype: int
    """

    triangle_number = 3
    next_number = 3
    triangle_number_divisors = []

    while len(triangle_number_divisors) < n_divisors:
        triangle_number += next_number
        next_number += 1

        triangle_number_divisors = get_divisors(triangle_number)

    return triangle_number


if __name__ == '__main__':
    start_time = time.time()
    n_divisors = 500  # 4
    print(exercise_012(n_divisors))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))