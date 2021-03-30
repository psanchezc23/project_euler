import numpy as np
import time


def exercise_003(number):
    """
    The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143.

    :param int number: Number to calculate prime factors.
    :return: largest primer factor.
    :rtype: int

    """

    max_prime = 1

    while number % 2 == 0:
        number /= 2
        max_prime = 2

    for i in range(3, int(np.sqrt(number))+1, 2):
        while (number % i) == 0:
            number /= i
            max_prime = max(max_prime, i)

    if number > 2:
        max_prime = max(number, max_prime)

    return max_prime


if __name__ == '__main__':
    start_time = time.time()
    number = 600851475143  # 13195
    print(exercise_003(number))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
