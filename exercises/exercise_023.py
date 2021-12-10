import time

from exercises.utils import sum_divisors

# By mathematical analysis, it can be shown that all integers greater than
# 28123 can be written as the sum of two abundant numbers
ABUNDANT_LIMIT_NUMBER = 28123


def is_abundant(number):
    return sum_divisors(number) > number


def exercise_023():
    """
    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors
    of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number.

    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
    smallest number that can be written as the sum of two abundant numbers is
    24. By mathematical analysis, it can be shown that all integers greater
    than 28123 can be written as the sum of two abundant numbers. However,
    this upper limit cannot be reduced any further by analysis even though it
    is known that the greatest number that cannot be expressed as the sum of
    two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.

    :return: Sum of numbers that are not sum of two abundant numbers.
    :rtype: int
    """

    abundant_numbers = {
        number for number in range(1, ABUNDANT_LIMIT_NUMBER + 1)
        if is_abundant(number)
    }

    sum_abundant_numbers = {
        number_1 + number_2
        for number_1 in abundant_numbers
        for number_2 in abundant_numbers
    }

    numbers = set(range(1, ABUNDANT_LIMIT_NUMBER + 1))
    return sum(numbers - sum_abundant_numbers)


if __name__ == '__main__':

    start_time = time.time()
    print(exercise_023())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
