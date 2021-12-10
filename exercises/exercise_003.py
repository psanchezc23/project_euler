import numpy as np
import time


def exercise_003(prime_factor_number):
    """
    The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
    factor of the number 600851475143.

    :param prime_factor_number: Number to calculate prime factors.
    :type prime_factor_number: int

    :return: largest primer factor.
    :rtype: int
    """

    max_prime = 1

    while prime_factor_number % 2 == 0:
        prime_factor_number /= 2
        max_prime = 2

    for i in range(3, int(np.sqrt(prime_factor_number))+1, 2):
        while (prime_factor_number % i) == 0:
            prime_factor_number /= i
            max_prime = max(max_prime, i)

    if prime_factor_number > 2:
        max_prime = max(prime_factor_number, max_prime)

    return max_prime


if __name__ == '__main__':
    start_time = time.time()
    prime_factor_number = 600851475143  # 13195
    print(exercise_003(prime_factor_number))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
