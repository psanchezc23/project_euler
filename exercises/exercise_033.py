import time
from math import gcd


def _is_unorthodox_cancellable(numerator, denominator, i):
    return denominator * (10 * numerator + i) == \
           numerator * (10 * i + denominator)


def exercise_033():
    """
    The fraction 49/98 is a curious fraction, as an inexperienced
    mathematician in attempting to simplify it may incorrectly believe that
    49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less
    than one in value, and containing two digits in the numerator and
    denominator.

    If the product of these four fractions is given in its lowest common
    terms, find the value of the denominator.

    :return: The denominator its lowest common terms of the product of these
    four fractions.
    :rtype: int
    """

    denominator_product = 1
    numerator_product = 1
    for i in range(1, 10):
        for denominator in range(1, i):
            for numerator in range(1, denominator):
                if _is_unorthodox_cancellable(numerator, denominator, i):
                    numerator_product *= numerator
                    denominator_product *= denominator
    denominator_product /= gcd(numerator_product, denominator_product)
    return int(denominator_product)


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_033())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
