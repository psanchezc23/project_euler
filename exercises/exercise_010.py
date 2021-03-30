import time
import numpy as np


def exercise_010(number):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.

    :param int number: Maximum number to look for primes
    :return: sum of all the primes below <number>
    :rtype: int

    """

    def _is_prime(n):
        if n == 1:
            return False
        elif n < 4:  # 2 and 3 are primes
            return True
        elif (n % 2) == 0:  # odd are not primes
            return False
        elif n < 9:  # 5 and 7 are primes (4, 6 and 8 are odds)
            return True
        elif (n % 3) == 0:
            return False
        else:
            maximum_value = np.floor(np.sqrt(n))
            factor = 5
            while factor <= maximum_value:
                if n % factor == 0:
                    return False
                if n % (factor + 2) == 0:
                    return False
                factor += 6
            return True

    prime_cumsum = 2
    candidate = 3
    while candidate < number:
        if _is_prime(candidate):
            prime_cumsum += candidate
        candidate += 2

    return prime_cumsum


if __name__ == '__main__':
    start_time = time.time()
    number = 2000000  # 10
    print(exercise_010(number))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
