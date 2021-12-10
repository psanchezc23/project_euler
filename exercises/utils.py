import numpy as np


def is_prime(number):
    """
    This function returns if a number is prime or not.
    :param number: Number to check if it's prime or not.
    :type number: int

    :return: if the given number is prime or not.
    :rtype: bool
    """

    if number == 1:
        return False
    elif number < 4:  # 2 and 3 are primes
        return True
    elif (number % 2) == 0:  # odd are not primes
        return False
    elif number < 9:  # 5 and 7 are primes (4, 6 and 8 are odds)
        return True
    elif (number % 3) == 0:
        return False
    else:
        maximum_value = np.floor(np.sqrt(number))
        factor = 5
        while factor <= maximum_value:
            if number % factor == 0:
                return False
            if number % (factor + 2) == 0:
                return False
            factor += 6
        return True


def get_divisors(number):
    divisors = {1}
    for i in range(2, np.int64(np.sqrt(number))+1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number / i)
    return divisors


def sum_divisors(number):
    return np.int64(sum(get_divisors(number)))
