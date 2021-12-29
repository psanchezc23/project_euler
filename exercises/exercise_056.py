import time


def exercise_056():
    """
    A googol (10^100) is a massive number: one followed by one-hundred zeros;
    100^100 is almost unimaginably large: one followed by two-hundred zeros.
    Despite their size, the sum of the digits in each number is only 1.

    Considering natural numbers of the form, ab, where a, b < 100, what is the
    maximum digital sum?

    :return: Maximum digit sum
    :rtype: int
    """

    maximum_digit_sum = 0
    for a in range(2, 100):
        for b in range(2, 100):
            digit_sum = sum(map(int, list(str(a ** b))))
            maximum_digit_sum = max(maximum_digit_sum, digit_sum)
    return maximum_digit_sum


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_056())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
