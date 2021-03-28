import numpy as np


def exercise_003(number):
    """
    The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143.

    :param int number: Number to calculate prime factors.
    :return: largest primer factor.
    :rtype: int

    """

    while (number % 2) == 0:
        number /= 2

    primes = np.arange(3, int(number / 2), 2)
    is_prime = np.ones(len(primes), dtype=bool)
    i = 0
    while np.any(is_prime[i:]) and i < (len(is_prime)-1):
        if is_prime[i]:
            n = primes[i]
            is_prime[(i+1):] &= (primes[(i+1):] % n) != 0
        i += 1

    primes = primes[is_prime]

    is_divisor = number % primes == 0

    return max(primes[is_divisor])


if __name__ == '__main__':
    number = 600851475143  # 13195
    print(exercise_003(number))
