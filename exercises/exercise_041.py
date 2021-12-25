import time

from itertools import permutations

from exercises.utils import is_prime


def exercise_041():
    """
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
    and is also prime.

    What is the largest n-digit pandigital prime that exists?

    :return: largest pandigital number
    :rtype: int
    """

    max_number = 0
    for n_digits in range(9, 1, -1):
        numbers = range(1, n_digits + 1)
        for number in permutations(numbers):
            number_int = int("".join(map(str, number)))
            if is_prime(number_int):
                max_number = max(max_number, number_int)
    return max_number


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_041())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
