import time

from exercises.utils import is_prime


def _all_odd(digits):
    odd_numbers = {"1", "3", "5", "7", "9"}
    return all(digit in odd_numbers for digit in digits)


def _digits_rotations(digits):
    return [digits[i:] + digits[:i] for i in range(len(digits))]


def _is_circular(digits):
    is_circular = True
    perms = set()
    for rotation_digits in _digits_rotations(digits):
        rotation_number = int("".join(rotation_digits))
        if rotation_number not in perms:
            is_circular &= is_prime(rotation_number)
            perms.add(rotation_number)
    return {k: is_circular for k in perms}


def exercise_035(maximum_number):
    """
    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.

    How many circular primes are there below one million?

    :return: Products of coefficients.
    :rtype: int
    """

    circular = {2: True, 3: True}
    number = 3
    n = 1
    while number < maximum_number:
        for number in [6 * n - 1, 6 * n + 1]:
            digits = list(str(number))
            if number not in circular and _all_odd(digits):
                number_circular = _is_circular(digits)
                circular.update(number_circular)
        n += 1
    return len([k for k, v in circular.items() if v])


if __name__ == '__main__':
    start_time = time.time()
    maximum_number = 1000000
    print(exercise_035(maximum_number))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
