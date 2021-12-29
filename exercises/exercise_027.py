import time

from exercises.utils import is_prime


def exercise_027():
    """
    Euler discovered the remarkable quadratic formula:

    n^2 + n + 41

    It turns out that the formula will produce 40 primes for the consecutive
    integer values 0 <= b <= 39 . However, when n = 40, 40^2 + 40 + 41 =
    40(40 + 1) + 41 is divisible by 41, and certainly when
    is clearly divisible by 41.

    The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
    primes for the consecutive values 0 <= n <= 79. The product of the
    coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

    n^2 + an + b, where |a|<1000 and |b| <= 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4
    Find the product of the coefficients, a and b, for the quadratic
    expression that produces the maximum number of primes for consecutive
    values of n, starting with n = 0.

    :return: Products of coefficients.
    :rtype: int
    """

    primes = {}

    # b should be prime
    b_values = []
    for b in range(1, 1001, 1):
        primes[b] = is_prime(b)
        if primes[b]:
            b_values.append(b)

    maximum_length = 0
    solution = 0

    # a must be odd
    for a in range(-999, 1000, 2):
        for b in b_values:
            n = 1
            prime = True
            while prime:
                n += 1
                number = n ** 2 + a * n + b
                if number not in primes:
                    primes[number] = is_prime(number)
                prime = primes[number]
            if n > maximum_length:
                maximum_length = n
                solution = a * b
    return solution


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_027())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
