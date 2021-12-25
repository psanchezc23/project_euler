import time


def exercise_006(n_natural):
    """
    The sum of the squares of the first ten natural numbers is,
        1^2 + 2^2 + 3^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,
        (1 + 2 + 3 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 - 385 = 2640. Find the
    difference between the sum of the squares of the first one hundred natural
    numbers and the square of the sum.

    :param n_natural: Number of natural numbers
    :type n_natural: int

    :return: difference between the sum of the squares of the first
    <n_natural> natural numbers and the square of the sum.
    :rtype: int
    """

    cumsum = 0
    sum_square = 0
    for natural in range(1, n_natural+1):
        cumsum += natural
        sum_square += natural ** 2

    difference = cumsum ** 2 - sum_square

    return difference


def exercise_006_best(n_natural):
    cumsum = n_natural * (n_natural + 1) / 2
    sum_square = (2 * n_natural + 1) * (n_natural + 1) * n_natural / 6
    difference = cumsum ** 2 - sum_square
    return difference


if __name__ == '__main__':
    n_natural = 100  # 10
    start_time = time.time()
    print(exercise_006(n_natural))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

    start_time = time.time()
    print(exercise_006_best(n_natural))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
