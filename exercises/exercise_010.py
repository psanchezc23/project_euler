import time
import numpy as np


def exercise_010(number):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.

    :param number: Maximum number to look for primes
    :type number: int

    :return: sum of all the primes below <number>
    :rtype: int
    """

    prime_cumsum = 2
    watched = np.zeros(number, dtype=bool)
    candidate = 3

    while candidate < number:
        if not watched[candidate - 1]:
            prime_cumsum += candidate
            multiple = candidate
            while multiple < number:
                watched[multiple - 1] = True
                multiple += candidate
        candidate += 2
    return prime_cumsum


def exercise_010_best(number):
    """
    The sieve of Eratosthenes
    """
    sievebound = np.int64((number-1) / 2)
    sieve = np.zeros(sievebound, dtype=bool)
    crosslimit = np.int64((np.floor(np.sqrt(number)) - 1) / 2)
    for i in range(1, crosslimit + 1):
        if not sieve[i]:
            for j in range(2 * i * (i+1), sievebound, 2 * i + 1):
                sieve[j] = True

    total_sum = 2
    for i in range(1, sievebound):
        if not sieve[i]:
            total_sum += 2*i+1
    return total_sum


if __name__ == '__main__':
    start_time = time.time()
    number = 2000000  # 10
    print(exercise_010(number))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

    start_time = time.time()
    number = 2000000  # 10
    print(exercise_010_best(number))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
