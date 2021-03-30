import time
import numpy as np


def exercise_007(n_prime):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?

    :param int n_prime: Number of prime numbers.
    :return: <n_prime>-th prime number.
    :rtype: int

    """

    n = 1
    number = 1

    while n <= n_prime:
        number += 1
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            n += 1

    return number


def exercise_007_best(n_prime):

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

    count = 1
    candidate = 1
    while count < n_prime:
        candidate += 2
        if _is_prime(candidate):
            count += 1

    return candidate


if __name__ == '__main__':
    start_time = time.time()
    n_prime = 10001  # 10
    print(exercise_007(n_prime))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

    start_time = time.time()
    print(exercise_007_best(n_prime))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
