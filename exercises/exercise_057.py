import time


def _get_next_expansion(numerator, denominator):
    """
    1 + 1 / 1 + (numerator/denominator)

    :param numerator: previous numerator.
    :type numerator: int
    :param denominator: previous denominator.
    :type denominator: int

    :return next_numerator: next numerator.
    :rtype next_numerator: int
    :return next_denominator: next denominator.
    :rtype next_denominator: int
    """
    return 2 * denominator + numerator, numerator + denominator


def _is_valid_fraction(numerator, denominator):
    """
    The fraction is valid if the number of digits of the numerator is greater
    than the number of digits of the denominator.

    :param numerator: previous numerator.
    :type numerator: int
    :param denominator: previous denominator.
    :type denominator: int

    :return: if the number of digits of the numerator is greater
    than the number of digits of the denominator.
    :rtype: bool
    """
    return len(list(str(numerator))) > len(list(str(denominator)))


def exercise_057():
    """
    In the first one-thousand expansions, how many fractions contain a
    numerator with more digits than the denominator?

    :return: Number of numerator with more digits than the denominator
    :rtype: int
    """

    numerator = 3
    denominator = 2
    n_times = 0
    for expansion in range(1, 1000):
        numerator, denominator = _get_next_expansion(numerator, denominator)
        if _is_valid_fraction(numerator, denominator):
            n_times += 1
    return n_times


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_057())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
