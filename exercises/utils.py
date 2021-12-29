import numpy as np


def is_prime(number):
    """
    This function returns if a number is prime or not.

    :param number: Number to check if it's prime or not.
    :type number: int

    :return: if the given number is prime or not.
    :rtype: bool
    """

    if number < 1:
        return False
    elif number == 1:
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


def range_product(lo, hi):
    if lo + 1 < hi:
        mid = (hi + lo) // 2
        return range_product(lo, mid) * range_product(mid + 1, hi)
    if lo == hi:
        return lo
    return lo * hi


def factorial(number):
    return range_product(1, number)


def large_sum(number_1, number_2):
    """
    Sum of two large numbers
    """
    number_1_rev = str(number_1)[::-1]
    len_number_1 = len(number_1_rev)
    number_2_rev = str(number_2)[::-1]
    len_number_2 = len(number_2_rev)

    carry = 0
    final_sum = ""
    for i in range(max(len_number_1, len_number_2)):
        n1 = int(number_1_rev[i]) if i < len_number_1 else 0
        n2 = int(number_2_rev[i]) if i < len_number_2 else 0
        carry, digit = divmod(n1 + n2 + carry, 10)
        final_sum += str(digit)

    if carry:
        final_sum += str(carry)

    return final_sum[::-1]


def long_division(dividend, divisor):
    quotient, rem = divmod(dividend, divisor)
    dec = ""
    dividends = []
    while rem not in dividends and rem != 0:
        dividends.append(rem)
        rem *= 10
        quot, rem = divmod(rem, divisor)
        dec += str(quot)

    if rem != 0:
        cycle_index = dividends.index(rem)
        dec = "{}({})".format(dec[:cycle_index], dec[cycle_index:])
    return "{}.{}".format(quotient, dec)
